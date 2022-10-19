from importlib.abc import ExecutionLoader
from tkinter import Widget
from django.forms import ModelForm
from .models import Persondata, Resultdata

# 人物情報の作成
class PersondataForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        Attributes
        model: モデルのクラス
        fields: フォームで使用するモデルのフィールドを指定
        '''
        model = Persondata
        fields = ['occupation', 'title','org', 'name', 'gender', 'summary', 'collabat', 'specialat', 'interest', 'snsurl']

# 実績情報の作成
class ResultdataForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        Attributes
        model: モデルのクラス
        fields: フォームで使用するモデルのフィールドを指定
        '''
        model = Resultdata
        fields = ('resulttype', 'name', 'event',)