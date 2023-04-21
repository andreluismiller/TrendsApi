from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Profile(models.Model):
    """
    Base model, associate each page and post to exactaly one profile
    """    
    id = models.PositiveBigIntegerField(primary_key=True)
    username = models.CharField(max_length=30)


class Page(models.Model):
    """
    Model for input, via admin, page data and metrics
    """    
    pageId = models.PositiveBigIntegerField(primary_key=True)
    userId = models.OneToOneField(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    followers = models.IntegerField()
    totalPosts = models.IntegerField(null=True, blank=True)
    profileViews = models.IntegerField(null=True, blank=True)
    siteClicks = models.IntegerField(null=True)
    profileImpressions = models.IntegerField(null=True, blank=True)
    profileReach = models.IntegerField(null=True, blank=True)
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    

    # def save(self, *args, **kwargs):
    # # """
    # # Use the `pygments` library to create a highlighted HTMLrepresentation of the code snippet
    # # """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                           full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super().save(*args, **kwargs)



class Posts(models.Model):
    """
    Model to input, via admin, posts data and metrics
    """
    
    mediaId = models.PositiveBigIntegerField(primary_key=True)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.IntegerField()
    engajament = models.IntegerField(null=True)
    likes = models.IntegerField()
    plays = models.IntegerField(null=True)
    shares = models.IntegerField()
    saves = models.IntegerField()
    reach = models.IntegerField(null=True)
    impressions = models.IntegerField(null=True)
    link = models.URLField()
    PostType = models.TextChoices('PostType', 'VIDEO ALBUM IMAGE')
    type = models.CharField(choices=PostType.choices, max_length=10)
    date = models.DateTimeField(null=True) 
