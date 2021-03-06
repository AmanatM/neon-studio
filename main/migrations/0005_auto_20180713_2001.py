# Generated by Django 2.0.6 on 2018-07-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180713_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(default='Name Surname', max_length=50)),
                ('member_position', models.CharField(default='Co-Founder & CEO', max_length=50)),
                ('member_bio', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto maxime non dolorem, deserunt, optio debitis fuga.', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_1_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_2_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_3_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_4_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_5_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_6_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_7_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_8_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='feature_9_text',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?', max_length=200),
        ),
    ]
