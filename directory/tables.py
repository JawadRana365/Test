from .models import Subject,Teacher
import django_tables2 as tables

class TeacherTable(tables.Table):
	# id = tables.Column(field='id',header="ID")
	# teacherId = tables.Column(field='teacherId',header="Teacher Id")
	# name = tables.Column(field='name',header="Subject Name")
	# clickable = {'class':'Row'}
	class Meta:
		model = Subject
		template_name = "django_tables2/bootstrap4.html"
		fields = ("id","teacherId","name")
