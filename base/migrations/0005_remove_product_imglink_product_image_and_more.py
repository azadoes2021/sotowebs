# Generated by Django 5.0.6 on 2024-05-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_imglink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imglink',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/defaultimg.jpg', null=True, upload_to='static/images', verbose_name='이미지업로드'),
        ),
        migrations.AlterField(
            model_name='product',
            name='plink',
            field=models.CharField(max_length=100, verbose_name='링크주소[제품코드[]'),
        ),
    ]