# Generated by Django 5.0.7 on 2024-08-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfile', '0010_rename_poetry_poetry_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='android_apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_img', models.FileField(default=None, max_length=500, null=True, upload_to='')),
                ('app_name', models.CharField(max_length=200)),
                ('app_ver', models.CharField(max_length=200)),
                ('app_link', models.CharField(max_length=500)),
                ('app_source', models.CharField(max_length=200)),
                ('app_category', models.CharField(max_length=200)),
            ],
        ),
    ]
