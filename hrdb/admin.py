from django.contrib import admin

# Register your models here.
from .models import Occupation, Org, Title, Persondata, Resulttype, Resultdata


# 職種情報の管理
class OccupationAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameを表示する
    list_display = ('id', 'name')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name')
    
#Django管理サイトで、Occupation、OccupationAdminを登録する
admin.site.register(Occupation, OccupationAdmin)


# 所属組織名情報の管理
class  OrgAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameを表示する
    list_display = ('id', 'name')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name')
    
#Django管理サイトにOrg、OrgAdminを登録する
admin.site.register(Org, OrgAdmin)


# 肩書情報の管理
class  TitleAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameを表示する
    list_display = ('id', 'name')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name')
    
#Django管理サイトにTitle、TitleAdminを登録する
admin.site.register(Title, TitleAdmin)


# 人物情報の管理
class PersondataAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameとauthorを表示する
    list_display = ('id', 'name', 'org')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name', 'org')
    
#Django管理サイトにPersonData、PersonDataAdminを登録する
admin.site.register(Persondata, PersondataAdmin)


# 実績の種別の管理
class ResultTypeAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameとauthorを表示する
    list_display = ('id', 'name')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name')
    
#Django管理サイトで、EventType、EventTypeAdminを登録する
admin.site.register(Resulttype, ResultTypeAdmin)


# 実績情報の管理
class ResultDataAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧を表示するカラムを設定するためのクラス
    '''
    #レコード一覧に、idとnameとauthorを表示する
    list_display = ('id', 'name', 'resulttype', 'persondata')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'name', 'resulttype', 'persondata')
    
#Django管理サイトにCareerData、CareerDataAdminを登録する
admin.site.register(Resultdata, ResultDataAdmin)