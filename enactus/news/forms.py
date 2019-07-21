from django.forms.models import ModelForm
from news.models import Moment




class MomentForm(ModelForm):
    class Meta:
        model=Moment
        fields=('xiaoxi','user_name','kind')
