# Generated by Django 5.1.2 on 2024-12-23 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_quiztime_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquizdata',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.options'),
        ),
    ]