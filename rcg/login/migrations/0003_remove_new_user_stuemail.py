# Generated by Django 4.0 on 2022-11-23 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_new_user_stuemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_user',
            name='stuemail',
        ),
    ]
