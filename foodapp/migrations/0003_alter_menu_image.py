# Generated by Django 4.0.2 on 2022-02-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_alter_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='images'),
        ),
    ]