from django.shortcuts import render
from django.http import HttpResponseRedirect

from django import forms
from django.urls import reverse

# Create your views here.

# tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label='Priority', min_value=1, max_value=5)


def index(request):
    if 'tasks' not in request.session:
        # If no list of tasks in session create it.
        request.session['tasks'] = []
    return render(request,
                  template_name='tasks/index.html',
                  context={'tasks': request.session['tasks']})


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            # priority = form.cleaned_data['priority']
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # Send the invalid filled in form back to the user
            return render(request, "tasks/add.html",
                          {'form': form})

    return render(request, "tasks/add.html",
                  {'form': NewTaskForm()}
                  )
