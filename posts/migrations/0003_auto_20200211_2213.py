# Generated by Django 2.2.2 on 2020-02-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_menuitem_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
