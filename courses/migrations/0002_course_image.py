# Generated by Django 5.1.4 on 2024-12-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images/', verbose_name='Rasm'),
        ),
    ]