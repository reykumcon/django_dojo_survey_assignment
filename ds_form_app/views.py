from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'languages': request.POST.getlist('language'),
            'answer': request.POST['answer'],
            'comment': request.POST['comment']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')