from django.db import models

# Create your models here.
class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    from_who = models.ForeignKey('user.User', related_name='Chat_from', on_delete=models.CASCADE)
    to_who = models.ForeignKey('user.User', related_name='Chat_to', on_delete=models.CASCADE)
    upload_text = models.TextField(null=True, blank=True)
    upload_file = models.FileField(upload_to='chat/media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)