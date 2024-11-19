# Generated by Django 4.2.16 on 2024-11-19 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BojanglesSecurity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='privacysettings',
            name='DataEncryption',
        ),
        migrations.AddField(
            model_name='privacysettings',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='BojanglesSecurity.device'),
            preserve_default=False,
        ),
    ]
