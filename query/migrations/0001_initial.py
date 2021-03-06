# Generated by Django 4.0 on 2021-12-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=68)),
                ('registration_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('registration_date', models.DateTimeField(auto_now=True, null=True)),
                ('mentor', models.ForeignKey(db_column='mentor', on_delete=django.db.models.deletion.CASCADE, to='query.mentor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='E:\\BoschProject\\media')),
                ('query_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('replied_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('mentor', models.ForeignKey(db_column='mentor', on_delete=django.db.models.deletion.CASCADE, to='query.mentor')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='query.student')),
            ],
            options={
                'unique_together': {('user', 'mentor', 'question')},
            },
        ),
    ]
