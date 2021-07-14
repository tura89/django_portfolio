# Generated by Django 3.2.5 on 2021-07-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='portfolio/images')),
                ('date', models.DateField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]