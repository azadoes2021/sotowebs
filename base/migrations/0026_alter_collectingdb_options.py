# Generated by Django 5.0.6 on 2025-06-17 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_collectingdb_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectingdb',
            options={'ordering': ['-created'], 'verbose_name': '상담신청DB', 'verbose_name_plural': '상담신청DB'},
        ),
    ]
