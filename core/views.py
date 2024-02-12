from django.shortcuts import render, redirect


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html', {'user': request.user})
    else:
        return redirect("login")
