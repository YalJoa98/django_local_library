# Generated by Django 2.2.4 on 2020-07-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MariaBonita', '0005_auto_20200731_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(storage='https://mariabonita.s3.us-east-2.amazonaws.com/media/mariabonita/', upload_to='mariabonita'),
        ),
    ]