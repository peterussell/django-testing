from django.contrib import admin
from polls.models import Choice, Poll

# Customize objects before registering
class ChoiceInline( admin.TabularInline ):
	model = Choice
	extra = 3

class PollAdmin( admin.ModelAdmin ):
	fieldsets = [
		( None,								{ 'fields': ['question'] } ),
		( 'Date Information',	{ 'fields': ['pub_date'], 'classes': ['collapse'] } ),
	]
	inlines = [ChoiceInline]
	list_display = ( 'question', 'pub_date', 'was_published_recently' )	# Modifies Poll display on change list page
	list_filter = ['pub_date'] # Adds a 'filter' sidebar
	search_fields = ['question'] # Adds a search box, will search 'question' fields

# Register objects
admin.site.register( Poll, PollAdmin )
