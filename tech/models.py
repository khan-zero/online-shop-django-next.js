from django.db import models

class Hero(models.Model):
    hero_images = models.ImageField()

class Products(models.Model):
    main_img = models.ImageField()
    describtion = models.TextField()
    name = models.CharField(max_length=255)
    
class DeliverlyArea(models.Model):
    location = models.ImageField()
    title = models.CharField(max_length=255)
    describtion = models.TextField()
    
class NavList(models.Model):
    dev_pos_name = models.CharField(max_length=255)
    dev_name = models.CharField(max_length=255)
    dev_link = models.URLField()

class NavbarFooter(models.Model): 
    call_center = models.CharField(max_length=255)
    describtion = models.CharField(max_length=255)
    developers = models.ForeignKey(NavList, on_delete=models.CASCADE)


