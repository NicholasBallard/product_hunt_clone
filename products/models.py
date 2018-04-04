from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    pub_date = models.DateField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    # The "product hunter"
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        date_pretty = self.pub_date.strftime("%b %e %Y")
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]