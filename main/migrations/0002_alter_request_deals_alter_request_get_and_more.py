# Generated by Django 4.1.3 on 2022-11-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='deals',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Сделки'),
        ),
        migrations.AlterField(
            model_name='request',
            name='get',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Получаем'),
        ),
        migrations.AlterField(
            model_name='request',
            name='send',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отправляем'),
        ),
    ]
