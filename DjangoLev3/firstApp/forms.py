from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name Need to start with Z :(')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    vemail = forms.EmailField(label='enter your email again ')
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_data  = super().clean()
        email = all_data['email']
        vmail = all_data['vemail']


        if email!= vmail :
            raise forms.ValidationError("chof mli7")
    # def clean_botCatcher(self):
    #
    #     botChatcher = self.cleaned_data['botCatcher']
    #
    #     if len(botChatcher) > 0 :
    #         raise forms.ValidationError("BotCatcher f!!!!!")
    #     return botChatcher
