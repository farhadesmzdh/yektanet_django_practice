# Generated by Django 4.2.4 on 2024-01-01 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('imgUrl', models.URLField(max_length=256)),
                ('link', models.URLField(max_length=256)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.advertiser')),
            ],
        ),
    ]