from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406360016',
        'name': 'Jovian Felix Rustan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)