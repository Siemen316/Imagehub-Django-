# Generated by Django 2.2.2 on 2019-09-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_by',
            field=models.CharField(default='siemen', max_length=250),
        ),
    ]
