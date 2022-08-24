from django.db import models
from django.utils.text import slugify
# Create your models here.

class category(models.Model):
    #to auto generate slug field
    def save(self,*args,**kwargs):
          self.slug = slugify(self.category_name)
          super(category,self).save(*args,**kwargs)  
    category_name=models.CharField(max_length=20,unique=True)
    slug = models.SlugField(max_length=20,default=category_name)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self) -> str:
        return self.category_name

class SubCategory(models.Model):

    #to auto generate slug field
    def save(self,*args,**kwargs):
          self.slug = slugify(self.sub_category_name)
          super(SubCategory,self).save(*args,**kwargs)

    sub_category_name=models.CharField(max_length=20,unique=True)
    slug=models.SlugField(max_length=100,default=sub_category_name)
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    class Meta:
        verbose_name='Sub category'
        verbose_name_plural='Sub Categories'
    def __str__(self) -> str:
        return self.sub_category_name