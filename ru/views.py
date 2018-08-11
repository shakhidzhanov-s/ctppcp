from django.shortcuts import render
from django.http import Http404
from itertools import chain
from django.db.models import Q

from .models import MainImage, Institute, History, Contact, Event, Area, PrInvestigator, Scientist, Staff, Fazly
from .models import Course, PhDProgram
from .models import Page, Position, Research, Etics, Report, Senate, Publication, Attestation, MainDocs, Laboratories


def main(request):
    latest_news_list = Event.objects.order_by('-date')[:2]
    area_list = Area.objects.all()
    institute = Institute.objects.all().first()
    image_list = MainImage.objects.all()
    context = {'latest_news_list': latest_news_list, 'area_list':area_list, 'institute':institute, 'image_list':image_list}
    return render(request, 'ru/main.html', context)


def news_index(request, pagenum):
    news_num = Event.objects.count()
    news_per_page = 10
    page_max = (news_num - (news_num % news_per_page))/news_per_page
    if (pagenum > page_max + 1) or pagenum <= 0:
        news_list = []
    elif (pagenum == page_max + 1):
        news_list = Event.objects.order_by('-date')[(pagenum-1)*news_per_page:]
    else:
        news_list = Event.objects.order_by('-date')[(pagenum-1)*news_per_page:(pagenum)*news_per_page]
    institute = Institute.objects.all().first()
    page_list_f = range(pagenum-2,pagenum+3)
    page_list = [x for x in page_list_f if x>0 and x<=(page_max+1)]
    if pagenum >= 4:
        page_list.insert(0, '&#171;')
    if pagenum <= page_max-2:
        page_list.append('&#187;')
    context = {'news_list':news_list, 'institute':institute, 'page_list':page_list, 'page_num':pagenum, 'page_max':int(page_max+1)}
    return render(request, 'ru/news.html', context)


def positions_index(request):
    position_list = Position.objects.all()
    institute = Institute.objects.all().first()
    context = {'position_list': position_list, 'institute':institute}
    return render(request, 'ru/positions.html', context)


def prinvestigator_index_old(request):
    institute = Institute.objects.all().first()
    pi_list = PrInvestigator.objects.all()
    context = {'pi_list': pi_list, 'institute':institute}
    return render(request, 'ru/pi-index.html', context)


def prinvestigator_index(request):
    institute = Institute.objects.all().first()
    lab = Laboratories.objects.all().first()
    context = {'lab': lab, 'institute':institute}
    return render(request, 'ru/pi-index.html', context)


def staff_index(request):
    institute = Institute.objects.all().first()
    staff_list = Staff.objects.all()
    context = {'staff_list': staff_list, 'institute':institute}
    return render(request, 'ru/staff.html', context)


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
    return render(request, 'ru/people.html', context)


def course_index(request):
    institute = Institute.objects.all().first()
    course_list = Course.objects.order_by('-date')
    context = {'course_list':course_list,'institute':institute}
    return render(request, 'ru/courses.html', context)


def phd(request):
    institute = Institute.objects.all().first()
    phd = PhDProgram.objects.all().first()
    context = {'phd':phd,'institute':institute}
    return render(request, 'ru/phd.html', context)


def pages_index(request, name):
    page = Page.objects.get(pagename=name)
    page_list = Page.objects.all()
    institute = Institute.objects.all().first()
    context = {'page':page,'page_list':page_list,'institute':institute}
    return render(request, 'ru/pages.html', context)


def research_index(request):
    area_list = Area.objects.all
    institute = Institute.objects.all().first()
    context = {'area_list': area_list, 'institute':institute}
    return render(request, 'ru/research.html', context)


def detail(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "ru/detail.html", context)


def members(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "ru/members.html", context)


def profile(request, nc):
    institute = Institute.objects.all().first()
    try:
        person = PrInvestigator.objects.get(nick=nc)
        context = {'person' : person, 'institute':institute}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, "ru/profile.html", context)


def mission(request):
    try:
        institute = Institute.objects.all().first()
        context = {'institute': institute}
    except Institute.DoesNotExist:
        raise Http404("Institute does not exist")
    return render(request, 'ru/mission.html', context)


def history(request):
    try:
        institute = Institute.objects.all().first()
        history = History.objects.all().first()
        context = {'history': history,'institute':institute}
    except History.DoesNotExist:
        raise Http404("History does not exist")
    return render(request, 'ru/history.html', context)


def fazly(request):
    try:
        institute = Institute.objects.all().first()
        fazly = Fazly.objects.all().first()
        context = {'fazly': fazly,'institute':institute}
    except Fazly.DoesNotExist:
        raise Http404("Fazly does not exist")
    return render(request, 'ru/fazly.html', context)


def contacts(request):
    try:
        institute = Institute.objects.all().first()
        contact_list = Contact.objects.all()
        context = {'contact_list':contact_list,'institute': institute}
    except Contact.DoesNotExist:
        raise Http404("Contacts do not exist")
    return render(request, 'ru/contacts.html', context)


def etics(request):
    try:
        institute = Institute.objects.all().first()
        etics = Etics.objects.all().first()
        context = {'etics': etics,'institute':institute}
    except Etics.DoesNotExist:
        raise Http404("Etics does not exist")
    return render(request, 'ru/etics.html', context)


def senate(request):
    try:
        institute = Institute.objects.all().first()
        senate = Senate.objects.all().first()
        context = {'senate': senate,'institute':institute}
    except Senate.DoesNotExist:
        raise Http404("Senate does not exist")
    return render(request, 'ru/senate.html', context)


def reports(request):
    institute = Institute.objects.all().first()
    r_list = Report.objects.order_by('date')
    years = r_list.dates('date', 'year').reverse()
    context = {'r_list':r_list,'institute':institute,'years':years}
    return render(request, 'ru/reports.html', context)


def attestation(request):
    institute = Institute.objects.all().first()
    r_list = Attestation.objects.order_by('date')
    years = r_list.dates('date', 'year').reverse()
    context = {'r_list':r_list,'institute':institute,'years':years}
    return render(request, 'ru/attestation.html', context)


def maindocs(request):
    institute = Institute.objects.all().first()
    r_list = MainDocs.objects.order_by('title')
    context = {'r_list':r_list,'institute':institute}
    return render(request, 'ru/maindocs.html', context)


def publications(request):
    institute = Institute.objects.all().first()
    p_list = Publication.objects.order_by('date')
    years = p_list.dates('date', 'year').reverse()
    context = {'p_list':p_list,'institute':institute,'years':years}
    return render(request, 'ru/publications.html', context)


def pipub(request, nc):
    try:
        institute = Institute.objects.all().first()
        person = PrInvestigator.objects.get(nick=nc)
        p_list = Publication.objects.filter(prInvestigator=person)
        years = p_list.dates('date', 'year').reverse()
        context = {'p_list':p_list,'institute':institute,'years':years,'person':person}
    except PrInvestigator.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'ru/pipub.html', context)
