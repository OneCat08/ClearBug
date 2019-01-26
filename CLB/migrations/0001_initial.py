# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-26 03:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, '待处理'), (2, '待审核'), (3, '已修复'), (4, '已拒绝')])),
                ('degree', models.IntegerField(choices=[(1, '致命'), (2, '严重'), (3, '较重'), (4, '一般'), (5, '建议')])),
                ('priority', models.IntegerField(choices=[(1, '马上解决'), (2, '急需解决'), (3, '高度重视'), (4, '正常处理'), (5, '低优先级')])),
                ('create_peo', models.IntegerField()),
                ('Dealing_people', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('close_time', models.DateTimeField()),
                ('description', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('all_bugs', models.IntegerField()),
                ('Project_peo', models.CommaSeparatedIntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
                ('Team_peo', models.CommaSeparatedIntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bug',
            name='Pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CLB.Project'),
        ),
    ]
