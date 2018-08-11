from django.contrib import admin

from .models import MainImage, Image, Institute, History, Contact, Event, Area, PrInvestigator, Scientist, Staff, Fazly
from .models import Document, Course, PhDProgram
from .models import Page, Position, Research, Etics, Report, Senate, Publication, MainDocs, Attestation, Laboratories


admin.site.register(MainImage)
admin.site.register(Image)
admin.site.register(Document)
admin.site.register(Institute)
admin.site.register(History)
admin.site.register(Fazly)
admin.site.register(Contact)
admin.site.register(Etics)
admin.site.register(Senate)
admin.site.register(Event)
admin.site.register(Area)
admin.site.register(PrInvestigator)
admin.site.register(Scientist)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(PhDProgram)
admin.site.register(Page)
admin.site.register(Position)
admin.site.register(Research)
admin.site.register(Report)
admin.site.register(MainDocs)
admin.site.register(Attestation)
admin.site.register(Publication)
admin.site.register(Laboratories)
