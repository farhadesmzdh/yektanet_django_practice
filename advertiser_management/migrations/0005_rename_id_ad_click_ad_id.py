# Generated by Django 4.2.4 on 2024-01-01 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0004_remove_ad_clicks_remove_ad_views_view_click'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='id_ad',
            new_name='ad_id',
        ),
    ]
