# Generated by Django 3.2.8 on 2021-10-12 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='user_id',
            new_name='user',
        ),
    ]
