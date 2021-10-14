from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
   if request.method != 'POST':
      return render(request, 'accounts/register.html')
   
   first_name = request.POST['first_name'].capitalize()
   last_name = request.POST['last_name'].capitalize()
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']
   password2 = request.POST['password2']
   
   allUsers = User.objects
   
   if password != password2:
      messages.error(request, 'Passwords do not match!')
      return redirect('register')

   if allUsers.filter(username = username).exists():
      messages.error(request, 'Username already taken!')
      return redirect('register')
   
   if allUsers.filter(email = email).exists():
      messages.error(request, 'Email already taken!')
      return redirect('register')      
   
   user = User.objects.create(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
   
   user.save()
   messages.success(request, 'Successfully registered!')
   return redirect('login')
   
def login(request):
   if request.method != 'POST':
      return render(request, 'accounts/login.html')
   
   username = request.POST['username']
   password = request.POST['password']
   
   user = auth.authenticate(username = username, password = password)
   
   if user is None:
      messages.error(request, 'Invalid credentials!')
      return redirect('login')
   
   auth.login(request, user)
   messages.success(request, 'You are now logged in!')
   return redirect('dashboard')

def logout(request):
   if request.method == "POST":
      auth.logout(request)
      messages.success(request, 'You are now logged out.')
      return redirect('index')

def dashboard(request):
   user_contacts = Contact.objects.filter(user_id=request.user.id).order_by('-contact_date')
   context = {
      'contacts': user_contacts
   }
   return render(request, 'accounts/dashboard.html', context)


