from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=250, unique=True, blank=False)
    state = models.CharField(max_length=250, blank=True)
    suburb = models.CharField(max_length=250, blank=False)
    street_name = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=250, blank=True)
    contact_name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=250, unique=True, blank=False, verbose_name='Email Address')
    phone = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return str(self.client_name)

    @property
    def get_address(self):
        return '{} {} {}'.format(self.street_name, self.state, self.postcode)

