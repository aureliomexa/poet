from django.shortcuts import render
from poet.entities.work import get_work_context
from poet.entities.search import get_search_context
from poet.entities.entity import get_entity_context


def work(request, work_id):
    context = get_work_context(work_id)
    return render(request, context.template, context.data)


def entity(request, entity_id):
    context = get_entity_context(entity_id)
    return render(request, context.template, context.data)


def search(request, entity_name):
    search_term = request.GET.get('term', '')
    return render(request, 'poet/search.html.j2', get_search_context(entity_name, search_term))


def index(request):
    return render(request, 'poet/index.html.j2')


def home(request):
    return render(request, 'poet/home.html.j2')

