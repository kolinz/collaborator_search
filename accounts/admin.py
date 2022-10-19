from django.contrib import admin

# Register your models here.
# カスタムUserをインポート
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとusernameを表示する
    list_display = ('id', 'username')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'username')

#Django管理サイトにCustomUser、CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)