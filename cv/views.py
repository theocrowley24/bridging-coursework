from django.shortcuts import render
from .forms import EditForm
from .forms import AddQualification
from .forms import AddExperience
from .models import Cv
from .models import Experience
from .models import Qualification
from django.shortcuts import redirect

# Create your views here.
def home(request):
    cv = Cv.objects.get()
    experience = Experience.objects.all()
    qualifications = Qualification.objects.all()

    return render(request, 'home.html', {'cv': cv, 'experience': experience, 'qualifications': qualifications})

def edit(request):
    if request.method == "POST":
        if request.user.is_anonymous:
            return redirect("home")
        
        form = EditForm(request.POST, instance=Cv.objects.get())
        if form.is_valid():
            form.save()

    cv = Cv.objects.get()
    return render(request, 'edit.html', {'form': EditForm(instance=cv)})

def addExperience(request):
    if request.method == "POST":
        if request.user.is_anonymous:
            return redirect("home")

        form = AddExperience(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'addExperience.html', {'form': AddExperience()})

def addQualification(request):
    if request.method == "POST":
        if request.user.is_anonymous:
            return redirect("home")

        form = AddQualification(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'addQualification.html', {'form': AddQualification})