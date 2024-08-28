from elements.models.mixins import BaseModel
from django.db import models


class Block(BaseModel):
    coordinate_x = models.FloatField('Координата X')
    coordinate_y = models.FloatField('Координата Y')
    height = models.FloatField('Высота', default=200)
    width = models.FloatField('Ширина', default=300)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'
