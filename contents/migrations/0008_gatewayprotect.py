# Generated by Django 4.1.1 on 2022-11-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatewayProtect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_protected', models.BooleanField(default=True)),
            ],
        ),
    ]
