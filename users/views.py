from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from companies.models import Company
from .forms import EditUserInfoForm, ChangeUserPassForm, UserPicForm, DeleteUserForm
from .models import ExtraUserInformations
from django.contrib.auth import login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required

def error404(request, exception):
    context = {
        'message': str(exception),
    }
    return render(request, 'error404.html', context, status=404)

'''Return the user profile with his username in URL and user information in userprofile.html'''
@login_required(login_url='/login_user/')
def user_profile(request, username): #used for userprofile.html
    try:
        the_user_name = User.objects.get(username=username)
        try:
            extra_info = ExtraUserInformations.objects.get(user=the_user_name) #used to get informations from ExtraUserInformations model
        except ExtraUserInformations.DoesNotExist:
            raise Http404("Extra user informations does not exist")
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        "the_user_name": the_user_name,
        "extra_info": extra_info
    }
    return render(request, 'user_html/userprofile.html', context)

'''Update the user info like username, first name, last name, etc with conditions and return the user profile in updateuserprofileinfo.html'''
@login_required(login_url='/login_user/')
def update_user_info(request, username):
    user = User.objects.get(username=username)
    extra_info = ExtraUserInformations.objects.get(user=user)
    if request.method == "POST":
        form = EditUserInfoForm(request.POST, instance=user)
        user_pic_form = UserPicForm(request.POST, request.FILES, instance=extra_info)
        if form.is_valid() and user_pic_form.is_valid():
            form.save()
            extra_info.save()
            user_pic_form.save()
            user.save()
            messages.success(request, "Profilul tau a fost editat cu succes!")
            return redirect ('user_profile', user.username)
    else:
        form = EditUserInfoForm(instance=user)
        user_pic_form = UserPicForm(instance=extra_info)
        
    context = {
        "form": form,
        "user_pic_form": user_pic_form,
        "user": user,
        "extra_info": extra_info
    }
    return render(request, 'user_html/updateuserprofileinfo.html', context)

'''Delete the user account with conditions and return the register_user.html page after the user account was deleted'''
@login_required(login_url='/login_user/')
def delete_user_account(request, user_id):
    user = User.objects.get(pk=user_id)
    user_companies = Company.objects.filter(managers=user)
    
    if request.method == "POST":
        delete_form = DeleteUserForm(request.POST or None)
        if delete_form.is_valid():
            email = delete_form.cleaned_data['email']
            if request.user.email == email:
                user = User.objects.get(email=email)
                if user_companies: #if user has a company
                    for company in user_companies:
                        managers = company.managers.all()
                        if len(managers) == 1 and user in managers: #if the user is the only one manager on his company, then he must delete the company first
                            if company.managers.count() == 1:
                                user.delete()
                                company.delete()
                                messages.success(request, "Contul tau a fost sters!")
                                return redirect('home')
                        elif len(managers) > 1 and user in managers: #if the company has many managers, then the user can delete the account
                            user.delete()
                            messages.success(request, "Contul tau a fost sters!")
                            return redirect('home')
                else: #if user has no company
                    user.delete()
                    messages.success(request, "Contul tau a fost sters!")
                    return redirect('home')
            else:
                messages.error(request, "The email you entered is not your email")
                return redirect('delete_user_account', user_id)
    else:
        delete_form = DeleteUserForm()  
    
    context = {
        "delete_form": delete_form,
        "user": user,
        "user_companies": user_companies,
    }
    return render(request, "user_html/deleteuseraccount.html", context)

'''Change the user password and return to the login page after the password was changed with success!'''
@login_required(login_url='/login_user/')
def change_pass(request,username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ChangeUserPassForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated, Please log in again!")
            logout(request)
            return redirect('login_user')
    else:
        form = ChangeUserPassForm(request.user)   
    
    context = {
        "user": user,
        "form": form
    }      
    return render(request, 'user_html/changeuserpass.html', context)











