# Generated by Django 4.2.3 on 2023-08-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0004_servisesinsupport_ip_adreses'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableForForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название Предмета')),
                ('hero_name', models.CharField(max_length=100, verbose_name='Имя Героя')),
            ],
        ),
    ]
