# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-13 06:27
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0036_remove_old_recipe_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RenameField(
            model_name='reciperevision',
            old_name='filter_expression',
            new_name='extra_filter_expression',
        ),
        migrations.AlterField(
            model_name='reciperevision',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_revisions', to='recipes.Action'),
        ),
        migrations.AddField(
            model_name='reciperevision',
            name='channels',
            field=models.ManyToManyField(to='recipes.Channel'),
        ),
        migrations.AddField(
            model_name='reciperevision',
            name='countries',
            field=models.ManyToManyField(to='recipes.Country'),
        ),
        migrations.AddField(
            model_name='reciperevision',
            name='locales',
            field=models.ManyToManyField(to='recipes.Locale'),
        ),
    ]