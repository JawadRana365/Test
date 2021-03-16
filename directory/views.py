from django.shortcuts import render
from .models import Subject,Teacher
from .forms import SubjectForm,TeacherForm
from django.shortcuts import redirect
from django.contrib import messages
from .tables import TeacherTable


# Create your views here.
def index(request):
    if request.method == "POST":
        teacherForm = TeacherForm(request.POST or None, request.FILES or None)
        print(request.POST.get("emailAddress"))
        if teacherForm.is_valid():
            count = Teacher.objects.filter(emailAddress=request.POST.get("emailAddress")).count()
            if(count < 1):
                teacherForm.save()
                return redirect('test')

    page = {
        "teacherForm" : TeacherForm,
        "subjectForm" : SubjectForm,
        "teachers" : TeacherTable,
        "teacher" : Teacher.objects.all(),
        "subject" : Subject.objects.all(),
        "title" : "Teacher List",
        "session": request.session
    }
    return render(request,'index.html',page)

def subject(request):
    if request.method == "POST":
        subjectForm = SubjectForm(request.POST or None, request.FILES or None)
        if subjectForm.is_valid():
            count = Subject.objects.filter(teacherId=request.POST.get("teacherId")).count()
            if(count < 5):
                subjectForm.save()
    
    return redirect('test')


def profile(request,item_id):
    item = Teacher.objects.get(id=item_id)
    subject = Subject.objects.filter(teacherId=item)
    print(item) 
    print(subject) 
    page = {
        "profile" : item,
        "subjects" : subject
    }
    return render(request,'profile.html',page)
