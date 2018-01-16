from django.db import models
from django.utils.translation import gettext as _


class Timestamp(models.Model):
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('atualizado em'), auto_now=True)

    class Meta:
        abstract = True


class State(Timestamp):
    name = models.CharField(_('nome'), max_length=255)
    abbr = models.CharField(_('sigla'), max_length=2)
    slug = models.SlugField(_('identificador'), max_length=255)

    class Meta:
        verbose_name = _('estado')
        verbose_name_plural = _('estados')
        ordering = ['name']

    def __str__(self):
        return self.name


class City(Timestamp):
    name = models.CharField(_('nome'), max_length=255)
    slug = models.SlugField(_('identificador'), max_length=255)

    state = models.ForeignKey(State, verbose_name=_('estado'), on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = _('cidade')
        verbose_name_plural = _('cidades')
        ordering = ['state', 'name']

    def __str__(self):
        return self.name
