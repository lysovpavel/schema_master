from elements.models.mixins import BaseModel
from django.db import models


class Arrow(BaseModel):
    block_from = models.ForeignKey('Block', on_delete=models.CASCADE, related_name='arrow_from',
                                   verbose_name='Откуда')
    block_to = models.ForeignKey('Block', on_delete=models.CASCADE, related_name='arrow_to', verbose_name='Куда')

    class Meta:
        verbose_name = 'Стрелка'
        verbose_name_plural = 'Стрелки'
