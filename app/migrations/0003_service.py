# Generated by Django 4.0.3 on 2022-04-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_gallary_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
