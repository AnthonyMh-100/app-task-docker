# Generated by Django 5.0.4 on 2024-05-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('backlog', 'Backlog'), ('doing', 'Doing'), ('completed', 'Completed')], default='backlog', max_length=20),
        ),
    ]
