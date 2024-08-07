# Generated by Django 5.0 on 2024-06-08 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0010_alter_facilities_classrooms_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facilities",
            name="classrooms",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="laboratory",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="library",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="online_resources",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="playgrounds",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="Academic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("college", models.CharField(max_length=100)),
                ("programs", models.CharField(max_length=100, null=True)),
                ("enrollement_rate", models.CharField(max_length=100, null=True)),
                (
                    "facilities",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="academics",
                        to="website.facilities",
                    ),
                ),
            ],
            options={
                "verbose_name": "Academic",
                "verbose_name_plural": "Academic",
            },
        ),
    ]
