# Generated by Django 4.2.2 on 2023-06-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globaldata', '0005_contact_spam_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AlterField(
            model_name='contact',
            name='spam_count',
            field=models.IntegerField(default=1),
        ),
    ]
