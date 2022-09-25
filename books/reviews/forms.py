from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        
        model = Review
        fields = ['rating', 'comment','user_name']
        widgets = {
            'comment': Textarea(attrs={'cols':10, 'rows': 5}),
        }