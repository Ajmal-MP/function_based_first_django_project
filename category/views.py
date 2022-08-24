import imp
from django.shortcuts import render,redirect
from .form import CategoryForm,SubCategoryForm
from category.models import category,SubCategory  


def admin_category(request):
    cat=category.objects.all()
    form = CategoryForm()
    context={
        'category':cat,
        'form':form
    }
    return render(request,'admin/admin-category.html',context)


def admin_sub_category(request,id):
    sub_cat=SubCategory.objects.filter(category = id )
    form = SubCategoryForm()
    context={
        'sub_category':sub_cat,
        'form':form
    }
    return render(request,'admin/admin-sub-category.html',context)


def add_category(request):
    if request.method == 'POST':
        form= CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect(admin_category)
        

def add_sub_category(request):
    if request.method == 'POST':
        form= SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect(admin_sub_category)