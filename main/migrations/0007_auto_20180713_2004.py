# Generated by Django 2.0.6 on 2018-07-13 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_content_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team'),
        ),
    ]
