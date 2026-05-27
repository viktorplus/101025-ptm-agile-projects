from django.db import models


class Tag(models.Model):
    title = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']
