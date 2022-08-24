from django import forms
from .models import category,SubCategory
class CategoryForm(forms.ModelForm):

    class Meta:
        model = category
        fields= ['category_name']

class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = ['sub_category_name','category']