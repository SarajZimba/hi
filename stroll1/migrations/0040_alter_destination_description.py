# Generated by Django 4.0.6 on 2023-08-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroll1', '0039_alter_rating_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
