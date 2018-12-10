# Generated by Django 2.1.2 on 2018-12-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0023_work_collection_entity'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='historicalworktoworkrel',
            name='from_work',
        ),
        migrations.RemoveField(
            model_name='historicalworktoworkrel',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalworktoworkrel',
            name='to_work',
        ),
        migrations.RemoveField(
            model_name='worktoworkrel',
            name='from_work',
        ),
        migrations.RemoveField(
            model_name='worktoworkrel',
            name='to_work',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='file_path',
        ),
        migrations.RemoveField(
            model_name='historicalentity',
            name='file_path',
        ),
        migrations.RemoveField(
            model_name='historicalwork',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='work',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='work',
            name='self_relation',
        ),
        migrations.AddField(
            model_name='entity',
            name='image',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='images/upload_date=%Y%m%d'),
        ),
        migrations.AddField(
            model_name='historicalentity',
            name='image',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='historicalwork',
            name='path_to_file',
            field=models.TextField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='historicalworkcollection',
            name='image',
            field=models.TextField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='path_to_file',
            field=models.FileField(max_length=512, upload_to='audio/upload_date=%Y%m%d', null=True),
        ),
        migrations.AlterField(
            model_name='workcollection',
            name='image',
            field=models.ImageField(max_length=512, null=True, upload_to='images/upload_date=%Y%m%d'),
        ),
        migrations.DeleteModel(
            name='HistoricalWorkToWorkRel',
        ),
        migrations.DeleteModel(
            name='WorkToWorkRel',
        ),

        migrations.RunSQL("""
        DELETE FROM poet_work WHERE work_type <> 'Pista son'
        """),

            migrations.RunSQL("""
        UPDATE poet_work SET path_to_file = concat('audio/', path_to_file)
        """),

            migrations.RunSQL("""
        UPDATE poet_work_collection SET image = concat('images/', image)
        """),

    ]
