import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import DeleteView, UpdateView

from .models import TemplateModel

from snappy.utils import log

from nlglib import pipeline
from nlglib import fol
from nlglib.simplifications import simplification_ops
from nlglib import lexicalisation


def homepage(request):
    return render(request, 'logic/homepage.html', {})


def demo(request):
    print(list(simplification_ops.values()))
    return render(request, 'logic/demo.html', {
        'simplifications': list(simplification_ops.keys()),
    })


def translate(request):
    """Read a given FOL formula as jason data and return it as text. """
    response_data = {}
    formula = request.POST['formula'].strip()
    response_data['formula'] = formula
    simplifications = [x.strip() for x in
                        request.POST.get('simplifications', '').split('|')]
    try :
        if formula:
            template_instances = TemplateModel.objects.all()
            templates = {}
            errors = []
            for t in template_instances:
                name = t.name
                try:
                    template = lexicalisation.string_to_template(t.content)
                    templates[name] = template
                except Exception as e:
                    errors.append( ('danger', str(e)) ) # use bootstrap terminology...
            response_data['text'] = pipeline.translate(formula, templates, simplifications)
            response_data['status'] = 'success'
            response_data['messages'] = json.dumps(errors)
        else:
            response_data['text'] = "Enter a formula first. E.g., 'Happy(you)'"
            response_data['status'] = 'default'
    except fol.FormulaParseError as e:
        response_data['text'] = str(e)
        response_data['status'] = 'error'
    except Exception as e:
        log().exception(e)
    return JsonResponse(response_data)


class TemplateCreateView(CreateView):
    model = TemplateModel
    fields = ['name', 'num_params', 'template_content']


class TemplateListView(ListView):
    model = TemplateModel
    template_name = 'logic/template_list.html'


class TemplateDetailView(DetailView):
    model = TemplateModel
    fields = ['name', 'num_params', 'template_content']
    template_name = 'logic/template_detail.html'


class TemplateDeleteView(DeleteView):
    model = TemplateModel


class TemplateUpdateView(UpdateView):
    model = TemplateModel
