# Generated by Django 5.0.6 on 2024-12-12 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('optiona', models.CharField(max_length=200)),
                ('optionb', models.CharField(max_length=200)),
                ('optionc', models.CharField(max_length=200)),
                ('optiond', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('Option A', 'A'), ('Option B', 'B'), ('Option C', 'C'), ('Option D', 'D')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='QuizSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.IntegerField(default=0)),
                ('incorrect', models.IntegerField(default=0)),
                ('quetions', models.ManyToManyField(to='quiz_app.questionset')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choosen_option', models.CharField(choices=[('Option A', 'A'), ('Option B', 'B'), ('Option C', 'C'), ('Option D', 'D')], max_length=10)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.questionset')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quizsession')),
            ],
        ),
    ]
