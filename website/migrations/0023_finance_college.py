# Generated by Django 5.0 on 2024-06-09 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0022_remove_facilities_collegef_facilities_college_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="finance",
            name="college",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.academic",
            ),
        ),
    ]