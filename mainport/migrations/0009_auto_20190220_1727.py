# Generated by Django 2.1.7 on 2019-02-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainport', '0008_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, upload_to='proImg'),
        ),
    ]
