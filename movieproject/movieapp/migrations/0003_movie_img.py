# Generated by Django 3.2.12 on 2022-03-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_place_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hfhjfj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
