from django.db import models

class registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email  =  models.CharField(max_length=100)
    mobile = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    address = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"Name:{self.first_name} {self.last_name} --- Mobile No:{self.mobile}"
    

    
    


