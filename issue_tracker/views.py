from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

@login_required
def get_issue_tracker_list(request):
    results = Item.objects.all()
    return render(request, "issue_tracker.html", {'items': results})



def create_an_issue(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_issue_tracker_list)
    else:
        form = ItemForm
    return render(request, "issue_form.html", {'form': form})


def edit_an_issue(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_issue_tracker_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "issue_form.html", {'form': form})


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_issue_tracker_list)
    
