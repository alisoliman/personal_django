from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from blog.models import BlogPage


class HomePage(Page):
    body = RichTextField(blank=True)

    def get_context(self, request):
        # Filter by tag

        blogpages = BlogPage.objects.live().order_by('-first_published_at')

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


@register_setting
class ProfileSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    linkedin = models.URLField(
        help_text='Your Linkedin page URL')
    github = models.URLField(
        help_text='Your Github page URL')
    instagram = models.URLField(
        help_text='Your Instagram page URL')
    twitter = models.URLField(
        help_text='Your Twitter page URL')
    email = models.EmailField()
