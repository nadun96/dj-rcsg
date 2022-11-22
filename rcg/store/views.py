from django.shortcuts import render

# Create your views here.

def manage(request):
    context = {
        'title': 'manage',
    }
    return render(request, 'store/manage.html', context)


def items(request):
    context = {
        'title': 'items',
    }
    return render(request, 'store/items.html', context)


def lend(request):
    context = {
        'title': 'lend',
    }
    return render(request, 'store/lend.html', context)


def reports(request):
    context = {
        'title': 'reports',
    }
    return render(request, 'store/reports.html', context)

def broken(request):
    context = {
        'title': 'broken',
    }
    return render(request, 'store/broken.html', context)