from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import Paginas.combustivel.cadastrar_combustivel as paginaCadastrarCombustivel
import Paginas.combustivel.consulta_combustivel as paginaConsultaCombustivel
import Paginas.fornecedor.cadastrar_fornecedor as paginaCadastrarFornecedor
import Paginas.fornecedor.consulta_fornecedor as paginaConsultaFornecedor
import Paginas.funcionario.consulta_funcionario as paginaConsultaFuncionario
import Paginas.funcionario.cadastrar_funcionario as paginaCadastrarFuncionario
import Paginas.bomba.cadastrar_bomba as paginaCadastrarBomba
import Paginas.bomba.consulta_bomba as paginaConsultaBomba
import Paginas.abertura_bomba.cadastrar_abertura_bomba as paginaCadastrarAberturaBomba
import Paginas.abertura_bomba.consulta_abertura_bomba as paginaConsultaAberturaBomba
import Paginas.venda.cadastrar_venda as paginaCadastrarVenda
import Paginas.venda.consulta_venda as paginaConsultaVenda
import Paginas.abastecimento.cadastrar_abastecimento as paginaCadastrarAbastecimento
import Paginas.abastecimento.consulta_abastecimento as paginaConsultaAbastecimento

st.sidebar.title("Menu")
pagina_posto =  st.sidebar.selectbox('Posto de Gasolina', ['Cadastrar Combustível', 'Consultar Cadastro Combustível',
'Cadastrar Fornecedor', 'Consultar Cadastro Fornecedor', 'Cadastrar Funcionário', 'Consultar Cadastro Funcionário',
'Cadastrar Bomba', 'Consultar Cadastro Bomba', 'Cadastrar Abertura de Bomba', 'Consultar Cadastro Abertura de Bomba',
'Cadastrar Venda', 'Consultar Cadastro Venda', 'Cadastrar Abastecimento', 'Consultar Cadastro Abastecimento'])

#------------Tabela Combustivel------------------

if pagina_posto == 'Consultar Cadastro Combustível':
    paginaConsultaCombustivel.consulta_combustivel()


if pagina_posto == 'Cadastrar Combustível':
    st.experimental_set_query_params()
    paginaCadastrarCombustivel.cadastrar_combustivel()

#--------------------------------------------------

#------------Tabela Fornecedor------------------

if pagina_posto == 'Consultar Cadastro Fornecedor':
    paginaConsultaFornecedor.consulta_fornecedor()


if pagina_posto == 'Cadastrar Fornecedor':
    st.experimental_set_query_params()
    paginaCadastrarFornecedor.cadastrar_fornecedor()    

#--------------------------------------------------

#------------Tabela Fornecedor------------------

if pagina_posto == 'Consultar Cadastro Funcionário':
    paginaConsultaFuncionario.consulta_funcionario()

if pagina_posto == 'Cadastrar Funcionário':
    paginaCadastrarFuncionario.cadastrar_funcionario()    

#--------------------------------------------------

#------------Tabela Bomba------------------

if pagina_posto == 'Consultar Cadastro Bomba':
    paginaConsultaBomba.consulta_bomba()

if pagina_posto == 'Cadastrar Bomba':
    paginaCadastrarBomba.cadastrar_bomba() 

#--------------------------------------------------

#------------Tabela Abertura de Bomba------------------

if pagina_posto == 'Consultar Cadastro Abertura de Bomba':
    paginaConsultaAberturaBomba.consulta_abertura_bomba()

if pagina_posto == 'Cadastrar Abertura de Bomba':
    paginaCadastrarAberturaBomba.cadastrar_abertura_bomba()

#--------------------------------------------------

#------------Tabela Venda------------------

if pagina_posto == 'Consultar Cadastro Venda':
    paginaConsultaVenda.consulta_venda()

if pagina_posto == 'Cadastrar Venda':
    paginaCadastrarVenda.cadastrar_venda()

#--------------------------------------------------

#------------Tabela Abastecimento------------------

if pagina_posto == 'Consultar Cadastro Abastecimento':
    paginaConsultaAbastecimento.consulta_abastecimento()

if pagina_posto == 'Cadastrar Abastecimento':
    paginaCadastrarAbastecimento.cadastrar_abastecimento()

#--------------------------------------------------