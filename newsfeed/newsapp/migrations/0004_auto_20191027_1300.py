# Generated by Django 2.2.3 on 2019-10-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_admin_availablecat'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('selectedfields', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='name',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='selectedfields',
        ),
    ]
