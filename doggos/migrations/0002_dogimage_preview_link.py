# Generated by Django 3.2.16 on 2022-10-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogimage',
            name='preview_link',
            field=models.CharField(default='none', max_length=128),
        ),
    ]