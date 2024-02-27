# Generated by Django 5.0.1 on 2024-02-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='conversations',
            field=models.ManyToManyField(blank=True, to='messaging.conversation'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='learning_interests',
            field=models.ManyToManyField(blank=True, default=list, related_name='learning_interests', to='accounts.skillandinterest'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(blank=True, default=list, related_name='skills', to='accounts.skillandinterest'),
        ),
    ]
