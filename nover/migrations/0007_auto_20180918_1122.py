# Generated by Django 2.1 on 2018-09-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nover', '0006_auto_20180918_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PollName',
        ),
    ]
