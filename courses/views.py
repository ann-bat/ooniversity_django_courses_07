from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def detail(request, course_id):
    course_inf = Course.objects.get(id=course_id)
    teacher = {'f_name': course_inf.coach.user.first_name, 
                'l_name': course_inf.coach.user.last_name,
                'descr': course_inf.coach.description,
                'id': course_inf.coach.id}
    assistant = {'f_name': course_inf.assistant.user.first_name, 
                'l_name': course_inf.assistant.user.last_name,
                'descr': course_inf.assistant.description,
                'id': course_inf.assistant.id}
    print(assistant)
    course_plan = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_inf': course_inf, 'course_plan': course_plan,
                                                    'teacher': teacher, 'assistant': assistant})

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, ('Course %s has been successfully added.' % data['name']))
            return redirect("index")
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    edit_course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=edit_course)
        if form.is_valid():
            form.save()
            text_for_success = 'The changes have been saved.'
            messages.success(request, text_for_success)
            return redirect('courses:edit', course_id=course_id)
    else:
        form = CourseModelForm(instance=edit_course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    remove_course = Course.objects.get(id=course_id)
    if request.method == "POST":
        text_for_success = 'Course ' + str(remove_course.name) +  ' has been deleted.'
        messages.success(request, text_for_success)
        remove_course.delete()
        return redirect("index")
    else:
        return render(request, 'courses/remove.html', {'remove_course': remove_course})


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = Course.objects.get(id=course_id)
            text_for_success = 'Lesson ' + data.name +  ' has been successfully added.'
            messages.success(request, text_for_success)
            return redirect("courses:detail", course_id=course_id)
    else:
        data = Course.objects.get(id=course_id)
        form = LessonModelForm(initial={'course': data.id})
    return render(request, 'courses/add_lesson.html', {'form': form})