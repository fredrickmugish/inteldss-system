# Generated by Django 5.0 on 2024-06-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0028_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(max_length=255, upload_to="documents/"),
        ),
    ]
