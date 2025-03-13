from django.db import models
from ProductManagement.models import Lead
from UserManagement.models import CustomUser

class LeadNotes(models.Model):
    dealer              = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lead                = models.ForeignKey(Lead, blank=True, null=True, on_delete=models.CASCADE)
    notes               = models.TextField(blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, verbose_name = "Created At", null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now=True, verbose_name = "Last Modified At", null=True, blank=True)
