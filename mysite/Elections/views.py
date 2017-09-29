# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

'''def index(request):
    return HttpResponse("<h1>Welcome to Elections Committee")'''
from .models import  Voter,Choice
'''def index(request):
    latest_question_list = Voter.objects.order_by('-DOB')[:5]
    output = ', '.join([q.first_name for q in latest_question_list])
    return HttpResponse(output)'''

def index(request):
    latest_voter_list = Voter.objects.order_by('DOB')[:5]
    context = {'latest_voter_list': latest_voter_list}
    return render(request, 'Elections/index.html', context)

'''def detail(request, voter_id):
    try:
        voter = Voter.objects.get(pk=voter_id)
    except Voter.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'Elections/detail.html', {'voter': voter})'''

def detail(request, voter_id):
    voter = get_object_or_404(Voter, pk=voter_id)
    return render(request, 'Elections/detail.html', {'voter': voter})

'''def results(request, voter_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % voter_id)'''


def results(request, voter_id):
    voter = get_object_or_404(Voter, pk=voter_id)
    return render(request, 'Elections/results.html', {'voter': voter})

def vote(request, voter_id):
    voter = get_object_or_404(Voter, pk=voter_id)
    try:
        selected_choice = voter.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'Elections/detail.html', {
            'voter': voter,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Elections:results', args=(voter.id,)))


from django.views import generic


class IndexView(generic.ListView):
    template_name = 'Elections/index.html'
    context_object_name = 'latest_voter_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Voter.objects.order_by('-DOB')[:5]


class DetailView(generic.DetailView):
    model = Voter
    template_name = 'Elections/detail.html'


class ResultsView(generic.DetailView):
    model = Voter
    template_name = 'Elections/results.html'

