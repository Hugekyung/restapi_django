import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField: 문자필드 표현
    pub_date = models.DateTimeField('date published') # DateTimeField: 날짜와 시간필드

    def __str__(self): # object에서 str을 가져올 떄
        return '%s %s' % (self.question_text, self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey: Choice가 하나의 Question에 관계됨을 말함
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 투표수 기본값 0

    def __str__(self):
        return self.choice_text