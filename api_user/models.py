from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = "user" # 테이블명을 "User"로 한다.
