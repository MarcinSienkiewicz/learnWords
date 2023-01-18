# Generated by Django 4.1.5 on 2023-01-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100)),
                ('part', models.CharField(max_length=20)),
                ('eng_meaning', models.CharField(max_length=250)),
                ('polish', models.CharField(max_length=310)),
            ],
        ),
    ]
