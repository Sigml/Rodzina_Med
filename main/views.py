from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Post, Message, Doctors, Contact, Rodo, Reglamin, File_to_download
from .forms import PostCreateForm, MessageCreateForm, DoctorCreateForm, ContactCreateForm, RodoCreateForm, ReglaminCreateForm, FileToDownloadCreateForm


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

def main(request):
    return render (request, 'base.html')


class DoctorCreateView(AdminRequiredMixin, CreateView):
    model = Doctors
    form_class = DoctorCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj nowego lekarza'
        return context
    
    
class DoctorListView(ListView):
    model = Doctors
    template_name = 'list_view.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Lista Lekarzy'
        context['fields'] = ['first_name', 'last_name', 'specialization', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        return context

class DoctorUpdateView(AdminRequiredMixin, UpdateView):
    model = Doctors
    form_class = DoctorCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class DoctorDeleteView(AdminRequiredMixin, DeleteView):
    model = Doctors
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    

class PostCreateView(AdminRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
    
class PostListView(ListView):
    model = Post
    template_name = 'list_view.html'


class PostUpdateView(AdminRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class PostDeleteView(AdminRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    
    
class MessageCreateView(AdminRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
    
class MessageListView(ListView):
    model = Message
    template_name = 'list_view.html'


class MessageUpdateView(AdminRequiredMixin, UpdateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class MessageDeleteView(AdminRequiredMixin, DeleteView):
    model = Message
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    
    
class ContactCreateView(AdminRequiredMixin, CreateView):
    model = Contact
    form_class = ContactCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
    
class ContactListView(ListView):
    model = Contact
    template_name = 'list_view.html'


class ContactUpdateView(AdminRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class ContactDeleteView(AdminRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    
    
class RodoCreateView(AdminRequiredMixin, CreateView):
    model = Rodo
    form_class = RodoCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
class RodoListView(ListView):
    model = Rodo
    template_name = 'list_view.html'


class RodoUpdateView(AdminRequiredMixin, UpdateView):
    model = Rodo
    form_class = RodoCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class RodoDeleteView(AdminRequiredMixin, DeleteView):
    model = Rodo
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    

class ReglaminCreateView(AdminRequiredMixin, CreateView):
    model = Reglamin
    form_class = ReglaminCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
    
class ReglaminListView(ListView):
    model = Reglamin
    template_name = 'list_view.html'


class ReglaminUpdateView(AdminRequiredMixin, UpdateView):
    model = Reglamin
    form_class = ReglaminCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class ReglaminDeleteView(AdminRequiredMixin, DeleteView):
    model = Reglamin
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    
    
class FileToDownloadCreateView(AdminRequiredMixin, CreateView):
    model = File_to_download
    form_class = FileToDownloadCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Uzupelnić'
        return context
    
class FileToDownloadListView(ListView):
    model = File_to_download
    template_name = 'list_view.html'


class FileToDownloadUpdateView(AdminRequiredMixin, UpdateView):
    model = File_to_download
    form_class = FileToDownloadCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class FileToDownloadDeleteView(AdminRequiredMixin, DeleteView):
    model = File_to_download
    template_name = 'delete.html'
    success_url = reverse_lazy('main')