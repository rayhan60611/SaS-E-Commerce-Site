# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
#importing custopm user
from django.contrib.auth import get_user_model
#Registrstion Admin class
from django.contrib.auth.admin import UserAdmin



admin.site.unregister(Group)
class registrationAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name', 'mobile','show_Image','address','is_active','is_admin','is_staff')
    list_filter = ('is_admin','is_staff','is_active')

    
    
    fieldsets = (
        ('User Credentials',{'fields': ('email','last_login','password')}),
        ('Personal Informations', {'fields': ('first_name', 'last_name', 'mobile',('image','show_Image'),'address',)}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_active')})
    )

   
    add_fieldsets = (
        (
            None,{
                'fields':('email','first_name', 'last_name' ,'mobile','image','address','is_active','last_login','password1','password2')
            }
        ),
        ('Permissions',{'fields': ('is_admin' , 'is_staff' ,'is_active') }
        
        )
    )
    readonly_fields = ('show_Image',) # for showing the image in the admin panel
    

    ordering = ('email',)
    search_fields =('email', 'mobile','first_name', 'last_name')
    filter_horizontal =()


#registering the user
user = get_user_model()
admin.site.register(user,registrationAdmin)