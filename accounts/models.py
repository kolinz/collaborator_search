from django.db import models
# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    '''Userモデルを継承したカスタムユーザーモデル
    '''
    # フィールドを追加しない場合は、passを記述
    pass