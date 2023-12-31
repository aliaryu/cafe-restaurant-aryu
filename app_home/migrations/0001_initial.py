# Generated by Django 5.0 on 2023-12-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiveMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='فرستنده')),
                ('email', models.EmailField(max_length=255, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='پیام')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
    ]
