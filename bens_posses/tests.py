from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from pessoas.tests import create_pessoa
from .models import BensPosses


def create_bens_posses():
    responsavel = create_pessoa()
    return BensPosses.objects.create(
        bens='Lorem Ipsum is simply dummy text of the printing and typesetting industry', 
        posses='Lorem Ipsum is simply dummy text of the printing and typesetting industry', 
        responsavel=responsavel)


class BensPossesTest(APITestCase):

    def test_criar_bens_posses(self):
        '''
            Criando registro de Bens e Posses
        '''
        responsavel = create_pessoa()
        response = self.client.post('/bens_posses/', data={
            'bens': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
            'posses': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
            'responsavel': responsavel.id
        })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(responsavel.id, response.data['responsavel'])
    
    def test_visualizar_bens_posses(self):
        '''
            Visualizando registro de Bens e Posses
        '''
        responsavel1 = create_pessoa(cpf='61672006023', email='responsavel1@gmail.com')
        responsavel2 = create_pessoa(cpf='67393096048', email='responsavel2@gmail.com')

        bens_posses = [
            BensPosses.objects.create(bens='Lorem Ipsum is simply dummy text of the printing and typesetting industry',\
                posses='Lorem Ipsum is simply dummy text of the printing and typesetting industry',\
                responsavel=responsavel1),
            BensPosses.objects.create(bens='Lorem Ipsum is simply dummy text of the printing and typesetting industry',\
                posses='Lorem Ipsum is simply dummy text of the printing and typesetting industry',\
                responsavel=responsavel2)
        ]
        
        response = self.client.get('/bens_posses/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        ids = [value.id for value in bens_posses]
        ids_data = [data.get('id') for data in response.data]
        self.assertCountEqual(ids, ids_data)
    
    def test_atualizar_bens_posses(self):
        '''
            Atualizando Responsavel pelos Bens
        '''
        responsavel = create_pessoa(cpf='26529669019', email='responsavel3@gmail.com')
        bens_posses = create_bens_posses()
        response = self.client.patch('/bens_posses/'+str(bens_posses.id)+'/' , data={'responsavel': responsavel.id})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_deletar_pessoa(self):
        '''
            Deletando registro Bens e Posses
        '''
        bens_posses = create_bens_posses()
        response = self.client.delete('/bens_posses/'+str(bens_posses.id)+'/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)