from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField  # Import AutoSlugField for slug generation
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Cheese(TimeStampedModel):
    # Standard name field
    name = models.CharField("Name of Cheese", max_length=255)
    
    # Autopopulating slug field
    slug = AutoSlugField("Cheese Address", unique=True, always_update=True, populate_from="name")
    
    # Description field (TextField for long text)
    description = models.TextField("Description", blank=True)
    
    firmness = models.CharField(max_length=255, default='Unknown')
    country_of_origin = CountryField(
        "Country of Origin", blank=True)

    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
    # Other fields can be added here if needed
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)


    @property
    def average_rating(self):
        ratings = Rating.objects.filter(cheese=self)

        if not ratings.exists():
            return 0  # Return a default value when there are no ratings.

        total = 0
        count = 0

        for rating in ratings:
            total += rating.i_rating
            count += 1

        if count <= 0:
            return 0  # Return a default value if there's no count.

        return total // count

    def __str__(self):
        return f"Rating for Cheese: {self.cheese.name}, Rating: {self.i_rating}"

    

    def get_absolute_url(self):
        """Return absolute URL to the Cheese Detail page."""
        return reverse(
            'cheeses:detail', kwargs={"slug": self.slug}
        )
    
class Rating(models.Model):
    i_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    cheese = models.ForeignKey(
        Cheese,
        null=True,
        on_delete=models.SET_NULL,
        related_name='ratings'
    )
    
    def __str__(self):
        return f"{self.i_rating}"
    