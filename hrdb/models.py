from django.db import models
# accountsアプリのmodelsモジュールから、CustomUserをインポート
from accounts.models import CustomUser
from django.urls import reverse
from datetime import datetime as dt
from email.policy import default

class Occupation(models.Model):
    '''モデルクラス、職種
    '''
    class Meta:
        verbose_name = "職種名"
        verbose_name_plural = "職種名"

    # 作成者
    author = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT
        )
    # 職種名 (大学教員、高校教員、大学職員、高校職員、自治体職員、歯科医師など)
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='職種名',
        # 最大文字数は200
        max_length=200
        )
    #　仕事内容
    summary = models.TextField(
        # フィールドのタイトル
        verbose_name='仕事内容'    
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):職種
        '''
        return self.name

class Org(models.Model):
    '''モデルクラス、所属
    '''
    class Meta:
        verbose_name = "組織名"
        verbose_name_plural = "所属組織名"
    # 作成者
    author = models.ForeignKey(
            CustomUser,
            # フィールドのタイトル
            verbose_name='作成者',
            # 関連づけられているものがあると削除不可
            on_delete=models.PROTECT
        )
    # 所属名
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='所属名',       
        # 最大文字数は100
        max_length=100
        )
    # ホームページURL
    url = models.URLField(
        # フィールドのタイトル
        verbose_name='ホームページ'
        )       

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):所属名
        '''
        return self.name

class Title(models.Model):
    '''モデルクラス、肩書
    '''
    class Meta:
        verbose_name = "肩書"
        verbose_name_plural = "肩書"
    # 作成者
    author = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT
        )
    # 肩書名 (漫画家、アニメーター、DXエバンジェリスト、経営者、実業家等)
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='肩書名',       
        # 最大文字数は100
        max_length=100
        ) 

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):対価の種別名
        '''
        return self.name

class Persondata(models.Model):
    '''モデルクラス、人物情報
    '''
    class Meta:
        db_table = 'person_data'
        verbose_name = "人物情報"
        verbose_name_plural = "人物情報"

    # 作成者情報
    author = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT
        )
	# 人物情報名
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='名前', 
        # 最大文字数は200
        max_length=200
        )
    # 性別
    gender = models.CharField(
        # フィールドのタイトル
        verbose_name='性別', 
        # 最大文字数は10
        max_length=10,
        default=u'未回答',
        )
    # 現在の仕事内容
    summary = models.TextField(
        # フィールドのタイトル
        verbose_name='現在の仕事内容'
        )
    # 職種
    occupation = models.ForeignKey(
        # Occupationモデルを呼び出す
        Occupation,
        # フィールドのタイトル
        verbose_name = '職種名',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT,
        )
    # 肩書名
    title = models.ForeignKey(
        # Occupationモデルを呼び出す
        Title,
        # フィールドのタイトル
        verbose_name = '肩書名',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT,
        # 未入力を認める
        null=True,
        blank=True
        )
    # 所属名
    org = models.ForeignKey(
        # Orgモデルを呼び出す
        Org,
        # フィールドのタイトル
        verbose_name = '所属名',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT
        )
    # 協力できること
    collabat = models.TextField(
        # フィールドのタイトル
        verbose_name='協力できること'
        )
    # 専門領域
    specialat = models.TextField(
        # フィールドのタイトル
        verbose_name='専門領域'
        )
    # 興味関心
    interest = models.TextField(
        # フィールドのタイトル
        verbose_name='興味関心'
        )
    # 連絡用のSNS URL
    snsurl = models.CharField(
        # フィールドのタイトル
        verbose_name='連絡用SNS_URL',
        max_length=100,
        null=True
        )
    # 登録日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='登録日時',
        # 日時を自動追加
        auto_now_add=True       
        )
    # 更新日時のフィールド
    updated_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='更新日時',
        # 日時を自動追加
        auto_now=True     
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):人物情報
        '''
        return self.name

    @staticmethod
    def get_absolute_url(self):
        return reverse('monitor:index')

class Resulttype(models.Model):
    '''モデルクラス、実績の種別
    '''
    class Meta:
        verbose_name = "実績の種別"
        verbose_name_plural = "実績の種別"

    # 作成者
    author = models.ForeignKey(
            CustomUser,
            # フィールドのタイトル
            verbose_name='作成者',
            # 関連づけられているものがあると削除不可
            on_delete=models.PROTECT
        )
    # 実績の種別
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='実績の種別',       
        max_length=200
        )             

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):実績の種別
        '''
        return self.name

class Resultdata(models.Model):
    '''モデル、実績、著書、執筆歴、開発実績など
    '''
    class Meta:
        db_table = 'result_data'
        verbose_name = "実績情報"
        verbose_name_plural = "実績情報"

    # 作成者
    author = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT,
        # CustomUserが親でCarrerDataが子の関係となる
        related_name='sub_author'
        )
    # 人物情報
    persondata = models.ForeignKey(
        Persondata,
        # フィールドのタイトル
        verbose_name='人物情報',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT,
        # Persondataが親でResultdataが子の関係となる
        related_name='sub_persondata'
        )
    # 実績の種別
    resulttype = models.ForeignKey(
        # 実績の種別モデルを呼び出す
        Resulttype,
        # フィールドのタイトル
        verbose_name = '実績の種別',
        # 関連づけられているものがあると削除不可
        on_delete=models.PROTECT,
        # Resulttypeが親でResultdataが子の関係となる
        related_name='sub_resulttype'
        )
    # 実績概要
    name = models.CharField(
        # フィールドのタイトル
        verbose_name='実績概要(200文字以内)', 
        max_length=200  
        )
    # 実績詳細
    event = models.TextField(
        # フィールドのタイトル
        verbose_name='実績詳細'    
        )
    # 登録日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='登録日時',
        # 日時を自動追加
        auto_now_add=True       
        )
    # 更新日時のフィールド
    updated_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='更新日時',
        # 日時を自動追加
        auto_now=True     
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):実績情報
        '''
        return self.persondata.name + ":" + str(self.name)