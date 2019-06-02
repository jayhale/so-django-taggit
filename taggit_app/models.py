import uuid

from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    pass


class Product(ModelBase):
    tags = TaggableManager(through=TaggedItem)
