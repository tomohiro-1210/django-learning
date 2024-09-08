# Generated by Django 5.1.1 on 2024-09-08 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリー名')),
                ('url_code', models.CharField(max_length=50, null=True, unique=True, verbose_name='URLコード')),
                ('sort', models.IntegerField(default=0, verbose_name='ソート')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, null=True, verbose_name='名無しさん')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('message', models.TextField(null=True, verbose_name='本文')),
                ('status', models.IntegerField(choices=[(0, '公開'), (1, '非公開'), (2, '承認待ち')], default=0, verbose_name='トピックのステータス')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='thread.category', verbose_name='カテゴリー')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('no', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=30, null=True, verbose_name='名無しさん')),
                ('message', models.TextField(verbose_name='投稿内容')),
                ('status', models.IntegerField(choices=[(0, '公開'), (1, '非公開')], default=0, verbose_name='コメントのステータス')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thread.topic')),
            ],
        ),
    ]
