# Generated by Django 3.2.14 on 2022-07-27 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]