# Generated by Django 5.1.3 on 2024-11-25 04:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KakeiboPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('category', models.CharField(choices=[('給料', '給料'), ('お小遣い', 'お小遣い'), ('家賃', '家賃'), ('水道光熱費', '水道光熱費'), ('通信費', '通信費'), ('食費', '食費'), ('日用品費', '日用品費'), ('交際費', '交際費'), ('交通費', '交通費'), ('教育費', '教育費')], max_length=30, verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.IntegerField(verbose_name='銀行')),
                ('income', models.IntegerField(verbose_name='収入')),
                ('outcome', models.IntegerField(verbose_name='支出')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
