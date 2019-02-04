# Generated by Django 2.1.5 on 2019-02-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainport', '0002_delete_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_image', models.ImageField(upload_to='proImg')),
                ('project_url', models.URLField()),
                ('project_url_name', models.CharField(max_length=50)),
            ],
        ),
    ]