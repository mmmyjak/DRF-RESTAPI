# Generated by Django 4.0.6 on 2022-07-29 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0002_alter_things_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='things',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='things', to=settings.AUTH_USER_MODEL),
        ),
    ]