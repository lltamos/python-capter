from django import forms
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.template.context_processors import csrf

from .models import Character


def index(request):
    return HttpResponse("this is first app")


def staff(request):
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)
    return render(request, 'staffadmin/staff.html', {'staffs': staff_list})


def template(request):
    context = {}
    context.setdefault('label', 'Hello World!')
    return render(request, 'staffadmin/template.html', context)


def form_get(request):
    return render(request, 'staffadmin/form.html')


def form_post(request):
    return render(request, 'staffadmin/investigate.html')


class CharacterForm(forms.Form):
    staff = forms.CharField(max_length=10
                            , error_messages={"max_length": "最长10字符", "required": "字段不能为空"})


def result(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            ctx['rlt'] = request.POST['staff']
            new_str = ctx.get('rlt', 'default')
            new_record = Character(name=new_str)
            new_record.save()
        all_records = Character.objects.all()
        ctx.setdefault('staff', all_records)
        return render(request, 'staffadmin/investigate.html', ctx)

    if request.GET:
        rlt = request.GET['staff']
        return HttpResponse(rlt)

    else:
        return HttpResponse('Null')
