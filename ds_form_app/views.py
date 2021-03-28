from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    context = {
        'result': request.session['data_submit']
    }
    return render(request, 'result.html', context)

def handle_form(request):
    if request.method == 'POST':
        request.session['data_submit'] = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'languages': request.POST.getlist('language'),
            'answer': request.POST['answer'],
            'comment': request.POST['comment']
        }
    return redirect('/result')