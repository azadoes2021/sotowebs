# Generated by Django 5.0.6 on 2025-06-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_collectingdb_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingdb',
            name='cate001',
            field=models.CharField(choices=[('신규', '신규'), ('완료', '완료'), ('진행중', '진행중'), ('보류', '보류')], max_length=10, null=True, verbose_name='구매/렌탈'),
        ),
        migrations.AlterField(
            model_name='collectingdb',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='성함'),
        ),
    ]
