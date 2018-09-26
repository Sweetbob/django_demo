from django.contrib import admin
from testblog.models import Article

# the class down blew is for senior administration
class ArticleAdmin(admin.ModelAdmin):
    # what you want to display on the admin pages
    list_display = ('title', 'content', 'post_date')
    # which one for percolating
    list_filter = ('post_date', )

# Register your models here.


admin.site.register(Article, ArticleAdmin)
