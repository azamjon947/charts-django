# Generated by Django 4.0.4 on 2022-06-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_chart_delete_home_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='number',
        ),
        migrations.AddField(
            model_name='chart',
            name='text',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
