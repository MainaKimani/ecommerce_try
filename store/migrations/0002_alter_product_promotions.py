# Generated by Django 4.0.2 on 2022-02-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, null=True, to='store.Promotion'),
        ),
    ]
