# Generated by Django 4.2.7 on 2023-11-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0002_task_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
