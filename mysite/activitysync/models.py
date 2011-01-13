from django.db import models
from activitysync.managers import PublishedManager
import datetime

class Activity(models.Model):
    """Activity from social network (Twitter, Flickr, etc)."""
    SOURCE_CHOICES = (
        ('T', 'twitter'),
        ('DL', 'delicious'),
        ('FB', 'facebook'),
        ('HU', 'hulu'),
        ('RD', 'reddit'),
        ('GR', 'googlereader'),
    )
    
    title = models.CharField('title', max_length=200)
    link = models.URLField(max_length=500)
    source = models.CharField(max_length=2, choices=SOURCE_CHOICES)
    username = models.CharField(max_length=20, blank=True)
    author = models.CharField(max_length=20, blank=True)
    comments = models.TextField(blank=True)
    pub_date = models.DateTimeField('Date published')
    published = models.BooleanField(default=True)
    guid = models.CharField(max_length=255, unique=True, db_index=True)
    objects = PublishedManager()
    
    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        db_table = 'blog_activities'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
    
    def __unicode__(self):
        return u'%s' % self.title

    def get_activity_prefix(self):
        if self.source == 'DL':
            return u'Bookmarked '
        elif self.source == 'HU':
            return u'Watched '
        elif self.source == 'RD':
            return u'Liked '
        elif self.source == 'GR':
            return u'Shared '
        else:
            return u''
    
    def get_network_link(self):
        if self.source == 'T':
            return u"http://twitter.com/erunama"
        elif self.source == 'DL':
            return u"http://delicious.com/erunama"
        elif self.source == 'FB':
            return u"http://www.facebook.com/people/Dan-Carroll/401024"
        elif self.source == 'HU':
            return u"http://www.hulu.com/profiles/erunama/"
        elif self.source == 'RD':
            return u"http://www.reddit.com/user/erunama/"
        elif self.source == 'GR':
            return u"http://www.google.com/reader/shared/dancarroll"
            
