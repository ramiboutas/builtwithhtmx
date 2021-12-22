from django.contrib import admin

from .models import Comment, Project, Technology


class CommentInline(admin.TabularInline):
    model = Comment


# class LikeInline(admin.TabularInline):
#     model = Like


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "date_added"]
    inlines = [CommentInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
admin.site.register(Comment)
