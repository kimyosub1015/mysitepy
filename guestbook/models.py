from django.db import models

# Create your models here.
class Guestbook(models.Model):
    # Varchar로 매핑
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    data = models.CharField(max_length=500)
    agg_date = models.DateTimeField(auto_now_add='2018-10-15 15:00:00')

    def __str__(self):
        return  'Guestbook(%s,%s,%s, %s)' % (self.name, self.password, self.data, self.agg_date)