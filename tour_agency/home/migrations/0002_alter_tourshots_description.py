# Generated by Django 3.2.12 on 2022-02-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourshots',
            name='description',
            field=models.TextField(default='Not exists', verbose_name='Tavsif'),
        ),
    ]
