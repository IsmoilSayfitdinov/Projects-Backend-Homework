# Generated by Django 5.0.6 on 2024-05-23 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CategoryProduct',
                'verbose_name_plural': 'CategoryProducts',
            },
        ),
        migrations.CreateModel(
            name='ColorProducstModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ColorProduct',
                'verbose_name_plural': 'ColorProducts',
            },
        ),
        migrations.CreateModel(
            name='ManufactureProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ManufactureProduct',
                'verbose_name_plural': 'ManufactureProducts',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ProductTag',
                'verbose_name_plural': 'ProductTags',
            },
        ),
        migrations.CreateModel(
            name='ProducuctsChoisSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=129)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ProducuctsChoisSize',
                'verbose_name_plural': 'ProducuctsChoisSizes',
            },
        ),
        migrations.CreateModel(
            name='ProducstModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product')),
                ('title', models.CharField(max_length=128)),
                ('reyting', models.FloatField(default=0.0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dicount', models.FloatField(default=0.0)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('test', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='products', to='product.categoryproductsmodel')),
                ('color', models.ManyToManyField(related_name='products', to='product.colorproducstmodel')),
                ('manufacture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.manufactureproductsmodel')),
                ('tags', models.ManyToManyField(related_name='products', to='product.producttagmodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
