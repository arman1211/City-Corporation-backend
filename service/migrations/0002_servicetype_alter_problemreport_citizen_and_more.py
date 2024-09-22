# Generated by Django 5.0.6 on 2024-08-20 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service/media/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='problemreport',
            name='citizen',
            field=models.ForeignKey(limit_choices_to={'role': 'citizen'}, on_delete=django.db.models.deletion.CASCADE, related_name='problem_report', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='requested', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('citizen', models.ForeignKey(limit_choices_to={'role': 'citizen'}, on_delete=django.db.models.deletion.CASCADE, related_name='problem_request', to=settings.AUTH_USER_MODEL)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicetype')),
            ],
        ),
    ]
