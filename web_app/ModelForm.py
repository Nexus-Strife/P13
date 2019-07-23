from .models import Art


class FormFromArtModel(forms.ModelForm):
    class Meta:
        model = Art
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }
