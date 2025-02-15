# Generated by Django 4.2.16 on 2024-11-06 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("nationalyouth", "0004_newscategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="nationalyouth.newscategory",
            ),
        ),
    ]
