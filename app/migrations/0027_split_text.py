# Generated by Django 2.1.2 on 2018-12-28 22:57

from django.db import migrations, models


def split_text_and_commentaries(apps, schema_editor):
    works = apps.get_model('app', 'Work')
    for work in works.objects.all():
            split_text = work.commentary.split('\r\n\r\nTexto:\r\n\r')
            work.commentary = split_text[0]
            if len(split_text) == 2:
                work.poetry_text = split_text[1]
            work.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_rename_collections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='historicalentity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='historicalentity',
            name='tags',
        ),
        migrations.AddField(
            model_name='historicalwork',
            name='poetry_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='poetry_text',
            field=models.TextField(blank=True, null=True),
        ),

        migrations.RunPython(split_text_and_commentaries)
    ]