# Generated by Django 3.2 on 2023-02-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_img_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='%Y/%m/%d/', verbose_name='картинка'),
        ),
    ]
