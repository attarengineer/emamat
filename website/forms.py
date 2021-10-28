from django import forms
from website.models import Contact
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # self.fields['created_date'] = JalaliDateField(label=('date'), # date format is  "yyyy-mm-dd"
        #     widget=AdminJalaliDateWidget # optional, to use default datepicker
        # )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['created_date'].widget.attrs.update({'class': 'jalali_date-date'})
        self.fields['message'].widget.attrs['placeholder'] = "پیام خود را در این قسمت بنویسید."
        # self.fields['update_date'] = SplitJalaliDateTimeField(label=('date time'),
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )