# Generated by Django 5.0 on 2024-06-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0014_social"),
    ]

    operations = [
        migrations.AddField(
            model_name="facilities",
            name="college",
            field=models.CharField(default="Default College", max_length=100),
        ),
    ]