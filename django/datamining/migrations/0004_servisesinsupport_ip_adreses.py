# Generated by Django 4.2.3 on 2023-07-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0003_rename_servises_in_support_servisesinsupport'),
    ]

    operations = [
        migrations.AddField(
            model_name='servisesinsupport',
            name='ip_adreses',
            field=models.TextField(default='', verbose_name='Айпи адреса серверов'),
        ),
    ]