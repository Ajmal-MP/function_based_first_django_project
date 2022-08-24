from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser
)

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,mobile,password=None):
        '''
        create and save a user with the given and 
        date of birth and password.
        '''
        if not email:
            raise ValueError('user Must have an email adders')
        if not mobile:
            raise ValueError('user Must have an mobile')
        user=self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,mobile,email,password):
        '''
        create and save a superuser with the given email and 
        date of birth and password.
        '''
        user=self.create_user(
            email=self.normalize_email(email),
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

        
class Account(AbstractBaseUser):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50,unique=True)
    mobile=models.CharField(max_length=50,unique=True)
    
    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=True)
    
    objects = MyAccountManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','mobile']
    
    def _str_(self) :
        return self.email
    
    def has_perm(self,prem,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True