
from django.shortcuts import render

def register_students(request):



    if request.method == "POST":


        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        donation_per_round = request.POST.get("donation-per-round")
        fixed_donations = request.POST.get("fixed-donation")

        new_student_entry = {
            "firstname":firstname,
            "lastname":lastname,
            "donation_per_round":donation_per_round,
            "fixed_donations":fixed_donations,
        }

        # Add database function here >>>


    return render(request,"register_students.html")