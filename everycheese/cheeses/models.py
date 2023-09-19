from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField  # Import AutoSlugField for slug generation

class Cheese(TimeStampedModel):
    # Standard name field
    name = models.CharField("Name of Cheese", max_length=255)
    
    # Autopopulating slug field
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    
    # Description field (TextField for long text)
    description = models.TextField("Description", blank=True)
    
    # Firmness choices
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    
    # Firmness field with choices and default value
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    
    # Other fields can be added here if needed
    def __str__(self):
        return self.name