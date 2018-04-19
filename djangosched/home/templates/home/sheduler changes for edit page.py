#courses/views.py

@login_required(login_url="/accounts/login/")
def edit_course(request, slug):
	course = Course.objects.get(slug = slug)
	if request.method == 'POST':
		form = forms.CreateCourse(request.POST, instance=course)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.professor = request.user
			instance.save()
			return redirect('courses:detail')
	else:
		form = forms.CreateCourse(request.FILES, instance=course)
	template = 'courses/course_edit.html'
	context = {'form': form, 'course':course, }
	return render(request, template, context)

#courses/urls.py
url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_course, name = 'edit_course'),

#courses/templates/courses/course_edit.html
{% extends 'base_html.html' %}

{% load static from staticfiles %}

{% block content %}
<head>
	<meta charset = "utf-8">
	<link rel = "stylesheet" href="{% static 'styles.css' %}">
		<title>Edit Course</title>
			<div class = "edit-course">
				<h2>Edit Course</h2>
				{{form}}
				<form class = 'site-form' action = '{% url "courses:detail" %}' method = 'post'>
				<input type = "submit" value = "Save">
				</form>
			</div>
	<script src="/static/slugify.js"></script>
{% endblock %}

#courses/templates/course_detail.html
<td><a href="{% url 'courses:edit_course' slug=course.slug %}"><button type="button" class="btn btn-warning">Edit</button></a></td>
##under the link to the style sheet

#courses/models.py

class Edit(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User, on_delete = True)
    course = models.ForeignKey(Course, on_delete = True)