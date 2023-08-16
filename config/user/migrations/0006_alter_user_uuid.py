# Generated by Django 4.2.4 on 2023-08-13 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='사용자 고유번호'),
        ),
    ]
