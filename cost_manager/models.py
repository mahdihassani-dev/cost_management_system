from django.db import models


class Budget(models.Model):
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Total Budget: {self.total_budget}"


PURCHASE_STATUS = (
    (1, "خریداری شده"),
    (2, "محمد"),
    (3, "مهدی"),
    (4, "امیرحسین"),
    (5, "امیرمحمد"),
)

class PurchaseItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    purchase_link = models.URLField(null=True, blank=True)
    purchase_date = models.DateField()
    status = models.IntegerField(choices=PURCHASE_STATUS, default=1)

    def __str__(self):
        return self.name
