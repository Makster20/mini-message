# Generated by Django 5.1.3 on 2024-12-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
