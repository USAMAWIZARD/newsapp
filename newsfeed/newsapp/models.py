from django.db import models
class user(models.Model):
	name=models.CharField(max_length=100)
	selectedfields=models.CharField(max_length=100)
class admin(models.Model):	
	availablecat=models.CharField(max_length=100)
