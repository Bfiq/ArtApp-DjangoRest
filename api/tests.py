from django.test import TestCase
from django.contrib.auth.models import User
from .models import Board, Pin
from rest_framework.test import APIClient #Simulación de peticiones Http
from rest_framework import status

class BoardTestCase(TestCase):
    def setUp(self): #función para preparar y configurar el entorno de prueba
        self.client = APIClient() #cliente de pruebas
        self.user = User.objects.create(username="TestUser")
        self.board = Board.objects.create(user=self.user, name="BoardTest", description="description test")

    #Testeando POST
    def testBoardCreation(self):
        response = self.client.post('/api/boards/', { #Simulando el post
            "user": self.user.id,
            "name": "Name Board Test Post",
            "description": "Description Board Test Post"
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 2)
        self.assertEqual(Board.objects.get(id=2).name, "Name Board Test Post")

    #Testeando GET
    def testGetBoard(self):
        response = self.client.get('/api/boards/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "BoardTest")

    #Testeando UPDATE
    def testUpdateBoard(self):
        response = self.client.patch(f'/api/boards/{self.board.id}/', {
            'name' : 'Update Name Board'
        }, format='json' )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.board.refresh_from_db() #Sincronizar la actualización
        self.assertEqual(self.board.name, "Update Name Board")

    #Testeando DELETE
    def testDeleteBoard(self):
        response = self.client.delete(f'/api/boards/{self.board.id}/')

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Board.objects.filter(id=self.board.id).exists())

class PintTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='test')
        self.pin = Pin.objects.create(user=self.user, title='pinTest', description='descriptionTest', imageUrl='http://api/bucket/image.jpg')

    def testGetPin(self):
        response = self.client.get('/api/pins/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pin.objects.count(), 1)
        self.assertEqual(response.data[0]["title"], "pinTest")

    def testPostPin(self):
        response = self.client.post('/api/pins/', {
            'user': self.user.id,
            'title': 'test',
            'description': 'test',
            'imageUrl': 'https://test.jpg'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pin.objects.count(), 2)
        self.assertEqual(Pin.objects.get(pk=2).title, "test")

    def testUpdatePin(self):
        response = self.client.patch(f'/api/pins/{self.pin.id}/', {
            'description':'test patch'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pin.refresh_from_db()
        self.assertEqual(Pin.objects.get(pk=1).description,"test patch")

