# Generated by Django 2.2.4 on 2020-07-16 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MariaBonita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='mariabonita')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MariaBonita.Categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
