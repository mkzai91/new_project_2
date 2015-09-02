from django.contrib import admin
from bid import models
class CustomAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomAdmin, self).__init__(model, admin_site)

@admin.register(models.Product)
class adminProduct(admin.ModelAdmin):
    search_fields =['name',]
    list_filter = ['publish_date',]
    list_display=['name','publish_date','price','expire_date','bid_price','photo','website','total_view',]


@admin.register(models.WorkSheet)
class WorkSheetAdmin(CustomAdmin, admin.ModelAdmin):
    search_fields =['title',]
    list_filter = ['pub_date']

@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    search_fields =['username',]
    list_display=['username','name','email',]

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['Product_ID','text']