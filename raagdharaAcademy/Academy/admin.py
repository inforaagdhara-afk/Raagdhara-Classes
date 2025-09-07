from django.contrib import admin
from .models import Course,Testimonial, Review, Enrollment, Contact

# Registering models for the admin interface
admin.site.register(Course)
# admin.site.register(Student)
admin.site.register(Testimonial)
admin.site.register(Review)
admin.site.register(Enrollment)
admin.site.register(Contact)