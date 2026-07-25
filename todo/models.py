from django.db import models

class Task(models.Model):

    CATEGORY_CHOICES = [
        ('Work', '💼 Work'),
        ('Learning', '📚 Learning'),
        ('Health', '💪 Health'),
        ('Personal', '📝 Personal'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Personal'
    )

    time = models.TimeField()

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def category_icon(self):
        display = self.get_category_display()
        return display.split(' ', 1)[0]

    def __str__(self):
        return self.title