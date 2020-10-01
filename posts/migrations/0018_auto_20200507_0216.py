# Generated by Django 2.2.6 on 2020-05-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_staff_staff_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='staff_no',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_number',
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_email',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]