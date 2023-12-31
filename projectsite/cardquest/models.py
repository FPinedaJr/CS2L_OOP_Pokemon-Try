from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index= True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class PokemonCard(BaseModel):
    rarity_choices = [
        ('C', 'Common'),
        ('U', 'Uncommon'),
        ('R', 'Rare'),
        ('L', 'Legendary'),
    ]
    card_type_choices = [
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Grass', 'Grass'),
        ('Electric', 'Electric'),
        ('Psychic', 'Psychic'),
        ('Fighting', 'Fighting'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
        ('Dragon', 'Dragon'),
        ('Normal', 'Normal'),
        ('Ghost', 'Ghost'),
        ('Ice', 'Ice'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ground', 'Ground'),
        ('Poison', 'Poison'),
        ('Flying', 'Flying'),
    ]
    
    name = models.CharField(max_length=255, null=True, blank=True)
    rarity = models.CharField(max_length=1, choices=rarity_choices, default='C')
    hp = models.IntegerField(null=True, blank=True)
    card_type = models.CharField(max_length=255, choices=card_type_choices, default='none')
    attack = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    weakness = models.CharField(max_length=255, null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    evolution_stage = models.CharField(max_length=255, null=True, blank=True)
    abilities = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Collection(BaseModel):
    card = models.ForeignKey(PokemonCard, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    collection_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Collection {self.card.name} + {self.trainer.name}"