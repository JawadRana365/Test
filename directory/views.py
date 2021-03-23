from django.shortcuts import render
from .models import Subject,Teacher
from .forms import SubjectForm,TeacherForm
from django.shortcuts import redirect
from django.contrib import messages
from .tables import TeacherTable
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest
import csv, io
from csv import reader
import codecs
from django_tables2 import RequestConfig


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
    teachers = TeacherTable(Subject.objects.all())
    RequestConfig(request).configure(teachers)
    page = {
        "teacherForm" : TeacherForm,
        "subjectForm" : SubjectForm,
        "teachers" : teachers,
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

# from DDIB.DDIv3CSV.RevisedDD.app.models import Privileges
from django.contrib.auth.models import User

def bulkupload(request):
    if request.method == "POST":
        try:
            csv_file = request.FILES['BulkCSVFile']
            if not csv_file.name.endswith('.csv'):
                messages.success(request, 'File is not a CSV')
                assert isinstance(request, HttpRequest)

                return render(
                    request,
                    'bulkupload.html',
                    {
                        'msg': 'File is not CSV type',

                    }
                )


            read = csv.reader(codecs.iterdecode(csv_file, 'utf-8'))
            header = next(read)
            if header != None:
                for row in read:
                    if row[0]!='' and row[1]!='':
                        print (row)
                        count = Teacher.objects.filter(emailAddress=row[3]).count()
                        if(count < 1):
                            Teacher(firstName=row[0],lastName=row[1],profilePicture=row[2],emailAddress=row[3],phoneNumber=row[4]).save()
                            teacher = Teacher.objects.latest('lastName')
                        else:
                            teacher = Teacher.objects.get(emailAddress=row[3])
                        count = Subject.objects.filter(teacherId=teacher).count()
                        if(count < 5):
                            subjects = row[6].split(',')
                            for subject in subjects:
                                Subject(teacherId=teacher,name=subject,roomNo=row[5]).save()
                                count = Subject.objects.filter(teacherId=teacher).count()
                                if(count > 5):
                                    break
        except Exception as e:
            print (e)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'bulkupload.html',
                {
                    'msg': 'Unable to upload file',

                }
            )
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'bulkupload.html',
            {
                'msg': 'True',
            }
        )
    else:
        assert isinstance(request, HttpRequest)
        return render( request, 'bulkupload.html',{} )