# Generated by Django 3.0 on 2019-12-15 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0004_socialmediasettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialMediaSettings',
            new_name='ProfileSettings',
        ),
    ]