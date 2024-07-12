# Generated by Django 5.0 on 2024-06-09 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0019_remove_facilities_college_facilities_collegef"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facilities",
            name="collegeF",
        ),
        migrations.AddField(
            model_name="facilities",
            name="college",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.academic",
            ),
        ),
    ]