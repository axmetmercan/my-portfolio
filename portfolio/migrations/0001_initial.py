# Generated by Django 3.2.8 on 2021-10-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myportfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=150, verbose_name='Surname')),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(max_length=1000, verbose_name='About Me')),
                ('study', models.TextField(max_length=1000, verbose_name='Study')),
                ('work_experiences', models.TextField(max_length=1000, verbose_name='Work Experiences')),
                ('hobbies', models.TextField(max_length=1000, verbose_name='Hobbies')),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.myportfolio', verbose_name='Programmer')),
            ],
        ),
    ]