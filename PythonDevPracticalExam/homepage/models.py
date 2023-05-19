from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=50)
    # pointer to ID of next car in ordered list
    next_id_pointer = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True
    )
    
    def __str__(self):
        return '{}, {}'.format(
            self.id,
            self.car_order
        )


# function to update next_id_pointer when next car is deleted
@receiver(pre_delete, sender=Car)
def update_next_on_delete(sender, instance, **kwargs):
    sender.objects.filter(next_id_pointer=instance).update(next_id_pointer=instance.next_id_pointer)
