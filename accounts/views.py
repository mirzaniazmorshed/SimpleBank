from django.shortcuts import render
from django.views.generic import FormView
from django.forms import UserRegistrationForm
from django.urls import reverse_lazy
# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake