# Generated by Django 4.1.5 on 2023-01-31 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
