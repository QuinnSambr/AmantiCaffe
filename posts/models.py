from django.db import models
from django.utils.timezone import now
from _datetime import timezone
  


ONLINE_CHOICE=[
    ('Y','Ready For Pickup'),
    ('N','Stil Being Made'),
]

MENU_CHOICES=[
    ('TEA/COFFEE','Tea/Coffee'),
    ('FRAPPE/CHILLERS','Frappe/Chillers'),
    ('SMOOTHIE','Smoothie'),
    ('PANCAKE','Pancakes'),
    ('EGGS/VEGTABLE EGG MEDLY','Eggs/Vegatable Egg Medely'),
    ('PANNIS','Pannis'),
    ('SUBS','Subs'),
    ('WRAPS','Wraps'),
    ('GLUTENF','Gluten-Free'),
]

INVEN_UNIT=[
    ('OZ','Oz'),
    ('KG','Kg'),
    ('EACH','Each'),
    ('CASE','Case'),
    ('BTL','Bottle'),
    ('TRAY','Tray'),

    
    ]

INVEN_CHOICES=[
    ('HERBS','Herbs'),
    ('FRUITS','Fruits'),
    ('VEGGIES','Vegetables'),
    ('POULTRY','Poultry'),
    ('MEAT','Meat'),
    ('CARBS','Carbs'),
    ('DAIRY','Dairy'),
]

DATE_INPUT_FORMATS = ['%Y-%m-%d %H:%M']


# Create your models here.
class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=100)
    item_description= models.CharField(max_length=500 , blank=True)
    item_price = models.DecimalField(max_digits=8,decimal_places=2)
    item_picture = models.ImageField( blank=True)
    item_category = models.CharField(max_length=100,default='', choices=MENU_CHOICES , blank=False)

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

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField(max_length=64)
    staff_address = models.CharField(max_length=50,default=" ")
    phone_number = models.CharField(max_length=12 , default=" ")

    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return self.staff_name


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    inventory_name= models.CharField(max_length=100)
    inventory_unit= models.CharField(max_length=100,default=" ", choices=INVEN_UNIT)
    inventory_quantity= models.CharField(max_length=100)
    inventory_item_cat=models.CharField(max_length=100,default='', choices=INVEN_CHOICES)

    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return '{} with Quantity - {}'.format(self.inventory_name, self.inventory_quantity)

class Customer(models.Model):
    customer_id =models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    customer_username=models.CharField(max_length=100)
    customer_password=models.CharField(max_length=100)
    customer_email=models.EmailField(max_length=100)

    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return self.customer_name

class Shedule(models.Model):
    shedule_id=models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staff,on_delete=models.CASCADE,default="")
    shedule_clockin =models.DateTimeField(null=True)
    shedule_clockout =models.DateTimeField(null=True)
    
    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return '{} {}'.format(self.staff_id.staff_name , self.staff_id.staff_id)

class OnlineCustomer(models.Model):
    online_recipt= models.AutoField(primary_key=True)
    customer_username=models.ForeignKey(Customer,on_delete=models.CASCADE,default="")
    item_id= models.ForeignKey(MenuItem,on_delete=models.CASCADE,default="")
    item_price=models.DecimalField(max_digits=8,decimal_places=2)
    online_status=models.CharField(max_length=50, choices=ONLINE_CHOICE,default="Stil Being Made")
    
    def __str__(self): #Used to Display Database Object Attribute in Admin Page
        return '{}, Online Order No: {}'.format(self.customer_username.customer_username , self.online_recipt) 