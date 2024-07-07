from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostCreateForm


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

def main(request):
    return render (request, 'base.html')

class PostCreateView(AdminRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('main')