from django.db import models

class InternetPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomerReview(models.Model):
    customer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    plan = models.ForeignKey(InternetPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer_name} - {self.rating}/5"
