from django import forms as fms
from django.core.exceptions import ValidationError
import requests
from django.utils.text import slugify

from .models import Image
from django.core.files.base import ContentFile

print("love is the most fucking thing in hte world")
class ImageForm(fms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': fms.HiddenInput
            # this is a hiddedn field which comes along with the get method request while on create() view
            # in fact
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        extention = url.rsplit(".", 1)[1].lower()
        valid_extension = ['jpg', 'png', 'jpeg']
        if not (extention in valid_extension):
            raise ValidationError('url does not conatiain appropriate images format')
        return url

    def save(self, commit=True, force_insert=False, force_update=False):
        """get the url, make a name and extension, download contents and save it as images record field,
            finally save the Model record
        """
        cd = self.cleaned_data
        url = cd[
            'url']  # we achiev it from the form object, and that was filled with GET METHOD having a hidden input /?url=....
        download_response = requests.get(url)
        ImageRecord = super().save(commit=False)
        name = slugify(ImageRecord.title)
        extension = url.rsplit(".", 1)[1].lower()
        fullName = name + "." + extension
        ImageRecord.image.save(fullName, ContentFile(download_response.content),
                               save=False)  # this is ImageField field of Image model,
        # it has got many mehtods includding save mehtod
        if commit:
            ImageRecord.save()
        return ImageRecord  # it should return model's object, like any other modelForm save methods
