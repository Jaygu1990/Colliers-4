# Generated by Django 4.1 on 2023-12-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_reviewvendor_vendor_code_vendorrequest_vendor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorrequest',
            name='status',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
