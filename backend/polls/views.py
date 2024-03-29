from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic 
from .models import Question, Choice



#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	context = {'latest_question_list': latest_question_list,}
#	return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Returen the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]

#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
		

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		# return the ID of the selected choice as string 
		# GET can be used too....
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist): # check for primary key existence. 
		return render(request, 'polls/detail.html',{
			'question': question,
			'error_message': "You didn't select a choice",
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		# return always after sucessful POST request =
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
