# Generated by Django 4.0.6 on 2022-07-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contactbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbook',
            name='contacts',
            field=models.ManyToManyField(related_name='book', to='main.contact'),
        ),
    ]