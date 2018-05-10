# Generated by Django 2.0.1 on 2018-05-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_article_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='images/jigou-img-03.png', max_length=30, verbose_name='图片Url')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('keywords', models.CharField(max_length=200, verbose_name='关键词')),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateField(verbose_name='发布日期')),
            ],
        ),
    ]