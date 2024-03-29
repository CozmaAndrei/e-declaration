from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .forms import AddNewManagerForm, DeleteManagerForm, EditCompanyInfoForm, CompanyLogoForm
from users.models import ExtraUserInformations


'''Return all users asociated to company in companypage.html and the company name in URL '''
def company_profile(request, company_name):
    get_company_name = Company.objects.get(company_name=company_name) #used for companypage.html
    return render(request, 'company_html/companypage.html', {"get_company_name": get_company_name})

'''Update the company info, like name, email, logo, etc'''
def update_company_info(request, company_name):
    the_company = Company.objects.get(company_name=company_name) #used in updatecompanyprofileinfo.html
    if request.method == "POST":
        company_form = EditCompanyInfoForm(request.POST, instance=the_company)
        company_logo_form = CompanyLogoForm(request.POST, request.FILES, instance=the_company)
        if company_form.is_valid() and company_logo_form.is_valid():
            company_logo_form.save()
            company_form.save()
            messages.success(request, "Your company was edited with success!")
            return redirect ('company_profile', the_company.company_name)
    else:
        company_form = EditCompanyInfoForm(instance=the_company)
        company_logo_form = CompanyLogoForm(instance=the_company)
    
    context = {
        "company_form": company_form, 
        "the_company": the_company, 
        "company_logo_form": company_logo_form
        }
    return render(request, 'company_html/updatecompanyprofileinfo.html', context)

'''This function checked if the AddNewManagerForm is POST, take the input value and add to the managers field from Company table and return to the company page'''
def add_manager(request, company_name):
    get_company_name = Company.objects.get(company_name=company_name) #used in addmanagerpage.html
    if request.method == 'POST':
        form = AddNewManagerForm(request.POST)
        if form.is_valid():
            manager = form.cleaned_data['manager']
            get_company_name.managers.add(manager) #add the new manager at the company
            extra_info = ExtraUserInformations.objects.get(user=manager)
            extra_info.user_company.add(get_company_name) #added in user_company field from ExtraUserInformations the new company
            messages.success(request, f"The {manager} manager was successfully added!")
            return redirect('company_profile', get_company_name.company_name)
    else:
        form = AddNewManagerForm()
    return render(request, 'company_html/addmanagerpage.html', {'form': form, "get_company_name": get_company_name})

'''Delete the company account with conditions'''
def delete_company_account(request, company_name):
    company = Company.objects.get(company_name=company_name)
    company_managers = company.managers.all()

    if len(company_managers) == 1: #if you are the only one manager, then can delete the company
        company.delete()
        messages.success(request, "The company was successfully deleted!")
        return redirect('user_profile', request.user.username)
    elif len(company_managers) > 1: #if the company has more than one manager, you can't delete the company. You must delete all the managers first!.
        messages.warning(request, "If you want to delete the company, you must delete all the managers first!")
        return redirect('company_profile', company.company_name)

    return redirect('user_profile', request.user.username)

'''Return all the companies without the current user company in companieslistpage.html'''
def companies_list(request):
    all_companies = Company.objects.exclude(managers=request.user) #used in for loop in companieslistpage.html
    companies = ExtraUserInformations.objects.get(user=request.user) #used in companieslistpage.html
    favorite_companies = companies.favorite_company.all() #used in companieslistpage.html
    return render(request, 'company_html/companieslistpage.html', {"all_companies": all_companies, "favorite_companies": favorite_companies})

'''Return the company view profile for the rest of the users in viewcompanyprofile.html'''
def company_view_profile(request, company_name):
    company = Company.objects.get(company_name=company_name) #used in viewcompanyprofile.html
    current_user_profile = ExtraUserInformations.objects.get(user=request.user)  # Get the ExtraUserInformations instance for the current user
    if request.method == "POST":
        action = request.POST.get("follow")
        if action == "unfollow":
            current_user_profile.favorite_company.remove(company)
        elif action == "follow":
            current_user_profile.favorite_company.add(company)
        current_user_profile.save()
    return render(request, 'company_html/viewcompanyprofile.html', {"company": company,"current_user_profile": current_user_profile})

'''This function checked if the DeleteManagerForm is POST, take the input value and remove from the managers field from Company table and return to the company page'''
def delete_manager(request, company_name):
    get_company_name = Company.objects.get(company_name=company_name)
    if request.method == 'POST':
        form = DeleteManagerForm(request.POST, company=get_company_name)
        if form.is_valid():
            manager = form.cleaned_data['delete_managers']
            get_company_name.managers.remove(manager) #remove the mananger
            extra_info = ExtraUserInformations.objects.get(user=manager)
            extra_info.user_company.remove(get_company_name) #remove company from user_company field from ExtraUserInformations model
            messages.success(request, f"The {manager} manager was successfully deleted!")
            return redirect('company_profile', get_company_name.company_name)
    else:
        form = DeleteManagerForm(company=get_company_name)
    return render(request, 'company_html/deletemanagerpage.html', {'form': form, "get_company_name": get_company_name})











