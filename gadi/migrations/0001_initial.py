# Generated by Django 5.1 on 2024-11-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(default=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(default=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='media/products/')),
                ('category', models.CharField(choices=[('unisex', 'Unisex'), ('boys', 'Boys'), ('ladies', 'Ladies')], default='unisex', max_length=20)),
                ('colors', models.ManyToManyField(blank=True, to='gadi.color')),
                ('sizes', models.ManyToManyField(blank=True, to='gadi.size')),
            ],
        ),
    ]
