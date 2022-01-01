# Generated by Django 4.0 on 2021-12-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='country2book', to='book_outlet.Country'),
        ),
    ]
