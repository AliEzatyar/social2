# Generated by Django 4.2.7 on 2024-02-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
