# Generated by Django 4.1.7 on 2023-06-02 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_news', '0007_news_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='user_id',
        ),
    ]
