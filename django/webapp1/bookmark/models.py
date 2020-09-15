from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model): # ORM(Object Relationship Management) 사용
    title = models.CharField("TITLE", max_length=100, blank=True) # blank = 공백 허용 여부
    url = models.URLField("URL", unique=True) # unique - 중복허용 여부

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # 외래키 안에서 어떻게 동작하는가(User테이블을 참조한다, 부모가 삭제가 될 때 자식테이블의 행도 삭제하라)
    # ORM기술을 사용하면 별도로 join할 필요가 없다.

# Create table Bookmark(
#       title varchar(100) NULL,
#       url varchar UNIQUE
#       ); 한거랑 같음

# Primary key 를 설정하지 않으면
# id integer AUTO_INCREMENT
#               PRIMARY KEY  - 자동으로 삽입되어 총 COLUMN 은 선언된 컬럼 + PRIMARY KEY 가 설정되어있는 COLUMN 나옴

    def __str__(self):
        return self.title