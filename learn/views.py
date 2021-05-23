from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import SearchResults
def home(request):
    return render(request, 'learn/home.html')

context = { 'sad' : [ 'introduction', 'design', 'implimentation'],
            'js' : ['introduction','variable', 'for loop']
}

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', { 'form' : form })
class SearchResultsView(ListView):
    model = SearchResults
    template_name = 'learn/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = SearchResults.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list
def javascript(request):
    return render(request, 'learn/javascript/javascript_tutorial.html', context)
def system_analysis(request):
    return render(request, 'learn/sad/intro_to_sad.html',context)
def design(request):
    return render(request, 'learn/sad/design.html', context)
def implimentation(request):
    return render(request, 'learn/sad/implimentation.html', context)