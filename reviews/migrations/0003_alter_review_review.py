# Generated by Django 5.0.4 on 2024-05-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=200),
        ),
    ]
