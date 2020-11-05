from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Empresas
from .serializers import EmpresasSerializer
from datetime import datetime


def create_pessoa():
    return get_user_model().objects.create_user(
        cpf='11144477735', 
        number='69999799051', 
        username='test@gmail.com', 
        first_name='Test', 
        last_name='User'
        )

def create_empresa(cnpj):
    return Empresas.objects.create(
        cnpj=cnpj, razao_social='Empresa Dona', data_abertura=datetime.strptime('01/01/2000', '%d/%m/%Y'), telefone='(00)0000-0000'
    )


class EmpresasTest(APITestCase):

    def test_criar_empresa(self):
        '''
            Criando registro Empresa
        '''
        response = self.client.post('/empresas/', data={
            'cnpj': '11.444.777/0001-61',
            'razao_social': 'Empresa Teste',
            'data_abertura': '29/07/1997',
            'telefone': '(00)0000-0000'
        })

        empresa_data = EmpresasSerializer(Empresas.objects.last()).data
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(empresa_data.get('cnpj'), response.data['cnpj'])
        self.assertEqual(empresa_data.get('razao_social'), response.data['razao_social'])
        self.assertEqual(empresa_data.get('data_abertura'), response.data['data_abertura'])
        self.assertEqual(empresa_data.get('telefone'), response.data['telefone'])
    
    def test_criar_e_associar_dono_pessoa_empresa(self):
        '''
            Criando registro Empresa e Associando ao Dono Pessoa
        '''

        pessoa = create_pessoa()
        response = self.client.post('/empresas/', data={
            'cnpj': '11.444.777/0001-61',
            'razao_social': 'Empresa Teste',
            'data_abertura': '29/07/1997',
            'telefone': '(00)0000-0000',
            'cpf_or_cnpj': pessoa.cpf,
        })

        empresa_data = EmpresasSerializer(Empresas.objects.last()).data
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(empresa_data.get('cnpj'), response.data['cnpj'])
        self.assertEqual(empresa_data.get('razao_social'), response.data['razao_social'])
        self.assertEqual(empresa_data.get('data_abertura'), response.data['data_abertura'])
        self.assertEqual(empresa_data.get('telefone'), response.data['telefone'])
        self.assertEqual(empresa_data.get('dono_pessoa'), pessoa.cpf)

    def test_criar_e_associar_dono_empresa_empresa(self):
        '''
            Criando registro Empresa e Associando ao Dono Empresa
        '''

        empresa = create_empresa(cnpj='13.860.893/0001-97')
        response = self.client.post('/empresas/', data={
            'cnpj': '11.444.777/0001-61',
            'razao_social': 'Empresa Teste',
            'data_abertura': '29/07/1997',
            'telefone': '(00)0000-0000',
            'cpf_or_cnpj': empresa.cnpj,
        })

        empresa_data = EmpresasSerializer(Empresas.objects.last()).data
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(empresa_data.get('cnpj'), response.data['cnpj'])
        self.assertEqual(empresa_data.get('razao_social'), response.data['razao_social'])
        self.assertEqual(empresa_data.get('data_abertura'), response.data['data_abertura'])
        self.assertEqual(empresa_data.get('telefone'), response.data['telefone'])
        self.assertEqual(empresa_data.get('dono_empresa'), empresa.cnpj)

    def test_visualizar_empresas(self):
        '''
            Visualizando registro de empresas
        '''
        empresas = [
            Empresas.objects.create(
            cnpj='00.000.000/0000-00', razao_social='Empresa Teste', data_abertura=datetime.strptime('01/01/2000', '%d/%m/%Y'), telefone='(00)0000-0000'),
            Empresas.objects.create(
            cnpj='00.000.000/0000-02', razao_social='Empresa Teste 2', data_abertura=datetime.strptime('01/01/2000', '%d/%m/%Y'), telefone='(00)0000-0002')
        ]
        
        response = self.client.get('/empresas/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        ids = [value.id for value in empresas]
        ids_data = [data.get('id') for data in response.data]
        self.assertCountEqual(ids, ids_data)
    
    def test_atualizar_empresa(self):
        '''
            Atualizando Razao Social empresa
        '''
        empresa = create_empresa(cnpj='00.000.000/0000-01')
        response = self.client.patch('/empresas/'+str(empresa.id)+'/' , data={'razao_social': 'Empresa Teste 2'})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_deletar_empresa(self):
        '''
            Deletando empresa
        '''
        empresa = create_empresa(cnpj='00.000.000/0000-02')
        response = self.client.delete('/empresas/'+str(empresa.id)+'/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)