from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer
# Register your models here.

# Customizing the UserAdmin to show customer details
# Customizing the UserAdmin to show customer details
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer Profile'
    fields = ('address', 'phone')  # Fields from the Customer model to display

class CustomUserAdmin(admin.ModelAdmin):
    # Define the fields to display in the user list and edit page
    list_display = ('username', 'email', 'get_address', 'get_phone')  # Show address and phone
    inlines = [CustomerInline]  # Display Customer inline form on the User change page

    # Add only customer fields to fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Customer Profile', {'fields': ('customer_profile',)}),  # You can optionally include customer_profile here
    )

    def get_address(self, obj):
        customer = obj.customer_profile if hasattr(obj, 'customer_profile') else None
        return customer.address if customer else 'No address'

    def get_phone(self, obj):
        customer = obj.customer_profile if hasattr(obj, 'customer_profile') else None
        return customer.phone if customer else 'No phone number'

    get_address.short_description = 'Customer Address'
    get_phone.short_description = 'Customer Phone Number'

    
# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
