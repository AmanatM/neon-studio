# Generated by Django 2.0.6 on 2018-07-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180713_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='team',
            new_name='team_member_first',
        ),
        migrations.AlterField(
            model_name='team',
            name='member_bio',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto maxime non dolorem, deserunt, optio debitis fuga.', max_length=300),
        ),
    ]
