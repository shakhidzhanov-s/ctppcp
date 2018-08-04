from django.shortcuts import render
from django.http import Http404
from itertools import chain
from django.db.models import Q

from .models import MainImage, Institute, History, Contact, Event, Area, PrInvestigator, Scientist, Staff
from .models import Course, SummerSchool, PhDProgram
from .models import Page, Position, Research, Publication


def main(request):
    latest_news_list = Event.objects.order_by('-date')[:3]
    area_list = Area.objects.all()
    institute = Institute.objects.all().first()
    image_list = MainImage.objects.all()
    context = {'latest_news_list': latest_news_list, 'area_list':area_list, 'institute':institute, 'image_list':image_list}
    return render(request, 'en/main.html', context)


def prinvestigator_index(request):
    institute = Institute.objects.all().first()
    pi_list = PrInvestigator.objects.all()
    context = {'pi_list': pi_list, 'institute':institute}
    return render(request, 'en/pi-index.html', context)


def staff_index(request):
    institute = Institute.objects.all().first()
    staff_list = Staff.objects.all()
    context = {'staff_list': staff_list, 'institute':institute}
    return render(request, 'en/staff.html', context)


def people_index(request):
    institute = Institute.objects.all().first()
    pi_list = PrInvestigator.objects.all()
    staff_list = Staff.objects.all()
    for i in staff_list:
        pi_list = pi_list.filter(~Q(email=i.email))
    scientist_list = Scientist.objects.all()

    r_list = sorted(chain(pi_list, staff_list, scientist_list),key=lambda instance: instance.lastname)
    q = []
    for p in r_list:
        q.append(p.lastname[0])
    s_list = list(sorted(set(q)))

    context = {'r_list':r_list, 'institute':institute, 's_list':s_list}
    return render(request, 'en/people.html', context)


def course_index(request):
    institute = Institute.objects.all().first()
    course_list = Course.objects.order_by('-date')
    context = {'course_list':course_list,'institute':institute}
    return render(request, 'en/courses.html', context)


def school(request):
    institute = Institute.objects.all().first()
    school_list = SummerSchool.objects.order_by('-date')
    school = school_list.first()
    context = {'school':school,'school_list':school_list,'institute':institute}
    return render(request, 'en/school.html', context)


def schoolyear(request, y):
    institute = Institute.objects.all().first()
    school_list = SummerSchool.objects.order_by('-date')
    school = SummerSchool.objects.filter(date__year=y).first()
    context = {'school':school,'school_list':school_list,'institute':institute}
    return render(request, 'en/school.html', context)


def phd(request):
    institute = Institute.objects.all().first()
    phd = PhDProgram.objects.all().first()
    context = {'phd':phd,'institute':institute}
    return render(request, 'en/phd.html', context)


def news_index(request):
    news_list = Event.objects.order_by('-date')
    institute = Institute.objects.all().first()
    context = {'news_list':news_list, 'institute':institute}
    return render(request, 'en/news.html', context)


def pages_index(request, name):
    page = Page.objects.get(pagename=name)
    page_list = Page.objects.all()
    institute = Institute.objects.all().first()
    context = {'page':page,'page_list':page_list,'institute':institute}
    return render(request, 'en/pages.html', context)


def positions_index(request):
    position_list = Position.objects.all()
    institute = Institute.objects.all().first()
    context = {'position_list': position_list, 'institute':institute}
    return render(request, 'en/positions.html', context)



def research_index(request):
    area_list = Area.objects.all
    institute = Institute.objects.all().first()
    context = {'area_list': area_list, 'institute':institute}
    return render(request, 'en/research.html', context)


def detail(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "en/detail.html", context)


def members(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "en/members.html", context)


def profile(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "en/profile.html", context)


def mission(request):
    try:
        institute = Institute.objects.all().first()
        context = {'institute': institute}
    except Institute.DoesNotExist:
        raise Http404("Institute does not exist")
    return render(request, 'en/mission.html', context)


def history(request):
    try:
        institute = Institute.objects.all().first()
        history = History.objects.all().first()
        context = {'history': history,'institute':institute}
    except History.DoesNotExist:
        raise Http404("History does not exist")
    return render(request, 'en/history.html', context)


def contacts(request):
    try:
        institute = Institute.objects.all().first()
        contact_list = Contact.objects.all()
        context = {'contact_list':contact_list,'institute': institute}
    except Contact.DoesNotExist:
        raise Http404("Contacts do not exist")
    return render(request, 'en/contacts.html', context)


def publications(request):
    institute = Institute.objects.all().first()
    p_list = Publication.objects.order_by('date')
    years = p_list.dates('date', 'year').reverse()
    context = {'p_list':p_list,'institute':institute,'years':years}
    return render(request, 'en/publications.html', context)


def pipub(request, nc):
    try:
        institute = Institute.objects.all().first()
        person = PrInvestigator.objects.get(nick=nc)
        p_list = Publication.objects.filter(prInvestigator=person)
        years = p_list.dates('date', 'year').reverse()
        context = {'p_list':p_list,'institute':institute,'years':years,'person':person}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'en/pipub.html', context)
