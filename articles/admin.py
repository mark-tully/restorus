from django.contrib import admin
from articles.models import Tag, Topic, Article, Study, Review


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-title',)

admin.site.register(Tag, TagAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-title',)

admin.site.register(Topic, TopicAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-date',)

admin.site.register(Article, ArticleAdmin)


class StudyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-title',)

admin.site.register(Study, StudyAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-title',)

admin.site.register(Review, ReviewAdmin)
