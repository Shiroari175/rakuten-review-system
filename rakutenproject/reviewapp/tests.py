from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse

# Create your tests here.
# 実行
# python manage.py test
# python manage.py test myapp.tests.HelloWorldViewTest.test_hello_world_view


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



