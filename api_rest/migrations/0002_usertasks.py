# Generated by Django 5.1.4 on 2024-12-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('user_nickname', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
