# Generated by Django 5.1.4 on 2025-01-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, default='satelite.jpg', upload_to='photos/'),
        ),
    ]
