from django.db import models


MENU_CHOICES=[
    ('TEA/COFFEE','Tea/Coffee'),
    ('FRAPPE/CHILLERS','Frappe/Chillers'),
    ('SMOOTHIE','Smoothie'),
    ('PANCAKE','Pancakes'),
    ('EGGS/VEGTABLE EGG MEDLEY','Eggs/Vegetable Egg Medley'),
    ('PANINIS','Paninis'),
    ('SUBS','Subs'),
    ('WRAPS','Wraps'),
    ('WAFFLES','Waffle'),
    ('TOAST','Toast'),
    ('HOTPASTA','Hot-Pasta'),
    ('BAGELS','Bagels'),
    ('FRIES','Fries'),
    ('SALADS','Salads'),
]

# Create your models here.
class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=100)
    item_description= models.CharField(max_length=500 , blank=True)
    item_price = models.DecimalField(max_digits=8,decimal_places=2)
    item_picture = models.ImageField( blank=True)
    item_category = models.CharField(max_length=100,default=' ', choices=MENU_CHOICES)

    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return self.item_name


class NewsLetter(models.Model):
    email_id = models.AutoField(primary_key=True)
    email_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=64)
    telephone_number =models.CharField(max_length=10,default=" ")
    home_address =models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=300,default=" ")


    def __str__(self):
        return self.email_address
# This class would be used for further expansion
# class OnlineItem(models.Model):