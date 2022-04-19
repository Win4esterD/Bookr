from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
from django.contrib.admin import ModelAdmin
 # Register your models here.

class BookAdmin(ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date', )
    search_fields = ('title', 'isbn')

class ReviewAdmin(ModelAdmin):
    fieldsets = (('Linkage', {'fields': ('creator', 'book')}), ('Review content', {'fields': ('content', 'rating')}))

class ContributorAdmin(ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names', )

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)



