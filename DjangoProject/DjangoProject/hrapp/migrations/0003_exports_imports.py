# Generated by Django 5.1.7 on 2025-03-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exports',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('file_disk', models.CharField(max_length=255)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('exporter', models.CharField(max_length=255)),
                ('processed_rows', models.PositiveIntegerField()),
                ('total_rows', models.PositiveIntegerField()),
                ('successful_rows', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imports',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('file_name', models.CharField(max_length=255)),
                ('file_path', models.CharField(max_length=255)),
                ('importer', models.CharField(max_length=255)),
                ('processed_rows', models.PositiveIntegerField()),
                ('total_rows', models.PositiveIntegerField()),
                ('successful_rows', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'imports',
                'managed': False,
            },
        ),
    ]
