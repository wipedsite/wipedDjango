from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['info.wiped@gmail.com'], # to Email
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name': message_name})


	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def wipers(request):
	return render(request, 'wipers.html', {})

def service(request):
	return render(request, 'service.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def blog_details(request):
	return render(request, 'blog_details.html', {})



def booking(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_message = request.POST['your-message']

		# send an email
		booking = " Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Message: " + your_message
		send_mail(
			'Wiper Application', # subject
			booking, # message
			your_email, # from email
			['info.wiped@gmail.com'],
			fail_silently=False, # To Email
			)

		return render(request, 'booking.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_message': your_message
			})


	else:
		return render(request, 'home.html', {})






