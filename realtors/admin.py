from django.contrib import admin
from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
   list_display_links = ('id', 'name')
   list_editable = ('is_mvp',)
   list_per_page = 20
   search_fields = ('name', 'email')
   
admin.site.register(Realtor, RealtorAdmin)

