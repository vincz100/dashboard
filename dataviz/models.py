from django.db import models
from django.utils import timezone

class Statistiques(models.Model):
    codgeo = models.CharField(max_length=5)
    libgeo = models.TextField(null=True)
    epci = models.CharField(max_length=9)
    libepci = models.TextField(null=True)
    dep = models.CharField(max_length=2)
    libdep = models.TextField(null=True)
    reg = models.CharField(max_length=2)
    libreg = models.TextField(null=True)
    d68_pop = models.FloatField()
    d75_pop = models.FloatField()
    d82_pop = models.FloatField()
    d90_pop = models.FloatField()
    d99_pop = models.FloatField()
    p10_pop = models.FloatField()
    p15_pop = models.FloatField()
    varpop_6875 = models.FloatField()
    varpop_7582 = models.FloatField()
    varpop_8290 = models.FloatField()
    varpop_9099 = models.FloatField()
    varpop_9910 = models.FloatField()
    varpop_1015 = models.FloatField()

    class Meta:
        verbose_name="statistiques communale"
        ordering = ["codgeo"]

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.libgeo


