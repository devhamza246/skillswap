# Generated by Django 5.0.1 on 2024-03-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]