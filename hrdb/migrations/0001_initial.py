# Generated by Django 4.1.2 on 2022-10-19 06:07

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
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='職種名')),
                ('summary', models.TextField(verbose_name='仕事内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
            options={
                'verbose_name': '職種名',
                'verbose_name_plural': '職種名',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='所属名')),
                ('url', models.URLField(verbose_name='ホームページ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
            options={
                'verbose_name': '組織名',
                'verbose_name_plural': '所属組織名',
            },
        ),
        migrations.CreateModel(
            name='Persondata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('gender', models.CharField(default='未回答', max_length=10, verbose_name='性別')),
                ('summary', models.TextField(verbose_name='現在の仕事内容')),
                ('collabat', models.TextField(verbose_name='協力できること')),
                ('specialat', models.TextField(verbose_name='専門領域')),
                ('interest', models.TextField(verbose_name='興味関心')),
                ('snsurl', models.CharField(max_length=100, null=True, verbose_name='連絡用SNS_URL')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hrdb.occupation', verbose_name='職種名')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hrdb.org', verbose_name='所属名')),
            ],
            options={
                'verbose_name': '人物情報',
                'verbose_name_plural': '人物情報',
                'db_table': 'person_data',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='肩書名')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
            options={
                'verbose_name': '肩書',
                'verbose_name_plural': '肩書',
            },
        ),
        migrations.CreateModel(
            name='Resulttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='実績の種別')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
            options={
                'verbose_name': '実績の種別',
                'verbose_name_plural': '実績の種別',
            },
        ),
        migrations.CreateModel(
            name='Resultdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='実績概要(200文字以内)')),
                ('event', models.TextField(verbose_name='実績詳細')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_author', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('persondata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_persondata', to='hrdb.persondata', verbose_name='人物情報')),
                ('resulttype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_resulttype', to='hrdb.resulttype', verbose_name='実績の種別')),
            ],
            options={
                'verbose_name': '実績情報',
                'verbose_name_plural': '実績情報',
                'db_table': 'result_data',
            },
        ),
        migrations.AddField(
            model_name='persondata',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='hrdb.title', verbose_name='肩書名'),
        ),
    ]
