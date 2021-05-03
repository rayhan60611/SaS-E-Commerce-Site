from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

from django.utils.html import mark_safe #for Image show in admin panel

# deleting images
from django.dispatch import receiver 
import os


# creating  user
class RegistrationManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, mobile, address ,image , password=None):
        if not email:
            raise ValueError('User Must Have An Unique Email Address')
        email = email.lower()
        first_name = first_name.title()
        last_name = last_name.title()

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            address = address,
            image = image
        )

        user.set_password(password)
        user.save(using = self._db)

        return user

# creating  superuser
    def create_superuser(self, email, first_name, last_name, mobile, address, password=None):
        if not email:
            raise ValueError('Superuser Must Have An Unique Email Address')
        email = email.lower()
        first_name = first_name.title()
        last_name = last_name.title()

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            address =address
        )

        user.set_password(password)
        user.is_admin =True
        user.is_staff =True
        user.save(using = self._db)
        return user


class Registration(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email  =  models.CharField(max_length=100, unique =True, verbose_name='Email',help_text='It is also used as Username')
    mobile = models.CharField(max_length=100 ,verbose_name='Mobile No')
    image = models.ImageField(upload_to='pics',verbose_name='Photo', blank=True)
    address = models.TextField(verbose_name='Address')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'mobile','address')

    object = RegistrationManager()


    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self , perm , obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class meta:
        verbose_name_plural = 'Users'
        
    #for showing image:

    def show_Image(self):
        if self.image:
            return mark_safe(f'<img src="/media/{self.image}" style="width: 45px; height:45px;" />')
        else:
            return mark_safe(f'<img src="/static/noImagefound.jpg" style="width: 45px; height:45px;" />')
    
    show_Image.short_description = mark_safe('<b>Image Preview</b>')

#image delete
@receiver(models.signals.post_delete, sender=Registration)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

#update image 
@receiver(models.signals.pre_save, sender=Registration)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.object.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

# class registration(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email  =  models.CharField(max_length=100)
#     mobile = models.IntegerField()
#     image = models.ImageField(upload_to='pics')
#     address = models.TextField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return f"Name:{self.first_name} {self.last_name} --- Mobile No:{self.mobile}"
    

    
    


