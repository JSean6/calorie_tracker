from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_food_items')
    else:
        form = FoodItemForm()
    return render(request, 'add_food_item.html', {'form': form})

def list_food_items(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'list_food_items.html', {'food_items': food_items, 'total_calories': total_calories})

def delete_food_item(request, food_item_id):
    item = FoodItem.objects.get(id=food_item_id)
    item.delete()
    return redirect(request, 'list_food_items.html')

# def reset_calorie_count(request):
#     today = timezone.now().date()
#     FoodItem.objects.filter(date_added=today).delete()
#     return redirect(request, 'list_food_items')

def reset_view(request):
    if request.method == 'POST':
        # Handle the reset logic
        pass
    return render(request, 'list_food_items.html')

def some_view(request):
    if some_condition:
        return HttpResponseRedirect(reverse('reset'))
