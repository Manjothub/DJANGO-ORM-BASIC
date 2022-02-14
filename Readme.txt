Some Basic ORM Queries we have used in this project are:-

from home. models import Student
1) for fetching all result
            q=Student.objects.all()
2) for creating insert data 
            q=Student.objects.create(username="user2",first_name="Bkon",last_name="Kumar",mobile="8632028970",email="user2@gmail.com") 
3) for getting the single values 
            Q=Student.objects.get(id=1)
4) for filtering the particular values
            queryset = Student.objects.filter(first_name__startswith = 'A')
5) for adding the Bulk Values 
            Student.objects.bulk_create([Student(first_name = 'Jai', last_name = 'Shah', mobile = '88888', email = 'shah@reddif.com'),Student(first_name = 'Tarak', last_name = 'Mehta', mobile = '9999', email = 'tarak@reddif.com'), Student(first_name = 'SuryaKumar', last_name = 'Yadav', mobile = '00000', email = 'yadav@reddif.com')])
6) for mainpulating the data with Aggregate Function
            from django.db.models import Avg, Max, Min, Sum, Count  
 Student.objects.all().aggregate(Avg('id'))  
{'id__avg': 3.0}
 Student.objects.all().aggregate(Max('id'))   
{'id__max': 5}
 Student.objects.all().aggregate(Min('id'))   
{'id__min': 1}
 Student.objects.all().aggregate(Sum('id'))   
{'id__sum': 15}
 Student.objects.all().aggregate(Count('id'))   
{'id__count': 5}
Student.objects.all().count()      

7) Dnango Modifications 
 Student.objects.filter(first_name='Akon').delete() 
(1, {'home.Student': 1})
>>> Student.objects.all()                              
<QuerySet [<Student: Bkon Kumar>, <Student: Jai Shah>, <Student: Tarak Mehta>, <Student: SuryaKumar Yadav>]>
>>> q1 = Student.objects.filter(id__gte = 15)     
>>> q1
<QuerySet []>
>>> q2 = Student.objects.filter(id__lte = 15)
>>> q2
<QuerySet [<Student: Bkon Kumar>, <Student: Jai Shah>, <Student: Tarak Mehta>, <Student: SuryaKumar Yadav>]>
