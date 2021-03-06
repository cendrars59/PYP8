# Generated by Django 3.0.7 on 2020-06-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0004_auto_20200630_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='code',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='store',
            name='code',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=2048),
        ),
    ]
