# Generated by Django 3.1.1 on 2020-10-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_auto_20200926_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='heroId',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
