# Generated by Django 2.0.1 on 2018-01-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='user_brick',
        ),
        migrations.AddField(
            model_name='sport',
            name='id',
            field=models.AutoField(auto_created=True, default=-1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
