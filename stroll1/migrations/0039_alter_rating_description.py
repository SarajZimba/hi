# Generated by Django 4.0.6 on 2023-08-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroll1', '0038_alter_rating_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
