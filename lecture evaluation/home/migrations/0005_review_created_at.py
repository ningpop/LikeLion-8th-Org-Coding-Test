# Generated by Django 3.0.3 on 2020-02-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
