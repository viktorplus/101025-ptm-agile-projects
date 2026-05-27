from django.db import models


class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file_path = models.CharField(max_length=255)
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project_files'
        verbose_name = 'Project File'
        verbose_name_plural = 'Project Files'
        ordering = ['name']
