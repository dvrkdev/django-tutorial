from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(type(user))
            print(user)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_user.html', {'form': form})