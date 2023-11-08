from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import students
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
#from django.http import get_object_or_404
from django.contrib import messages
from .forms import studentform

def index(request):
    context = {
        'students' : students.objects.all()
    }
    template ="student/index.html"
    return render(request, template, context)
    #return HttpResponse("Schhol Management")

def add_form(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have succesfully registered ')
            return redirect('index')
        else:
            messages.error(request, 'Invalid data entry, please try again ')
            return HttpResponseRedirect('add')
          
    else:
        form = studentform()
        return render(request, 'student/add.html', {'form':form})
        
def view_info(request, id):
    stu = students.object.get(pk=id)
    return HttpResponseRedirect('index')


def update_view(request, id):
   # if request.method == "POST":
        stu= students.objects.get(pk=id)
        form = studentform(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record succesfully updated ')
            return redirect('index')
            #return render(request, 'student/update.html', {'form':form,
                                                         #  'success':True})
        else:
            stu = students.objects.get(pk = id)
            form = studentform(instance=stu)
        return render(request, 'student/update.html', {'form':form})
 
def delete(request, id):
    if request.method == "POST":
        stu = students.objects.get(pk = id)
        stu.delete()
        messages.warning(request, 'Record succesfully deleted ')
            
    return HttpResponseRedirect(reverse('index'))


