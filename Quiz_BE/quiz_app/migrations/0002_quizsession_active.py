# Generated by Django 5.0.6 on 2024-12-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]