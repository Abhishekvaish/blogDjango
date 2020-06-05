from django.shortcuts import render,redirect
from .forms import UserRegisterationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.contrib.auth import get_user_model,login

# Create your views here.


def register(request):
	form = UserRegisterationForm()
	if request.method == "POST":
		form = UserRegisterationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string('user/acc_active_email.html', {
			    'user': user,
			    'domain': current_site.domain,
			    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			    'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
			email.content_subtype = 'html'
			email.send()
			return render(request,'user/msg.html',{"confirmation":True})
			'''form.save()
			messages.success(request, "Your Account has been created successfully you can go ahead and signIn")
			return redirect('login')'''
	return render(request, 'user/register.html',{'form':form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = get_user_model().objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		messages.success(request, "Your Account has been verified successfully you can go ahead and signIn")
		return redirect('login')
	else:
		return render(request, 'user/msg.html',{'invalid':True})

@login_required
def profile(request):
	return render(request, 'user/profile.html')	

@login_required
def profile_update(request):
	u_form = UserUpdateForm(instance=request.user)
	p_form = ProfileUpdateForm(instance=request.user.profile)
	if request.method =="POST":
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, "Your Account has been Updated")
			return redirect('profile')
	context = {
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request, 'user/profile_update.html',context)
