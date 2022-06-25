from django.contrib import admin

from .models import Match, MapChoice, MapPoolChoice, MatchCheckIn, GameChoice, PlatformChoice

admin.site.register(GameChoice)
admin.site.register(Match)
admin.site.register(MapChoice)
admin.site.register(MapPoolChoice)
admin.site.register(MatchCheckIn)
admin.site.register(PlatformChoice)