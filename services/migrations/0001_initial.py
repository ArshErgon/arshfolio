# Generated by Django 2.1.5 on 2019-01-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_completed', models.CharField(max_length=50)),
                ('years_of_experience', models.CharField(max_length=50)),
                ('total_client', models.CharField(max_length=50)),
                ('award_won', models.CharField(max_length=50)),
            ],
        ),
    ]