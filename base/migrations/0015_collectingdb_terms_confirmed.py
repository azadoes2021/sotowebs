# Generated by Django 5.0.6 on 2025-06-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_collectingdb_address001'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingdb',
            name='terms_confirmed',
            field=models.BooleanField(max_length=10, null=True, verbose_name='개인정보 수집 동의'),
        ),
    ]
