from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student

def signup(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

import json

from django.contrib.auth.decorators import login_required
from .models import Student

@login_required
def dashboard(request):
    query = request.GET.get('roll_no')

    # 🔍 Search logic
    if query:
        students = Student.objects.filter(roll_no=query)
    else:
        students = Student.objects.all()

    # 📊 Graph logic (PUT YOUR CODE HERE)
    max_marks = 100
    graph_data = []

    for s in students:
        try:
            height = (float(s.marks) / max_marks) * 100
        except:
            height = 0

        graph_data.append({
            'name': s.name,
            'marks': s.marks,
            'height': height
        })

    # 📤 Send data to HTML
    return render(request, 'dashboard.html', {
        'students': students,
        'graph_data': graph_data
    })

@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            roll_no=request.POST['roll_no'],
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            age=request.POST['age'],
            marks=request.POST['marks'],
            attendance=request.POST['attendance'],
            dob=request.POST['dob']
        )
        return redirect('dashboard')
    return render(request, 'add_student.html')

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.roll_no = request.POST['roll_no']
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.marks = request.POST['marks']
        student.attendance = request.POST['attendance']
        student.dob = request.POST['dob']
        student.save()
        return redirect('dashboard')

    return render(request, 'edit_student.html', {'student': student})

@login_required
def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('dashboard')
