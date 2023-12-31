# Generated by Django 3.2.22 on 2023-10-19 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='recinvoice',
            name='discount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='recinvoice',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='repeatevry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='recterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(max_length=100)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
