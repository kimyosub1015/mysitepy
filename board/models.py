from django.db import models

# Create your models here.
class Board(models.Model):
    # Varchar로 매핑
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4096)
    reg_date = models.DateTimeField(auto_now_add='2018-10-15 15:00:00')
    user_name = models.CharField(max_length=10)
    user_id = models.IntegerField()
    group_no = models.IntegerField(default=0)
    order_no = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return  'Board(%s,%s,%s, %s)' % (self.title, self.content, self.reg_date, self.user_name)