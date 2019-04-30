from django.urls import path

from . import views

urlpatterns = [
    # example: /polls/
	path('', views.index, name='index'),
	# example: /polls/id/
	path('<int:question_id>', views.detail, name="detail"),
	# example: /polls/id/results/
	path('<int:question_id>/results/', views.results, name="results"),
	# example: /polls/id/votes/
	path('<int:question_id>/vote/', views.vote, name="vote"),
]
