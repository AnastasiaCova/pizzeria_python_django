# Generated by Django 3.1.7 on 2021-04-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynews',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static/main'),
        ),
    ]
