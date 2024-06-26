from django.test import TestCase
from django.contrib.auth.models import User
from .models import Board, Pin, BoardPin
from rest_framework.test import APIClient, force_authenticate #Simulación de peticiones Http
from rest_framework import status

class BoardTestCase(TestCase):
    def setUp(self): #función para preparar y configurar el entorno de prueba
        self.user = User.objects.create(username="TestUser", password="12345")
        self.client = APIClient() #cliente de pruebas
        self.client.force_authenticate(user=self.user)
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
        self.user = User.objects.create(username="TestUser", password="12345")
        self.client = APIClient() #cliente de pruebas
        self.client.force_authenticate(user=self.user)
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

class BoardPinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="TestUser", password="12345")
        self.client = APIClient() #cliente de pruebas
        self.client.force_authenticate(user=self.user)
        self.board = Board.objects.create(user=self.user, name='test', description='test')
        self.pin = Pin.objects.create(user = self.user, title='test', description='test', imageUrl='http://api/bucket/image.jpg')
        self.pin2 = Pin.objects.create(user = self.user, title='test2', description='test', imageUrl='http://api/bucket/image2.jpg')
        self.pin3 = Pin.objects.create(user = self.user, title='test3', description='test', imageUrl='http://api/bucket/image3.jpg')
        self.boardPin = BoardPin.objects.create(boardFk=self.board, pinFk= self.pin)

    def testGetBoardPin(self):
        response = self.client.get('/api/board-pin/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['boardFk'], 1)

    def testPostBoardPin(self):
        response = self.client.post('/api/board-pin/', {
            'boardFk' : 1,
            'pinFk' : 2,
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BoardPin.objects.get(pk=2).pinFk.id, 2)
        self.assertEqual(BoardPin.objects.count(), 2)

    def testPatchBoardPin(self):
        response = self.client.patch(f'/api/board-pin/{self.boardPin.id}/', {
            'pinFk' : 3,
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.boardPin.refresh_from_db()
        self.assertEqual(BoardPin.objects.get(pk=self.boardPin.id).pinFk.id, 3)
