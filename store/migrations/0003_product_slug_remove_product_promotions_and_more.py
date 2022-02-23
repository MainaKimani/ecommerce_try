# Generated by Django 4.0.2 on 2022-02-23 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_promotions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='promotions',
        ),
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.promotion'),
        ),
    ]