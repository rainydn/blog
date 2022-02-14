from django.contrib import admin
from django.shortcuts import redirect
from bs4 import BeautifulSoup as BSoup
import requests

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "photo", "author", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    # list_editable = ('is_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'time_create')


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

# @admin.register(Headline)
# class HeadlineAdmin(admin.ModelAdmin):
#     list_display = ("id", "title")
#
#     def scrape(self, request):
#         session = requests.Session()
#         session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#         url = "https://hi-tech.news/"
#
#         content = session.get(url, verify=False).content
#         soup = BSoup(content, "html.parser")
#         News = soup.find_all(class_='post-body')
#         for artcile in News:
#             title = artcile.find('div', class_='post-content').find(class_='title').find("a").text
#             image = f"https://hi-tech.news{artcile.find('div', class_='post-media').find('img').get('src')}"
#             url = artcile.find('div', class_='post-content').find(class_='title').find("a").get("href")
#             date_text = artcile.find('div', class_='post-short-bottom').find('div', class_='post-detail').find("a").text
#             art_id = date_text[13]
#             content_text = artcile.find('div', class_='post-content').find(class_='the-excerpt').text.strip().replace(
#                 '\n',
#                 '')
#
#             new_headline = Headline()
#
#             new_headline.title = title
#             new_headline.date_text = date_text
#             new_headline.art_id = art_id
#             new_headline.url = url
#             new_headline.image = image
#             new_headline.content_text = content_text
#
#             new_headline.save()
#         return redirect("../")
#
#     def response_change(self, request, obj):
#         response = super().response_change(request, obj)
#         if obj.title:
#             self.scrape(obj)
#         return response
#
#     def response_add(self, request, obj):
#         response = super().response_add(request, obj)
#         if obj.title:
#             self.scrape(obj)
#         return response
#
# # admin.site.register(Headline, HeadlineAdmin)