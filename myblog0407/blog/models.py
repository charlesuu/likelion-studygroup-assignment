from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        index = self.content.find('결론')
        if index != -1:
            return self.content[index:]
        else:
            return self.content[:100]


