# Generated by Django 3.1.3 on 2020-11-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_auto_20201129_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='is_audited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='call',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
