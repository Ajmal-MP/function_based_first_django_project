from django.contrib import admin
from .models import category,SubCategory
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug','created_at']

class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('sub_category_name',)}
    list_display=['sub_category_name','slug','created_at']


admin.site.register(category,categoryAdmin)
admin.site.register(SubCategory,SubcategoryAdmin)