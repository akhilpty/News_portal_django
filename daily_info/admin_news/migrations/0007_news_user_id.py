# Generated by Django 4.1.7 on 2023-06-02 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_news', '0006_remove_news_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
