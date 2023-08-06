from django.db import models
from auth_app.models import User
from common.models import ModelMixin, TimeStampMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone

# Create your models here.
class Post(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Blog - Posts')
        verbose_name_plural = _('Blog - Posts')

    def __str__(self):
        return self.title

class Like(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")

    class Meta:
        verbose_name = _('Blog - Like')
        verbose_name_plural = _('Blog - Like')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} likes {self.post.title}"