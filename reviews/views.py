from django.shortcuts import redirect
from .forms import ReviewForm
from django.views import View
from django.contrib import messages
from NewsPaper import settings
from django.core.mail import send_mail

class ReviewsView(View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MY_INFO, 'сообщение отправлено ☺')

            send_mail('Заявка с сайта',
                      f'Имя: {form.cleaned_data["firstname"]}\nТелефон: {form.cleaned_data["phone"]}\nemail: {form.cleaned_data["email"]}',
                      settings.EMAIL_HOST_USER, ['glukhovas@yandex.ru'])
        else:
            messages.add_message(request, settings.MY_INFO, form.errors)
        return redirect("/" + '#firstname')




