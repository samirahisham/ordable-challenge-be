
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from merchants.models import Store

# Create your models here.




class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField( unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Merchant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="merchant")
    employee_id=models.CharField(max_length=20,unique=True)


class StoreMerchant(models.Model):
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE,related_name="store_merchant")
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name="merchants")
    is_admin=models.BooleanField(default=False)


class StoreDriver(models.Model):
    driver=models.OneToOneField(User,on_delete=models.CASCADE,related_name="driver")
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name="drivers")
    employee_id=models.CharField(max_length=20,unique=True)
    phone_number=models.CharField(max_length=20)