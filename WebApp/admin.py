
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile,Product

#unregister groups
#admin.site.unregister(Group)

# Register your models here.
class ProfileInLine(admin.StackedInline):
    model = Profile
#extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #just display username fields on admin page
    fields = ['username','password']
    inlines = [ProfileInLine]
    
admin.site.unregister(User)

#reregister User
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

#register 
admin.site.register(Product)

class ProductRecordAdmin(admin.ModelAdmin):
    list_display = ('name','product_description','product_price')
    ordering = ('name',)
    search_fields =  ('name','product_description','product_price')