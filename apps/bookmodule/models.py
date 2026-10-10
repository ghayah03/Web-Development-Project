from django.db import models

# ===== LAB 7 & 8 Models =====
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    
    def __str__(self):
        return f"{self.title} - {self.author}"

class Address(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city

# ===== LAB 9 Models =====
class Card(models.Model):
    card_number = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Card {self.card_number}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} ({self.code})"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through='Enrollment')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #date_enrolled = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'course')




class Address2(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address2, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name




class Address3(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city

class Student3(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address3)
    
    def __str__(self):
        return self.name    




class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.name
        