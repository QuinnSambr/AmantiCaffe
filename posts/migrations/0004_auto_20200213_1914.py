# Generated by Django 2.2.2 on 2020-02-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200211_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_category',
            field=models.CharField(choices=[('TEA/COFFEE', 'Tea/Coffee'), ('FRAPPE/CHILLERS', 'Frappe/Chillers'), ('SMOOTHIE', 'Smoothie'), ('PANCAKE', 'Pancakes'), ('EGGS/VEGTABLE EGG MEDLY', 'Eggs/Vegatable Egg Medely'), ('PANNIS', 'Pannis'), ('SUBS', 'Subs'), ('WRAPS', 'Wraps')], default='', max_length=100),
        ),
    ]
