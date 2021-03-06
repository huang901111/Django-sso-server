# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-12 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldap_url', models.CharField(max_length=50)),
                ('organizations', models.CharField(max_length=50)),
                ('ldap_admin', models.CharField(max_length=50)),
                ('ldap_pass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='rsakeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.TextField()),
                ('public_key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='start_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': '\u7cfb\u7edf\u521d\u59cb\u5316\u8868',
            },
        ),
    ]
