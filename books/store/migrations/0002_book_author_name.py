# Generated by Django 4.2.6 on 2023-10-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author_name",
            field=models.CharField(default="author", max_length=255),
            preserve_default=False,
        ),
    ]
