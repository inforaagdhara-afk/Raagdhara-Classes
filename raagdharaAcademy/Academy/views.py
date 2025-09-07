from django.shortcuts import render, redirect
from .models import Course
from Academy.models import Enrollment, Review, Contact
from django.contrib import messages


# Home page view
def home(request):
    return render(request, 'home.html')  # Simple home page render

# Courses page view
def courses(request):
    return render(request, 'courses.html')  # Courses page render

# Contact page view
def contact(request):
    return render(request, 'contact.html')  # Contact page render

# Enroll page view
def enroll(request):
    return render(request, 'enroll.html')  # Enroll page render

# About page view
def about(request):
    return render(request, 'about.html')  # About page render

# Reviews page view
def reviews(request):
    return render(request, 'reviews.html')  # Reviews page render

# def enroll_view(request):
#     courses = Course.objects.all()  # Fetch all courses from the database
#     return render(request, 'enroll.html', {'courses': courses})


# def submit_enrollment(request):
#     courses = Course.objects.all()
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('enrollment_success')  # Redirect to a success page
#     else:
#         form = EnrollmentForm()
#     return render(request, 'enroll.html', {'form': form, 'courses': courses})


def submit_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')

        # Check if fields are valid
        if name and review_text and rating:
            # Save the review in the database
            review = Review(name=name, review_text=review_text, rating=rating)
            review.save()

            # Redirect to the same page or to a thank you page
            return redirect('reviews')  # Assuming 'reviews' is the name of your review page URL

    return redirect('home')
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return redirect('contact')

        # Send an email or save to the database
        try:
            send_mail(
                f"Contact Form Submission: {name}",
                message,
                email,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('contact')
    return redirect('contact')

# def enroll_view(request):
#     courses = Course.objects.all()  # Fetch all courses from the database
#     return render(request, 'enroll.html', {'courses': courses})

# def submit_enrollment(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         course = request.POST.get('course')

#         # Basic validation (optional)
#         if not (name and email and mobile and course):
#             messages.error(request, "Please fill all the fields!")
#             return redirect('enroll')  # ya jahan form hai wahan redirect

#         # Save data to DB
#         Enrollment.objects.create(name=name, email=email, mobile=mobile, course=course)
#         messages.success(request, "You have been successfully enrolled!")
#         return redirect('enrollment_success')  # ya jahan chahiye wahan redirect

#     # agar GET request ho toh form page show karo
#     return render(request, 'enroll.html')


def submit_enrollment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        course = request.POST.get('course')

        # Simple validation
        if not (name and email and mobile and course):
            messages.error(request, "Please fill all the fields!")
            return redirect('enroll')

        # Save data
        Enrollment.objects.create(name=name, email=email, mobile=mobile, course=course)
        messages.success(request, "You have been successfully enrolled!")
        return redirect('enrollment_success')
    else:
        return redirect('enroll')

def enrollment_success(request):
    return render(request, 'enrollment_success.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # form के बाद contact पेज पर redirect कर रहे हैं
        else:
            messages.error(request, "Please fill out all fields.")
    
    return render(request, 'contact.html')