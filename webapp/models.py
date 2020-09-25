from django.db import models

# Create your models here.
class Register(models.Model):
	Fullname=models.CharField(max_length=50)
	Email=models.CharField(max_length=50)
	Password=models.CharField(max_length=50)
	ConfirmPassword=models.CharField(max_length=50)
	
	class Meta:
		db_table="Register"