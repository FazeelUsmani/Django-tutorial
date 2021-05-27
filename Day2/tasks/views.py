from django.shortcuts import render
from datetime import datetime

# Django ORM (Object Relational Mapper)

current_tasks = [
    'Create a simple django project',
    'Learn blockchain',
    'Revise OOPS'
]



# Create your views here.
def index_page(request):
    return render(request, 'index.html', 
                    context={
                        'curr_date': str(datetime.now()),
                        'tasks': current_tasks,
                    })