from django.core.validators import RegexValidator


'''
This regex assumes that you have a clean string,
you should clean the string for spaces and other characters
'''

isalphavalidator = RegexValidator(r'^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$',
                                  message='name must be alphanumeric',
                                  code='Invalid name')
