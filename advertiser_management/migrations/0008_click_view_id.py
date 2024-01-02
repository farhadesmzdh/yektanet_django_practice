# Generated by Django 4.2.4 on 2024-01-02 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0007_views_delete_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='view_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.views'),
            preserve_default=False,
        ),
    ]
