# Generated by Django 5.0.6 on 2025-06-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_collectingdb_options_collectingdb_promoperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingdb',
            name='address001',
            field=models.CharField(choices=[('서울특별시', '서울특별시'), ('완료', '완료'), ('진행중', '진행중'), ('보류', '보류')], default='', max_length=10, verbose_name='주소1'),
        ),
        migrations.AddField(
            model_name='collectingdb',
            name='address002',
            field=models.CharField(max_length=50, null=True, verbose_name='주소2'),
        ),
    ]
