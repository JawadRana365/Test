from .models import Subject,Teacher
from table import Table
from table.columns import Column

class TeacherTable(Table):
	id = Column(field='id',header="ID")
	teacherId = Column(field='teacherId',header="Teacher Id")
	name = Column(field='name',header="Subject Name")
	clickable = {'class':'Row'}
	class Meta:
		model = Subject
		fields = ("id","teacherId","name")
