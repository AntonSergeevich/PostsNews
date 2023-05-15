from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class ContactForm(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='имя')
    lastname = models.CharField(max_length=50, verbose_name='фамилия')
    phone = PhoneNumberField(blank=True, verbose_name='телефон')
    email = models.EmailField()

    def __str__(self):
        return f'Заявка от: {self.firstname} <{self.phone}>'

    class Meta:
        verbose_name = 'Контактная форма'
        verbose_name_plural = 'Контактные формы'
