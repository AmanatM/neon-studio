# Generated by Django 2.0.6 on 2018-07-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_content_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='team_member_first',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Team'),
        ),
    ]
