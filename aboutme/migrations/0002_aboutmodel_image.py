# Generated by Django 2.1.5 on 2019-01-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='upImg'),
        ),
    ]