# Generated by Django 2.2.4 on 2020-07-31 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MariaBonita', '0008_auto_20200731_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(upload_to=models.CharField(max_length=150)),
        ),
    ]
