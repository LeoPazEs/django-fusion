# Generated by Django 3.2.4 on 2021-06-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210618_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço'),
        ),
    ]