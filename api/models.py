from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Pin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    imageUrl = models.TextField()
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BoardPin(models.Model):
    boardFk = models.ForeignKey(Board, on_delete=models.CASCADE)
    pinFk = models.ForeignKey(Pin, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['boardFk', 'pinFk'], name='unique_board_pin')
        ]

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class PinTag(models.Model):
    pinFk = models.ForeignKey(Pin, on_delete=models.CASCADE)
    tagFk = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['pinFk', 'tagFk'], name='unique_pin_tag')
        ]
