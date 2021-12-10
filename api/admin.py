from django.contrib import admin
from api.models import Match, Sport, Selection, Market

admin.site.register(Match)
admin.site.register(Market)
admin.site.register(Sport)
admin.site.register(Selection)