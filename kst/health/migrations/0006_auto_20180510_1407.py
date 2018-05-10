# Generated by Django 2.0.5 on 2018-05-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20180510_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='image',
            field=models.CharField(default='health/images/a.png', max_length=100, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(default='health/images/jigou-img-01.png', max_length=50, verbose_name='图片Url'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='image',
            field=models.CharField(default='health/images/jigou-img-03.png', max_length=50, verbose_name='图片Url'),
        ),
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.CharField(default='health/images/a.png', max_length=100, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='provide',
            name='provide_image',
            field=models.CharField(default='health/images/icon-01.png', max_length=50, verbose_name='图片Url'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.CharField(default='health/images/img-20.png', max_length=50, verbose_name='图片Url'),
        ),
    ]