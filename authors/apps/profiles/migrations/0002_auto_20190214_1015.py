# Generated by Django 2.1.4 on 2019-02-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]