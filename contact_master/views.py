from django.shortcuts import render
from .models import Contact

# Create your views here.

def fill_contact(request):
    return render(request, 'contact_inputs.html')

def save_contact(request):
    cont = Contact()
    cont.first_name = request.POST['first_name']
    cont.last_name = request.POST['last_name']
    cont.email = request.POST['email']
    cont.phone_number = request.POST['phone_number']
    
    # Validate input
    error1 = False
    error2 = False
    if len(cont.first_name) == 0:
        error_message1 = 'First name is a required field.'
        error1 = True
    if len(cont.email) == 0:
        error_message2 = 'Email is a required field.'
        error2 = True
    if error1 or error2:
        return render(request, 'contact_inputs.html', {'error1':error1, 'error2':error2, 'error_message1':error_message1, 'error_message2':error_message2})
        
    # Save this to database
    cont.save()
      
    return render(request, 'submitcontactinfo.html', {'cont_object':cont})

def show_all_contacts(request):
    
    cont_list = Contact.objects.all()
    
    return render(request, "showcontacts.html", {"conts":cont_list})