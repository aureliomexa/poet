# Generated by Django 2.0.6 on 2018-07-22 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0005_auto_20180722_1656'),
    ]

    operations = [
        migrations.RunSQL("CREATE TEXT SEARCH CONFIGURATION es ( COPY = spanish );"),
        migrations.RunSQL("""ALTER TEXT SEARCH CONFIGURATION es ALTER MAPPING
FOR hword, hword_part, word WITH unaccent, spanish_stem
        """),
        migrations.RunSQL("SET default_text_search_config = 'es'")
    ]
