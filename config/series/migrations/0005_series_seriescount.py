# Generated by Django 4.2.4 on 2023-08-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_alter_series_writername'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='seriesCount',
            field=models.IntegerField(default=0),
        ),
    ]