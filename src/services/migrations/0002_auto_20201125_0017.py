# Generated by Django 3.1.3 on 2020-11-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(default='tow', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
