# Generated by Django 3.2.22 on 2023-11-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_auto_20231107_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recinvoice',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recinvoice',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
