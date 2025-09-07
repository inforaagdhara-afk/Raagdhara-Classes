from django.db import models



class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Course Model
# class Course(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     duration = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# # Student Model
# # academy/models.py
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=10)
#     course = models.CharField(max_length=100)  # Static Courses (vocals, guitar, etc.)
#     # You can add more fields if needed.

    # def __str__(self):
    #     return self.name




class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Testimonial Model





class Testimonial(models.Model):
    student_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.rating}"



class Review(models.Model):
    name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()  # 1 to 5 rating

    def __str__(self):
        return f"Review by {self.name}"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




# Student Model
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=15, null=True, blank=True) 
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Changed to ForeignKey

#     def __str__(self):
#         return self.name
