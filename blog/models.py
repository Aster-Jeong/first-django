from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
# class -> 객체를 정의
# Post -> 모델의 이름, 항상 클래스 이름의 첫 글자는 대문자로 써야한다.(특수문자, 공백 제외)
# models는 Post가 장고 모델임을 의미

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# def publish(self):는 무슨 뜻일까요? 이것이 바로 앞서 말했던 publish라는 메서드(method) 입니다.
# def는 이것이 함수/메서드라는 뜻이고, publish는 메서드의 이름입니다.

    def __str__(self):
        return self.title


# models.CharField - 글자 수가 제한된 텍스트를 정의할 때 사용합니다. 글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
# models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다. 블로그 콘텐츠를 담기 좋겠죠?
# models.DateTimeField - 날짜와 시간을 의미합니다.
# models.ForeignKey - 다른 모델에 대한 링크를 의미합니다.
