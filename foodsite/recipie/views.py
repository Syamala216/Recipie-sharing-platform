from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.all().order_by('-created_at')

    if query:
        recipes = recipes.filter(title__icontains=query)

    return render(request, 'home.html', {'recipes': recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        Recipe.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            ingredients=request.POST.get('ingredients'),
            image=request.FILES.get('image')
        )
        return redirect('home')

    return render(request, 'add.html')