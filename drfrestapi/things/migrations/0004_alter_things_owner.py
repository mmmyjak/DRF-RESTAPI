# Generated by Django 4.0.6 on 2022-07-29 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0003_things_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='things', to=settings.AUTH_USER_MODEL),
        ),
    ]
