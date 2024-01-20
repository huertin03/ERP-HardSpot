from django.shortcuts import render, redirect


def home_view(request):
    if request.user.is_authenticated:
        user_id = request.user.idempleado
        user_email = request.user.email
        user_name = request.user.nombre
        user_age = request.user.edad

        # You can use this information to render a template or create a custom response
        return render(request, 'core/home.html', {'user_id': user_id, 'user_email': user_email, 'user_name': user_name, 'user_age': user_age})
    else:
        return redirect("../login/")
