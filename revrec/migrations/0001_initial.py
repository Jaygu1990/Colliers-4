# Generated by Django 4.1 on 2023-12-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='revrecmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('deal', models.PositiveIntegerField()),
                ('due_date', models.DateField()),
                ('assign_status', models.CharField(blank=True, default='unassigned', max_length=256)),
                ('test_status', models.CharField(blank=True, default='untested', max_length=256)),
            ],
        ),
    ]
