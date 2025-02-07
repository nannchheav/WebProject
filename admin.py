from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ExportActionMixin
# Register your models here.

admin.site.site_header = "Administrator"
admin.site.site_title = "ACLEDA University of Business Admin Panel"
admin.site.index_title = "Admin Panel"

class ExpProduct(resources.ModelResource):
    class Meta:
        model = tblProducts
        fields = ('id','productName','productImage','product_ratting','old_price','current_price','description')
class ProductAdmin( ExportActionMixin,admin.ModelAdmin):
    list_display = ["image_preview","id","productImage","productName","categoryID","product_ratting","old_price","current_price","description","productDate"]
    list_filter = ["productDate"]
    search_fields = ["productName"]
    date_hierarchy = "productDate"
    resource_class = ExpProduct
    readonly_fields = ["image_preview"]
    
    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'
    def __init__(self, model, admin_site):
            super().__init__(model, admin_site)
            self.opts.verbose_name_plural="Manage Products"
# class ClientAdmin( ExportActionMixin,admin.ModelAdmin):
#     list_display = ["image_preview","id","clientName","clientImage","clientDescription"]
#     readonly_fields = ["image_preview"]
    
#     def image_preview(self, obj):
#         if obj.clientImage:
#             return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.clientImage.url)
#         return "No Image"

#     image_preview.short_description = 'Image Preview'
#     def __init__(self, model, admin_site):
#             super().__init__(model, admin_site)
#             self.opts.verbose_name_plural="Manage Client"



class ExpCategory(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id','categoryName','categoryImage')
class CategoryAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ["image_preview","id","categoryImage","categoryName","date_created"]
    list_filter = ["date_created"]
    search_fields = ["categoryName"]
    date_hierarchy = "date_created"
    resource_class = ExpCategory
    readonly_fields = ["image_preview"]
    def image_preview(self, obj):
        if obj.categoryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.categoryImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'
    def __init__(self, model, admin_site):
            super().__init__(model, admin_site)
            self.opts.verbose_name_plural="Manage Categories"

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","phone","email","date_created"]
    list_filter = ["date_created"]
    search_fields = ["name"]
    date_hierarchy = "date_created"
# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(tblProducts, ProductAdmin)
admin.site.register(tblSocialMedia)
admin.site.register(tblTopMenu)
admin.site.register(tblSubTopMenu)
admin.site.register(TblBlogType)
admin.site.register(TblBlog)
admin.site.register(tblProductDetail)
admin.site.register(tblSlides)
admin.site.register(tblFooter)
admin.site.register(tblBanner)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Payment)



