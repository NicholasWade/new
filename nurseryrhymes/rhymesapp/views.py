from django.conf import settings
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Customer

from .forms import *
from .forms import ContactForm
from .forms import EditProfileForm
from .forms import RegisterForm
from .models import *
from django.shortcuts import render # new
import stripe # new
#PLEASE SUJU

now = timezone.now()
stripe.api_key = settings.STRIPE_SECRET_KEY # new



def home(request):
    return render(request, 'rhymesapp/home.html',
                 {'rhymesapp': home})


def audio_list(request):
    return render(request, 'rhymesapp/audio_list.html',
                 {'rhymesapp': audio_list})


@login_required
def account_information(request):
    account = Account.objects.filter(created_date__lte=timezone.now())
    return render(request, 'rhymesapp/account_information.html',
                 {'accounts': account})


def register(request):
    return render(request, 'rhymesapp/register.html', {'rhymesapp': register})


def rhymes_list(request):
    return render(request, 'rhymesapp/rhymes_list.html', {'rhymesapp': rhymes_list})

@login_required(login_url='login/')
def londonBridge(request):
    return render(request, 'rhymesapp/londonBridge.html', {'rhymesapp': londonBridge})

@login_required(login_url='login/')
def littleStar(request):
    return render(request, 'rhymesapp/littleStar.html', {'rhymesapp': littleStar})


def jackJill(request):
    return render(request, 'rhymesapp/jackJill.html', {'rhymesapp': jackJill})

@login_required(login_url='login/')
def itsySpider(request):
    return render(request, 'rhymesapp/itsySpider.html', {'rhymesapp': itsySpider})


def humptyDumpty(request):
    return render(request, 'rhymesapp/humptyDumpty.html', {'rhymesapp': humptyDumpty})


def hickoryDock(request):
    if Rhyme.premium:
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'rhymesapp/hickoryDock.html', {'rhymesapp': humptyDumpty})
            except Customer.DoesNotExist:
                return redirect('home/')
        return redirect('home/')
    else:
        return render(request, 'rhymesapp/hickoryDock.html', {'rhymesapp': humptyDumpty})

@login_required(login_url='login/')
def blackSheep(request):
    return render(request, 'rhymesapp/blackSheep.html', {'rhymesapp': blackSheep})

@login_required(login_url='login/')
def heyDiddle(request):
    return render(request, 'rhymesapp/heyDiddle.html', {'rhymesapp': heyDiddle})

@login_required(login_url='login/')
def hotBuns(request):
    return render(request, 'rhymesapp/hotBuns.html', {'rhymesapp': hotBuns})

@login_required(login_url='login/')
def jackNimble(request):
    return render(request, 'rhymesapp/jackNimble.html', {'rhymesapp': jackNimble})

@login_required(login_url='login/')
def market(request):
    return render(request, 'rhymesapp/market.html', {'rhymesapp': market})

@login_required(login_url='login/')
def muffins(request):
    return render(request, 'rhymesapp/muffins.html', {'rhymesapp': muffins})

@login_required(login_url='login/')
def peterPiper(request):
    return render(request, 'rhymesapp/peterPiper.html', {'rhymesapp': peterPiper})

@login_required(login_url='login/')
def piggy(request):
    return render(request, 'rhymesapp/piggy.html', {'rhymesapp': piggy})

@login_required(login_url='login/')
def rainPour(request):
    return render(request, 'rhymesapp/rainPour.html', {'rhymesapp': rainPour})

@login_required(login_url='login/')
def ringPosies(request):
    return render(request, 'rhymesapp/ringPosies.html', {'rhymesapp': ringPosies})

@login_required(login_url='login/')
def roses(request):
    return render(request, 'rhymesapp/roses.html', {'rhymesapp': roses})

@login_required(login_url='login/')
def rowBoat(request):
    return render(request, 'rhymesapp/rowBoat.html', {'rhymesapp': rowBoat})

@login_required(login_url='login/')
def sticks(request):
    return render(request, 'rhymesapp/sticks.html', {'rhymesapp': sticks})

@login_required(login_url='login/')
def threeMice(request):
    return render(request, 'rhymesapp/threeMice.html', {'rhymesapp': threeMice})

@login_required(login_url='login/')
def tweedle(request):
    return render(request, 'rhymesapp/tweedle.html', {'rhymesapp': tweedle})


class upgradeView(TemplateView):
    template_name = 'rhymesapp/upgrade.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    # return render(request, 'rhymesapp/upgrade.html', {'rhymesapp': upgrade})


def account_created(request):
    return render(request, 'rhymesapp/account_created.html', {'rhymesapp': account_created})


def email(request):
    return render(request, 'rhymesapp/contact.html', {'rhymesapp': email})


def success(request):
    return render(request, 'rhymesapp/success.html', {'rhymesapp': success})


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'rhymesapp/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts_created page:
                return HttpResponseRedirect('/register/account_created/')

    # No post data avaliable, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_address = form.cleaned_data['email_address']
            recipient_list = ['teamthreenurseryrhymes@gmail.com', ]
            try:
                send_mail(subject, message, email_address, recipient_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/email/success/')
    return render(request, 'rhymesapp/contact.html', {'form': form})



def infoView(request):
    args = {'user': request.user}
    return render(request, 'rhymesapp/account_information.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/account_information')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'rhymesapp/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account_information')
        else:
            return redirect('/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'rhymesapp/change_password.html', args)


def rhymes_list(request):
    search_term=''
    rhymes = Rhyme.objects.filter()
    if 'Search' in request.GET:
        search_term = request.GET['Search']
        rhymes = rhymes.filter(name__icontains=search_term)
    return render(request, 'rhymesapp/rhymes_list.html', {'rhymes': rhymes, 'search_term': search_term})




def charge(request):
    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, source=request.POST['stripeToken'])
        customer = Customer()
        customer.user = request.user
        customer.stripeid = stripe_customer.stripe_id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.save()
        return render(request, 'rhymesapp/charge.html')