from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Post, Message, Doctors, Contact, Rodo, Reglamin, File_to_download
from .forms import PostCreateForm, MessageCreateForm, DoctorCreateForm, ContactCreateForm, RodoCreateForm, ReglaminCreateForm, FileToDownloadCreateForm


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
    
class PostListView(ListView):
    model = Post
    template_name = 'post_list_view.html'
    context_object_name = 'list'
    paginate_by = 3 

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = ['title', 'content', 'date']
        context['labels'] = {
            'title': 'Tytuł',
            'content': 'Treść',
            'date': 'Data dodania',
        }
        
        elements = context['list']
        update_urls = []
        delete_urls = []
        file_upload_urls = []
        
        for element in elements:
            update_url = reverse('post_update', kwargs={'pk': element.pk})
            delete_url = reverse('post_delete', kwargs={'pk': element.pk})
            file_upload_url = element.file.url if element.file else None
            
            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(file_upload_url)

        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls)
        
        messages = Message.objects.all()
        active_messages = [msg for msg in messages if msg.date_start <= timezone.now().date() <= msg.date_end]
        context['active_messages'] = active_messages

        return context

def main(request):
    return PostListView.as_view()(request)


class DoctorCreateView(AdminRequiredMixin, CreateView):
    model = Doctors
    form_class = DoctorCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('doctor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj nowego lekarza'
        return context
    
    
class DoctorListView(AdminRequiredMixin, ListView):
    model = Doctors
    template_name = 'list_view.html'
    context_object_name = 'list'
    paginate_by = 3 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Lista Lekarzy'
        context['fields'] = ['first_name', 'last_name', 'specialization', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'file_upload_url']
        context['labels'] = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'specialization': 'Specjalizacja',
            'monday': 'Poniedziałek',
            'tuesday': 'Wtorek',
            'wednesday': 'Środa',
            'thursday': 'Czwartek',
            'friday': 'Piątek',
            'file_upload_url': 'Plik do pobrania'
        }

        elements = context['list'] 
        
        file_upload_urls = []

        if self.request.user.is_staff:
            context['create_url'] = reverse('doctor_create')
            context['button_name'] = 'Dodaj lekarza'
            update_urls = []
            delete_urls = []
        
        for element in elements:  
            update_url = reverse('doctor_update', kwargs={'pk': element.pk})  
            delete_url = reverse('doctor_delete', kwargs={'pk': element.pk}) 
            file_upload_url = element.file_upload.url if element.file_upload else None 

            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(file_upload_url)

        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls) 

        return context
    

class DoctorUpdateView(AdminRequiredMixin, UpdateView):
    model = Doctors
    form_class = DoctorCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('doctor_list')
    
    
class DoctorDeleteView(AdminRequiredMixin, DeleteView):
    model = Doctors
    template_name = 'delete.html'
    success_url = reverse_lazy('doctor_list')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('doctor_list')
        
        return context
    

class PostCreateView(AdminRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj post'
        return context
    

class PostUpdateView(AdminRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    
class PostDeleteView(AdminRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('main')
        
        return context
    
    
class MessageCreateView(AdminRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj komunikat'
        
        return context
    
    
class MessageListView(ListView):
    model = Message
    template_name = 'list_view.html'
    context_object_name = 'list'
    paginate_by = 3 
    
    def get_queryset(self):
        return Message.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Lista komunikatów'
        context['fields'] = ['title', 'text']
        context['labels'] = {
            'title':'Tytuł',
            'text':'Treść',
        }
        
        elements = context['list']
        
        if self.request.user.is_staff:
            context['create_url'] = reverse('message_create')
            context['button_name'] = 'Dodaj komunikat'
            update_urls = []
            delete_urls = []
            file_upload_urls = []
            
        for message in elements:  
            update_url = reverse('message_update', kwargs={'pk': message.pk})  
            delete_url = reverse('message_delete', kwargs={'pk': message.pk}) 
            
            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(None)
            
        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls) 
            
        return context


class MessageUpdateView(AdminRequiredMixin, UpdateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('message_list')
    
    
class MessageDeleteView(AdminRequiredMixin, DeleteView):
    model = Message
    template_name = 'delete.html'
    success_url = reverse_lazy('message_list')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('message_list')
        
        return context
    
class ContactCreateView(AdminRequiredMixin, CreateView):
    model = Contact
    form_class = ContactCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('contact_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj dane kontaktowe'
        
        return context
    
    
class ContactListView(ListView):
    model = Contact
    template_name = 'list_view.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Kontakt z nami'
        context['fields'] = ['number_phone_1', 'number_phone_2', 'email', 'email_2', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        context['labels'] = {
            'number_phone_1':'Numer kontaktowy do rejestracji',
            'number_phone_2':'Numer kontaktowy do biura',
            'email':'Email do rejestracji',
            'email_2':'Email do biura',
            'monday': 'Poniedziałek',
            'tuesday': 'Wtorek',
            'wednesday': 'Środa',
            'thursday': 'Czwartek',
            'friday': 'Piątek',
        }
        
        elements = context['list']
        
        file_upload_urls = []

        if self.request.user.is_staff:
            context['create_url'] = reverse('contact_create')
            context['button_name'] = 'Dodaj dane'
        update_urls = []
        delete_urls = []
        
        for element in elements:  
            update_url = reverse('contact_update', kwargs={'pk': element.pk})  
            delete_url = reverse('contact_delete', kwargs={'pk': element.pk}) 

            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(None)

        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls)
        
        return context
    


class ContactUpdateView(AdminRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('contact_list')
    
    
class ContactDeleteView(AdminRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = reverse_lazy('contact_list')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('contact_list')
        
        return context
    
    
class RodoCreateView(AdminRequiredMixin, CreateView):
    model = Rodo
    form_class = RodoCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('rodo_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj Rodo'
        return context
    
    
class RodoListView(ListView):
    model = Rodo
    template_name = 'list_view.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Rodo'
        context['fields'] = ['text', 'file_upload_url']
        context['labels'] = {
            'text': 'Treść',
            'file_upload_url': 'Plik do pobrania'
        }

        elements = context['list']

        file_upload_urls = []

        if self.request.user.is_staff:
            context['create_url'] = reverse('rodo_create')
            context['button_name'] = 'Dodaj rodo'
        update_urls = []
        delete_urls = []

        for element in elements:
            update_url = reverse('rodo_update', kwargs={'pk': element.pk})
            delete_url = reverse('rodo_delete', kwargs={'pk': element.pk})
            file_upload_url = element.file_upload.url if element.file_upload else None

            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(file_upload_url)

        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls)

        return context
        

class RodoUpdateView(AdminRequiredMixin, UpdateView):
    model = Rodo
    form_class = RodoCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('rodo_list')
    
    
class RodoDeleteView(AdminRequiredMixin, DeleteView):
    model = Rodo
    template_name = 'delete.html'
    success_url = reverse_lazy('rodo_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('rodo_list')
        
        return context
    

class ReglaminCreateView(AdminRequiredMixin, CreateView):
    model = Reglamin
    form_class = ReglaminCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('reglamin_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Dodaj regulamin'
        return context
    
    
class ReglaminListView(ListView):
    model = Reglamin
    template_name = 'list_view.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Regulamin'
        context['fields'] = ['text', 'file_upload_url']
        context['labels'] = {
            'text': 'Treść',
            'file_upload_url': 'Plik do pobrania'
        }

        elements = context['list']

        file_upload_urls = []

        if self.request.user.is_staff:
            context['create_url'] = reverse('reglamin_create')
            context['button_name'] = 'Dodaj regulamin'
        update_urls = []
        delete_urls = []

        for element in elements:
            update_url = reverse('reglamin_update', kwargs={'pk': element.pk})
            delete_url = reverse('reglamin_delete', kwargs={'pk': element.pk})
            file_upload_url = element.file_upload.url if element.file_upload else None

            update_urls.append(update_url)
            delete_urls.append(delete_url)
            file_upload_urls.append(file_upload_url)

        context['element'] = zip(elements, update_urls, delete_urls, file_upload_urls)

        return context
        


class ReglaminUpdateView(AdminRequiredMixin, UpdateView):
    model = Reglamin
    form_class = ReglaminCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('reglamin_list')
    
    
class ReglaminDeleteView(AdminRequiredMixin, DeleteView):
    model = Reglamin
    template_name = 'delete.html'
    success_url = reverse_lazy('reglamin_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('reglamin_list')
        
        return context
        
    
    
class FileToDownloadCreateView(AdminRequiredMixin, CreateView):
    model = File_to_download
    form_class = FileToDownloadCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('file_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Pliki do pobrania'
        return context
    
class FileToDownloadListView(ListView):
    model = File_to_download
    template_name = 'list_to_download.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Pliki do pobrania'
        context['fields'] = ['rodo', 'reglamin', 'doctor', 'nurse', 'instruction', 'calendar', 'application_for_authorisation']
        context['labels'] = {
            'rodo': 'RODO',
            'reglamin': 'Reglamin przychodni',
            'doctor': 'Deklaracja POZ (lekarz)',
            'nurse': 'Deklaracja POZ (pielęgniarka)',
            'instruction': 'Instrukcja wypełnienia deklaracji',
            'calendar': 'Kalendarz szczepień',
            'application_for_authorisation': 'Pełnomocnictwo',
        }

        elements = context['list']
        file_elements = []

        if self.request.user.is_staff:
            context['create_url'] = reverse('file_create')
            context['button_name'] = 'Dodaj plik'
        
        for element in elements:
            file_info = {
                'element': element,
                'fields': [],
                'update_url': reverse('file_update', kwargs={'pk': element.pk}),
                'delete_url': reverse('file_delete', kwargs={'pk': element.pk}),
            }
            
            for field in context['fields']:
                file_url = getattr(element, field).url if getattr(element, field) else None
                if file_url:
                    file_info['fields'].append({
                        'label': context['labels'][field],
                        'url': file_url,
                    })
            
            file_elements.append(file_info)

        context['file_elements'] = file_elements

        return context


class FileToDownloadUpdateView(AdminRequiredMixin, UpdateView):
    model = File_to_download
    form_class = FileToDownloadCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('file_list')
    
    
class FileToDownloadDeleteView(AdminRequiredMixin, DeleteView):
    model = File_to_download
    template_name = 'delete.html'
    success_url = reverse_lazy('file_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('file_list')
        
        return context
    
    
class OffersListView(ListView):
    model = Doctors
    template_name ='offers.html'
    
    def get_queryset(self):
        return Doctors.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor_days'] = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        return context

class DeclarationListView(ListView):
    model = File_to_download
    template_name = 'declaration.html'
    context_object_name = 'list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = 'Pliki do pobrania'
        context['fields'] = ['doctor', 'nurse', 'instruction']
        context['labels'] = {
            'doctor': 'Deklaracja POZ (lekarz)',
            'nurse': 'Deklaracja POZ (pielęgniarka)',
            'instruction': 'Instrukcja wypełnienia deklaracji',
        }

        elements = context['list']
        file_elements = []

        for element in elements:
            file_info = {'fields': []} 
            
            for field in context['fields']:
                file_url = getattr(element, field).url if getattr(element, field) else None
                if file_url:
                    file_info['fields'].append({
                        'label': context['labels'][field],
                        'url': file_url,
                    })
            
            file_elements.append(file_info)

        context['file_elements'] = file_elements

        return context
    