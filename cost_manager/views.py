from django.shortcuts import render, get_object_or_404, redirect
from .models import Budget, PurchaseItem
from .forms import PurchaseItemForm

def budget_view(request):
    budget = Budget.objects.first()
    items = PurchaseItem.objects.all()
    total_spent = sum(item.price * item.quantity for item in items)
    remaining_budget = budget.total_budget - total_spent if budget else 0

    # Calculate total cost for each item
    items_with_total = []
    for item in items:
        item.total_cost = item.price * item.quantity
        items_with_total.append(item)

    return render(request, 'cost_manager/budget.html', {
        'budget': budget,
        'items': items_with_total,
        'total_spent': total_spent,
        'remaining_budget': remaining_budget
    })

def add_item(request):
    if request.method == "POST":
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_view')
    else:
        form = PurchaseItemForm()
    return render(request, 'cost_manager/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(PurchaseItem, id=item_id)
    if request.method == "POST":
        form = PurchaseItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('budget_view')
    else:
        form = PurchaseItemForm(instance=item)
    return render(request, 'cost_manager/edit_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(PurchaseItem, id=item_id)
    item.delete()
    return redirect('budget_view')