# Generated by Django 4.1.1 on 2022-11-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0009_alter_scriptsuggestion_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='scriptsuggestion',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='scriptsuggestion',
            name='logentry_ptr',
        ),
        migrations.AddField(
            model_name='scriptsuggestion',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
