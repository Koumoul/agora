# Generated by Django 2.0.1 on 2018-01-14 12:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBrick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=400, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('autor', models.CharField(max_length=40)),
            ],
        ),
    ]