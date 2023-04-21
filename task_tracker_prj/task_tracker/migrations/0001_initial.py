# Generated by Django 4.2 on 2023-04-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('on_hold', 'On Hold'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='in progress', max_length=255)),
                ('due_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
