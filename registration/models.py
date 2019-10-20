from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.TextField(_('Nome'))
    user = models.ForeignKey(User, default=1)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modificado em'), auto_now=True)

    def __unicode__(self):
        return _("%s") % self.name


class Team(models.Model):
    name = models.TextField(_('Nome'), max_length=100)
    email = models.TextField(max_length=50)
    street = models.TextField(_('Rua'), blank=True, null=True)
    number = models.IntegerField(_('Número'), blank=True, null=True)
    city = models.TextField(_('Cidade'), default="")
    zip_code = models.TextField(_('CEP'), blank=True, null=True)
    state_or_province = models.TextField(_('Estado'), blank=True, null=True)
    country = models.TextField(_('País'), blank=True, null=True)
    telephone = models.TextField(_('Telefone'), blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modificado em'), auto_now=True)

    def __unicode__(self):
        return _("%s") % self.name


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(_('Foto'), upload_to='members', blank=True, null=True)
    birth_date = models.DateField(_('Data de Nascimento'), null=True, blank=True)
    team = models.ForeignKey(Team, related_name='members')

    def __unicode__(self):
        return _("%s") % self.name


class Robot(models.Model):
    name = models.TextField(_('Nome'))
    image = models.ImageField(_('Foto'), upload_to="robots", blank=True, null=True)
    team = models.ForeignKey(_('Equipe'), Team, null=False, related_name='robots')
    category = models.ForeignKey(_('Categoria'), Category, null=False, related_name='robots')
    user = models.ForeignKey(User, default=1)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modificado em'), auto_now=True)

    def __unicode__(self):
        return _("%s") % self.name


class Event(models.Model):
    name = models.TextField(_('Nome'))
    street = models.TextField(_('Rua'), blank=True, null=True)
    number = models.IntegerField(_('Número'), blank=True, null=True)
    city = models.TextField(_('Cidade'), default="")
    zip_code = models.TextField(_('CEP'), blank=True, null=True)
    state_or_province = models.TextField(_('Estado'), blank=True, null=True)
    country = models.TextField(_('País'), blank=True, null=True)
    date_start = models.DateField(_('Data de Início'), null=True, blank=True)
    date_end = models.DateField(_('Data de Término'), null=True, blank=True)
    logo = models.ImageField(upload_to='events', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='events')
    participants = models.ManyToManyField(Member, related_name='events')
    robots = models.ManyToManyField(Robot, related_name='events')
    user = models.ForeignKey(User, default=1)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modificado em'), auto_now=True)

    def __unicode__(self):
        return _("%s") % self.name
