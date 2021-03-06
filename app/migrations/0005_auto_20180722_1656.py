# Generated by Django 2.0.6 on 2018-07-22 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180722_1636'),
    ]

    operations = [
        migrations.RunSQL("""
UPDATE grupo g
SET (city_of_origin, subdivision_of_origin, country_of_origin) = (
  SELECT l.ciudad, l.subdivision, l.pais
  FROM lugar l
  WHERE l.lugar_id = g.lugar_id);
"""),

        migrations.RunSQL("""
UPDATE persona p
SET (city_of_origin, subdivision_of_origin, country_of_origin) = (
  SELECT l.ciudad, l.subdivision, l.pais
  FROM lugar l
  WHERE l.lugar_id = p.lugar_id);
"""),

        migrations.RunSQL("""
UPDATE persona p
SET (city_of_death, subdivision_of_death, country_of_death) = (
  SELECT l.ciudad, l.subdivision, l.pais
  FROM lugar l
  WHERE l.lugar_id = p.lugar_muer);
    """),

        migrations.RunSQL("""
UPDATE pista_son p
SET (city_of_origin, subdivision_of_origin, country_of_origin) = (
  SELECT l.ciudad, l.subdivision, l.pais
  FROM lugar l
  WHERE l.lugar_id = p.lugar_id);
    """),

        migrations.RemoveField(
            model_name='persona',
            name='lugar',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='lugar_muer',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='lugar',
        ),
        migrations.RemoveField(
            model_name='pistason',
            name='lugar',
        ),

        migrations.DeleteModel('lugar')
    ]
