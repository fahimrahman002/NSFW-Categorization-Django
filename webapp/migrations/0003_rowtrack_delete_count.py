# Generated by Django 3.2.15 on 2022-10-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20221005_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='rowtrack',
            name='delete_count',
            field=models.IntegerField(default=0),
        ),
    ]