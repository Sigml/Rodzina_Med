# Generated by Django 4.2.1 on 2024-07-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email_2',
            field=models.CharField(default='Null', max_length=64),
        ),
    ]