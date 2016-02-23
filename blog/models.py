import datetime
from django.db import models
# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    TYPE_CHOICES = (
        ('story', '故事'),
        ('article', '文章'),
        ('post', '随笔'),
    )
    name = models.CharField(max_length=100)
    content = models.TextField()
    blog_type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    tags = models.ManyToManyField(Tags)
    title_image = models.URLField(default=None, null=True, blank=True)
    reads = models.IntegerField(default=0, editable=False)
    likes = models.IntegerField(default=0, editable=False)
    comments = models.IntegerField(default=0, editable=False)
    creat_date = models.DateField()

    def published_days(self):
        now_days = (datetime.date.today() - self.creat_date).days
        if now_days >= 365:
            return str(now_days // 365) + ' Years Ago'
        elif now_days >= 30:
            return str(now_days // 30) + ' Months Ago'
        elif now_days > 0:
            return str(now_days) + ' Days Ago'
        else:
            return 'Today'


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-creat_date']
