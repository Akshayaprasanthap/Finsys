# Generated by Django 3.2.22 on 2023-11-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0036_auto_20231113_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bill',
            name='refference',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='profile_name',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
