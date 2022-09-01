from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm

from blango_auth.models import User


class BlangoRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(BlangoRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper() # refer formhelper. this is used to make forms without a .html template
        self.helper.add_input(Submit("submit", "Register")) # refer formhelper. to add a submit button named Register.