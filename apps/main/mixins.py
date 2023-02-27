from django.db import models


class MetaTagMixin(models.Model):
    name = None
    meta_tittle = models.CharField(verbose_name='Meta Tittle', max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name='Meta Description', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(verbose_name='Meta Keywords', max_length=255, null=True, blank=True)

    def get_meta_title(self):
        if self.meta_tittle:
            return self.meta_tittle
        return self.name

    class Meta:
        abstract = True
