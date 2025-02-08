from django.db import models
from django.contrib.auth.models import User
    
class SupportRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    issue_type = models.CharField(
        max_length=50,
        choices=[
            ('general', 'General Inquiry'),
            ('technical', 'Technical Issue'),
            ('billing', 'Billing Issue')
        ],
        default='general'
    )
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Support request from {self.name}"   