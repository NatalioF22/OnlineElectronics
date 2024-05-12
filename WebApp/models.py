from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms 
from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    

    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = "Categories"
            verbose_name_plural = "Categories"
            db_table = 'categories'  # Ex

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=5000, default="", null=True, blank=True)
    product_price = models.CharField(max_length=500, default="", null=True)
    product_link = models.CharField(max_length=500, default="", null=True)
    image = models.ImageField(upload_to='static', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)  # Changed to ForeignKey

    def __str__(self):
        return self.name
   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, blank=True, max_length=500)
    last_name = models.CharField(null=True, blank=True, max_length=500)
    profile_image = models.ImageField(upload_to='static', null=True, blank=True)
    profile_bio = models.CharField(max_length=500, null=True, blank=True)
    website_link = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    instagram_link = models.CharField(max_length=100, null=True, blank=True)
    linkedIn_link = models.CharField(max_length=100, null=True, blank=True)
    
	
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
# Create Profile When New User Signs Up
#@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
		
		
		user_profile.save()

post_save.connect(create_profile, sender=User)


def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
       
        user.delete()  # Delete the user
        return True
    except User.DoesNotExist:
        return False

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        #user_profile.follows.set([instance.profile.id])
        


class ProductPost(models.Model):
    user = models.ForeignKey(User, related_name="product_post", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1000)
    product_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    product_link = models.CharField(max_length=1000)
    product_price = models.CharField(max_length=100)
   
    def __str__(self) -> str:
        return f"{self.product_name} {self.product_price}: {self.product_description}"