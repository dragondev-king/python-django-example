"""Simple API Modles"""

from __future__ import unicode_literals

from django.db import models

PRIORITY_LIST = [
    ('H', 'high'),
    ('N', 'normal'),
    ('L', 'low')
]

class Todo(models.Model):
    """ Todo Model """

    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_LIST, default='normal', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
