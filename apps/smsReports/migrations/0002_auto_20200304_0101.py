# Generated by Django 3.0.3 on 2020-03-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsReports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='reports',
            field=models.TextField(blank=True, null=True),
        ),
    ]
