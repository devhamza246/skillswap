# Generated by Django 5.0.1 on 2024-01-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='conversations',
            field=models.ManyToManyField(blank=True, to='messaging.conversation'),
        ),
    ]