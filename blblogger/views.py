from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.forms import Form

from .models import Blog
from django.views import generic
from django.views.generic.edit import CreateView
from blblogger.forms import CreateBlog, UserRegister, UserLogin
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.views.generic import View


class IndexView(generic.ListView):
    template_name = 'blblogger/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blblogger/detail.html'


class BlogCreateView(CreateView):
    template_name = 'blblogger/index.html'
    model = Blog
    fields = [
        "heading",
        "post"
    ]


class CreateUser(FormView):
    template_name = 'blblogger/index.html'
    success_url = '/blogger'
    form_class = CreateBlog

    def get_context_data(self, **kwargs):
        self.template_name = 'blblogger/index.html'
        self.success_url = 'blblogger/index.html'
        self.form_class = CreateBlog

        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            context =  super(CreateUser, self).get_context_data(**kwargs)
            context['blog'] = Blog.objects.all()
            return context


class UserRegisterView(View):
    form_class = UserRegister
    template_name = 'blblogger/register.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('/blogger')

        return render(request, self.template_name, {'form': form})


class UserLoginView(FormView):
    form_class = UserLogin
    template_name = 'blblogger/Login.html'
    success_url = '/blogger'

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})
