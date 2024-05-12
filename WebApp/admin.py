from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, Product, Categories

# Extend UserAdmin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Configure Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_description', 'product_price', 'category')
    list_select_related = ('category',)  # Optimizes ForeignKey resolution
    search_fields = ('name', 'product_description', 'product_price')
    ordering = ('name',)

# Configure Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register models with their custom Admin interfaces
admin.site.register(Product, ProductAdmin)
admin.site.register(Categories, CategoryAdmin)

# Optionally, register Profile if needed directly (not recommended if using inlines with User)
# admin.site.register(Profile)
