from django.db import models
from poet.models.choices import ReleaseState, PENDING
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.contrib.postgres.fields import JSONField
from poet.models.work import Work


PERSON = 'Persona'
GROUP = 'Grupo'
ORGANISATION = 'Organización'
FESTIVAL = 'Festival'
UNIVERSITY = 'Universidad'
COLLECTIVE = 'Colectivo'
RADIO_STATION = 'Estación radiofónica'
EDUCATION_AND_RESEARCH = 'Educación e investigación'
AUDIO_ARCHIVE = 'Archivo sonoro'
STREAMING_SERVICE = 'Servicios de streaming'
MUSEUM = 'Museo'
EDITORIAL = 'Editorial'
RECORD_LABEL = 'Sello discográfico'
CULTURAL_CENTER = 'Centro cultural'
BAND = 'Banda musical'


ENTITY_TYPE = (
    (PERSON, PERSON),
    (GROUP, GROUP),
    (ORGANISATION, ORGANISATION),
    (FESTIVAL, FESTIVAL),
    (UNIVERSITY, UNIVERSITY),
    (COLLECTIVE, COLLECTIVE),
    (RADIO_STATION, RADIO_STATION),
    (EDUCATION_AND_RESEARCH, EDUCATION_AND_RESEARCH),
    (AUDIO_ARCHIVE, AUDIO_ARCHIVE),
    (STREAMING_SERVICE, _('Servicios de streaming')),
    (MUSEUM, _('Museo')),
    (EDITORIAL, _('Editorial')),
    (RECORD_LABEL, _('Sello discográfico')),
    (CULTURAL_CENTER, _('Centro cultural')),
    (BAND, _('Banda musical')),
)


class EntityType(models.Model):
    entity_type = models.CharField(max_length=128, primary_key=True)

    class Meta:
        managed = True
        db_table = 'poet_entity_type'


class Entity(models.Model):

    full_name = models.TextField(blank=True, null=True)
    alt_name = models.TextField(blank=True, null=True)

    entity_type = models.ForeignKey(EntityType, on_delete=models.PROTECT, db_column='entity_type')

    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    file_path = models.FilePathField(blank=True, null=True)

    tags = ArrayField(models.CharField(max_length=200), blank=True, default=list, null=True)

    # Arbitrary additional information
    commentary = models.TextField(blank=True, null=True)
    additional_data = JSONField(blank=True, null=True)
    history = HistoricalRecords()

    work_relation = models.ManyToManyField(Work, blank=True, symmetrical=False, through='EntityToWorkRel')

    self_relation = models.ManyToManyField('self', blank=True, symmetrical=False, through='EntityToEntityRel')

    release_state = models.ForeignKey(ReleaseState, on_delete=models.PROTECT, default=PENDING, db_column='release_state')

    class Meta:
        managed = True
        db_table = 'poet_entity'


class EntityToEntityRel(models.Model):
    """

    Recursive many to many relationship with the Entity model.
    """

    from_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='ee_from_model')
    to_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='ee_to_model')
    contains = models.BooleanField(_('Consists of'), default=False)

    role = models.TextField(blank=True, null=True)

    # Arbitrary additional information
    commentary = models.TextField(blank=True, null=True)
    additional_data = JSONField(blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'poet_entity_to_entity_rel'
