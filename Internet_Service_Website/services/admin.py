from django.contrib import admin
from .models import InternetPlan, CustomerReview

@admin.register(InternetPlan)
class InternetPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'speed')
    search_fields = ('name', 'speed')
    list_filter = ('price', 'speed')

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'plan')
    search_fields = ('customer_name', 'plan__name')
    list_filter = ('rating',)
