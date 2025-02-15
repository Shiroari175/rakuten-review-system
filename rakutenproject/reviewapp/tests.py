from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse

# Create your tests here.
# 実行
# python manage.py test
# python manage.py test myapp.tests.HelloWorldViewTest.test_hello_world_view

# 1.Client を使ってDjangoのテストクライアントを作成し、HTTPリクエストをシミュレートします。
# 2.reverse('hello_world') を使って、hello_worldビューへのURLを取得します。urls.pyでこのビューに対応するURLパターンが定義されていることを確認してください。
# 3.self.assertEqual(response.status_code, 200) を使って、レスポンスのHTTPステータスコードが200（成功）であることを確認します。
# 4.self.assertContains(response, '<h2>hello world from Review_app!!!</h2>') を使って、レスポンスの内容に特定の文字列が含まれていることを確認します。


class HelloWorldViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>hello world from Review_app!!!</h2>')


#
# class MyModelTest(TestCase):
#     def setUp(self):
#         # テストの前に実行されるセットアップコード
#         MyModel.objects.create(name="Test Name")
#
#     def test_name_field(self):
#         # モデルのnameフィールドが正しく保存されているかをテスト
#         item = MyModel.objects.get(name="Test Name")
#         self.assertEqual(item.name, "Test Name")



