"""imports"""
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_view(request):

    # Received Post
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):

            user = form.save()

            # log user in
            login(request, user)

            return redirect("articles:list")

    # Received Other
    else:
        form = UserCreationForm()

    # Render resulting form (get request or error)
    return render(request, 'accounts/signup.html', {'form': form} )


def login_view(request):

    # Received Post
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            # log user in
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("articles:list")

    # Received Other
    else:
        form = AuthenticationForm()

    # Render resulting form (get request or error)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):

    # Received Post
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')