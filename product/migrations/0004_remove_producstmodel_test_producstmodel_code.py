# Generated by Django 5.0.6 on 2024-05-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_name_producstmodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producstmodel',
            name='test',
        ),
        migrations.AddField(
            model_name='producstmodel',
            name='code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
