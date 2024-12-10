from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
def home(request):
    return render(request, 'home.html')
def reg(request):
    return render(request, 'reg.html')
def add_course(request):
    return render(request, 'add_course.html')
def add_coursedb(request):
    if request.method == 'POST':
        course_name = request.POST.get('course')
        course_fee = request.POST.get('fee')
        course = Course(course_name=course_name, fee=course_fee)
        course.save()
        return redirect('add_student')  
def add_student(request):
    courses = Course.objects.all() 
    return render(request, 'add_student.html', {"courses": courses})
def add_studentdb(request):
    if request.method == 'POST':
        student_name = request.POST['name']
        student_address = request.POST['address']
        age = request.POST['age']
        jdate = request.POST['jdate'] 
        sel = request.POST['sel']
        course = Course.objects.filter(id=sel).first()         
        if not course:
            return redirect('error_page')  
        student = Student(
            student_name=student_name,
            student_address=student_address,
            student_age=age,
            joining_date=jdate, 
            course=course        
        )
        student.save()
        return redirect('show_details') 
def show_details(request):
    students = Student.objects.all() 
    return render(request, 'show_details.html', {'students': students})
def edit(request, pk):
    student = get_object_or_404(Student, id=pk) 
    courses = Course.objects.all() 
    return render(request, 'edit.html', {'student': student, 'courses': courses})
def editdb(request, pk):
    student = get_object_or_404(Student, id=pk)  
    if request.method == 'POST':
        student.student_name = request.POST['name']
        student.student_address = request.POST['address']
        student.student_age = request.POST['age']
        student.joining_date = request.POST['jdate']
        student.course = Course.objects.get(id=request.POST['sel'])     
        student.save() 
        return redirect('show_details') 
def delete(request, pk):
    student = get_object_or_404(Student, id=pk)  
    student.delete()  
    return redirect('show_details') 
