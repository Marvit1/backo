# Generated by Django 5.0.1 on 2024-08-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_reclam_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reclam',
            options={'ordering': ('order', '-published'), 'verbose_name': 'Գովազդ', 'verbose_name_plural': 'Գովազդ'},
        ),
        migrations.AddField(
            model_name='reclam',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
