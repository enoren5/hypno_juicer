# Generated by Django 4.1.1 on 2022-12-18 08:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_scriptsuggestion_geeks_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='geeks_field',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300000),
        ),
    ]