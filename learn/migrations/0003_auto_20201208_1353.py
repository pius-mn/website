# Generated by Django 3.1.4 on 2020-12-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
