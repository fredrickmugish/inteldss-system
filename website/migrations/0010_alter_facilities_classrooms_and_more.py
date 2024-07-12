# Generated by Django 5.0 on 2024-06-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0009_facilities"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facilities",
            name="classrooms",
            field=models.CharField(max_length=100, null="true"),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="laboratory",
            field=models.CharField(max_length=100, null="true"),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="library",
            field=models.CharField(max_length=100, null="true"),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="online_resources",
            field=models.CharField(max_length=100, null="true"),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="playgrounds",
            field=models.CharField(max_length=100, null="true"),
        ),
    ]
