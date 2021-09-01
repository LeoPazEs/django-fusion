# Generated by Django 3.2.4 on 2021-06-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_feature_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pacote', models.CharField(max_length=100, verbose_name='Pacote')),
                ('preco', models.CharField(max_length=10, verbose_name='Preço')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-laptop-phone', 'Notebook'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico'), ('lni-package', 'Pacote'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Pacote',
            },
        ),
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Notebook'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico'), ('lni-package', 'Pacote'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Notebook'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico'), ('lni-package', 'Pacote'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone'),
        ),
    ]
