# Generated by Django 4.2.1 on 2024-07-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_friday_contact_monday_contact_thursday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='post_files/'),
        ),
    ]
