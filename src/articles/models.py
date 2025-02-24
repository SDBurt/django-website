from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import pre_save


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Article(models.Model):
    '''Model for articles'''
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    objects = PostManager()
    
    def __str__(self):
        '''return the title string for ORM and admin'''
        return self.title

    def snippet(self):
        '''return first characters of the body'''
        return self.content[:25] + '...'
    
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = sq.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_article_receiver, sender=Article)
