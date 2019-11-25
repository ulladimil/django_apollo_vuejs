from django.db import models


class Spec(models.Model):

    name = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Наименование')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Справочник специализаций'
        ordering = ('name',)
        default_permissions = ()

    def __str__(self):
        return f'{self.name}'


class CrashType(models.Model):

    name = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Наименование')

    specs = models.ManyToManyField(
        'Spec',
        related_name='crash_types',
        verbose_name='Специализация')

    class Meta:
        verbose_name = 'Тип аварии'
        verbose_name_plural = 'Справочник типов аварии'
        ordering = ('name',)
        default_permissions = ()

    def __str__(self):
        return f'{self.name}'
