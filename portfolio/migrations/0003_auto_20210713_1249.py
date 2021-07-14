# Generated by Django 3.2.5 on 2021-07-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210713_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to='portfolio/images'),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
