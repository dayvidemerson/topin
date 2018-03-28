from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

from apps.core.models import Timestamp, City

User = get_user_model()


class Point(models.Model):
    longitude = models.DecimalField(
        _('longitude'), max_digits=11, decimal_places=8)
    latitude = models.DecimalField(
        _('latitude'), max_digits=11, decimal_places=8)

    class Meta:
        abstract = True


class Marker(Timestamp, Point):
    TYPES = (
        ('bus_stop', _('Parada de ônibus')),
        ('ticket_store', _('Ponto de venda de passagens'))
    )
    name = models.CharField(_('título'), max_length=255)
    slug = models.SlugField(_('identificador'), unique=True)
    type = models.CharField(_('tipo'), max_length=50, choices=TYPES)
    description = models.TextField(_('descrição'), null=True, blank=True)
    city = models.ForeignKey(City, verbose_name=_(
        'cidade'), on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, verbose_name=_(
        'administrador'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('marcador')
        verbose_name_plural = _('marcadores')
        ordering = ['city']

    def __str__(self):
        return self.name


class Line(Timestamp):
    name = models.CharField(_('nome'), max_length=255)
    slug = models.SlugField(_('identificador'), unique=True)
    description = models.TextField(_('descrição'))

    city = models.ForeignKey(City, verbose_name=_(
        'cidade'), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_(
        'administrador'), on_delete=models.CASCADE)
    markers = models.ManyToManyField(
        Marker, verbose_name=_('marcadores'), blank=True)

    class Meta:
        verbose_name = _('linha')
        verbose_name_plural = _('linhas')

    def __str__(self):
        return self.name


class PointLine(Timestamp, Point):
    order = models.PositiveSmallIntegerField(_('ordem'))

    line = models.ForeignKey(Line, verbose_name=_(
        'linha'), on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = _('ponto')
        verbose_name_plural = _('pontos')
        ordering = ['line', 'order']

    def __str__(self):
        return '({}, {})'.format(self.latitude, self.longitude)


class Schedule(Timestamp):
    WEEKDAYS = (
        ('sunday', _('domingo')),
        ('monday', _('segunda')),
        ('tuesday', _('terça')),
        ('wednesday', _('quarta')),
        ('thursday', _('quinta')),
        ('friday', _('sexta')),
        ('saturday', _('sábado'))
    )
    weekdays = ArrayField(
        verbose_name=_('dias da semana'),
        base_field=models.CharField(max_length=9, choices=WEEKDAYS)
    )
    hour = models.TimeField(_('hora'))

    line = models.ForeignKey(Line, verbose_name=_(
        'linha'), on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = _('horário')
        verbose_name_plural = _('horários')
        ordering = ['line', 'hour']

    def __str__(self):
        return '{} - {}'.format(self.line.name, self.hour)


class Feedback(Timestamp):
    name = models.CharField(_('nome'), max_length=255)
    email = models.EmailField(_('e-mail'))
    contact = models.CharField(_('contato'), max_length=15)
    reason = models.CharField(_('motivo'), max_length=255)
    message = models.TextField(_('mensagem'))
    user = models.ForeignKey(User, verbose_name=_(
        'administrador'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('feedback')
        verbose_name_plural = _('feedbacks')
        ordering = ['-created_at']

    def __str__(self):
        return self.name
