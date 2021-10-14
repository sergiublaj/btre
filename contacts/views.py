from django.shortcuts import redirect, render
from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail

def contact(request):
   if request.method != "POST":
      return render(request, '/listings')
   
   print(request.POST)
   
   listing_id = request.POST.get('listing_id', 0)
   listing = request.POST.get('listing', 'Title')
   name = request.POST['name']
   email = request.POST['email']
   phone = request.POST['phone']
   message = request.POST['message']
   user_id = request.POST['user_id']
   
   contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
   
   print(contact)
   
   if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
      if has_contacted:
         messages.error(request, 'You have already made an inquiry for this listing.')
         return redirect('/listings/' + listing_id)
   
   contact.save()
   
   messages.success(request, 'Your request has been submitted, a realtor will get back to you soon.')
   
   return redirect('/listings/' + listing_id)
