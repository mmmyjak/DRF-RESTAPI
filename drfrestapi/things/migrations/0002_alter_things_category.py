# Generated by Django 4.0.6 on 2022-07-29 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='category',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='things.category'),
        ),
    ]
