from django import forms
from django.forms import ModelForm
from . models import Topic, Category

class TopicCreateForm(ModelForm):
    class Meta:
        model=Topic
        fields=[
            'title',
            'user_name',
            'category',
            'message',
        ]
        
        
class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=[
            'title',
            'user_name',
            'category',
            'message',
        ]  

    widgets = {
        'title' : forms.TextInput(attrs={'class': 'hoge'}),
         'user_name' : forms.TextInput(attrs={'value': '名無し'}),
    }

    #以下を追加
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択して下さい'
        self.fields['user_name'].widget.attrs['value'] = '名無し'


#追加
class TopicForm(forms.Form):
    """トピック作成用のフォームクラス

    Formの使用例として作成

    """
    title = forms.CharField(
        label='タイトル',
        max_length=255,
        required=True,
    )
    user_name = forms.CharField(
        label='お名前',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'value': '名無し'}),
    )
    category = forms.ModelChoiceField(
        label='カテゴリー',
        queryset=Category.objects.all(),
        required=True,
        empty_label='選択して下さい',
    )
    message = forms.CharField(
        label='本文',
        widget=forms.Textarea,
        required=True,
    )
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)