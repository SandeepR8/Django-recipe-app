from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Recipes
from .forms import RecipeForm

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def show_recipes(request):
    query = request.GET.get('query', '')

    if query:
        recipes = Recipes.objects.filter(name__icontains=query)  # Case-insensitive search
        if not recipes.exists():
            return render(request, '404.html', {'message': 'Recipe not found'})
    else:
        recipes = Recipes.objects.all()

    return render(request, 'show_recipes.html', {'recipes': recipes})

def Base_page(request):
    return render(request,'base.html',{})


def custom_404(request,exception):
    return render(request, '404.html', status=404)
