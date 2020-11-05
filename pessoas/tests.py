from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

def create_pessoa(cpf='11144477735', email='test@gmail.com'):
    return get_user_model().objects.create_user(
        cpf=cpf, 
        number='69999799051', 
        username=email, 
        first_name='Test', 
        last_name='User'
        )


class PessoasTest(APITestCase):

    '''
        Criando novas pessoas aparti do CPF
    '''
    def test_criar_pessoas(self):

        response = self.client.post('/pessoas/', data={
            'cpf': '00000000000000',
            'number': '69999799051',
            'username': 'test@gmail.com',
            'first_name': 'Test',
            'last_name': 'User',
        })

        pessoa = get_user_model().objects.last()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['cpf'], pessoa.cpf)
        self.assertEqual(response.data['first_name'], pessoa.first_name)
        self.assertEqual(response.data['last_name'], pessoa.last_name)
        self.assertEqual(response.data['number'], pessoa.number)
        self.assertEqual(response.data['username'], pessoa.username)


    def test_visualizar_pessoas(self):
        '''
            Visualizando registro de pessoas
        '''
        pessoas = [
            get_user_model().objects.create_user(
            cpf='00000000000000', number='69999799051', username='test@gmail.com', first_name='Test', last_name='User'),
            get_user_model().objects.create_user(
            cpf='00000000000002', number='69999799052', username='test2@gmail.com', first_name='Test2', last_name='User2')
        ]
        
        response = self.client.get('/pessoas/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        ids = [value.id for value in pessoas]
        ids_data = [data.get('id') for data in response.data]
        self.assertCountEqual(ids, ids_data)
    
    def test_atualizar_pessoa(self):
        '''
            Atualizando CPF pessoa
        '''
        user = create_pessoa()
        response = self.client.patch('/pessoas/'+str(user.id)+'/' , data={'cpf': '00000000000002'})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_deletar_pessoa(self):
        '''
            Deletando pessoa
        '''
        user = create_pessoa()
        response = self.client.delete('/pessoas/'+str(user.id)+'/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)