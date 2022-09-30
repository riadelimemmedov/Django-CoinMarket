# Generated by Django 3.1 on 2022-09-30 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('image', models.URLField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, default=0)),
                ('rank', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
            },
        ),
    ]
