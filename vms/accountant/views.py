from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView
from django.contrib import messages


from .models import LogBook
from .forms import LogbookForm
from vmsUser.models import Requisition
from accounts.decorators import gaccountant_only


@login_required(login_url='login')
@gaccountant_only
def home(request):
    return render(request, 'accountant/accountanthome.html')


@login_required(login_url='login')
@gaccountant_only
def accNotice(request):
    return render(request, 'accountant/accountantnotice.html')


# @login_required(login_url='login')
# def logBook(request):
#     form = AccForm()
#     if request.method == 'POST':
#         form = AccForm(request.POST)
#         if form.is_valid():
#             acc_req = form.save(commit=False)
#             requisition = Requisition.objects.create()
#             requisition.vcl_type = ''
#             requisition.destination = ''
#             requisition.save()
#             acc_req.save()
#             # return redirect('acc_home')
#     # requisite = Requisition.objects.filter(is_requisited=True).order_by('jour_date')[:1]
#     # 'requisite': requisite
#     context = {'form': form}
#     return render(request, 'accountant/logbook.html', context)

# @login_required(login_url='login')
# @gaccountant_only
# def InfoSuccess(request, id=None):
#     return render(request, 'accountant/inputdetails.html', {
#         'logbook': get_object_or_404(LogBook, pk=id)
#     })


# @method_decorator(login_required(login_url='login'), name='dispatch')
# @method_decorator(gaccountant_only, name='dispatch')
# class LogBookCreate(SuccessMessageMixin, CreateView):
#     model = LogBook
#     form_class = AccForm
#     template_name = 'accountant/logbook.html'

#     # requisite = Requisition.objects.values()
#     # requisite = Requisition.objects.filter(is_requisited=True).order_by('jour_date')[:1]

#     def form_valid(self, form):
#         request = self.request
#         form.save()
#         form.instance.created_by = self.request.user
#         formsave = super().form_valid(form)
#         return formsave

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     requisite = Requisition.objects.filter(is_requisited=True).order_by('jour_date')[:1]
    #     return requisite
    #     # return Requisition.objects.filter(is_requisited=True).order_by('jour_date')[:1]
    #     # return Requisition.objects.all()

@login_required(login_url='login')
@gaccountant_only
def logbook(request):
    logbook = LogBook.objects.all()
    return render(request, 'accountant/logbook.html', {'logbook': logbook})


@login_required(login_url='login')
@gaccountant_only
def inputDetails(request):
    form = LogbookForm()
    if request.method == 'POST':
        form = LogbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LogBook')
    context = {'form': form}
    return render(request, 'accountant/inputdetails.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('homePage')