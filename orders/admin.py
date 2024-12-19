from django.contrib import admin
from orders.models import Order,OrderedItem
from django.utils.html import format_html


# Register your models here.
class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extra = 0  # No extra empty rows by default
    fields = ('product', 'quantity', 'get_product_image', 'get_product_price')
    readonly_fields = ('get_product_image', 'get_product_price')

    def get_product_image(self, obj):
        if obj.product and obj.product.image:
            return format_html('<img src="{}" width="50" height="50"/>', obj.product.image.url)
        return "No Image"
    get_product_image.short_description = 'Product Image'

    def get_product_price(self, obj):
        return obj.product.price if obj.product else "No Price"
    get_product_price.short_description = 'Product Price'

class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]
    search_fields=[
        "owner",
        "id",
    ]
    list_display = ('id', 'owner', 'total_price', 'created_at', 'get_customer_address', 'get_customer_phone')

    def get_customer_address(self, obj):
        return obj.owner.address  # Fetching the address from the related Customer model
    get_customer_address.short_description = 'Customer Address'

    def get_customer_phone(self, obj):
        return obj.owner.phone  # Fetching the phone number from the related Customer model
    get_customer_phone.short_description = 'Customer Phone'


admin.site.register(Order,OrderAdmin)


