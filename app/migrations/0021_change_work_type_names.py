# Generated by Django 2.1.2 on 2018-12-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_insert_to_new_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalwork',
            name='file_type',
            field=models.CharField(choices=[('audio', 'Audio'), ('images', 'Image')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='file_type',
            field=models.CharField(choices=[('audio', 'Audio'), ('images', 'Image')], max_length=25, null=True),
        ),
    ]
