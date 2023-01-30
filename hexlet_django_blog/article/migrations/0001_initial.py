# Generated by Django 4.1.5 on 2023-01-28 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('body', models.TextField(verbose_name='body')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
            ],
        ),
    ]