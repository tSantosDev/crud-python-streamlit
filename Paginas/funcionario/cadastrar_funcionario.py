import streamlit as st;
import controllers.funcionarioController as funcionarioController
import models.funcionario as funcionario


def cadastrar_funcionario():
    idAlteracao = st.experimental_get_query_params()
    funcionarioRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        funcionarioRecuperado = funcionarioController.selecionarIdFuncionario(idAlteracao)
        st.experimental_set_query_params(Id=funcionarioRecuperado.funcionario_id)
        st.title("Alterar Funcionario")
    else:
        st.title("Cadastrar Funcionario")

    with st.form(key="include_funcionario"):
        if funcionarioRecuperado == None:
            input_nome_funcionario = st.text_input(label="Nome Funcionário")
            input_CPF = st.text_input(label="CPF")
        else:
            input_nome_funcionario = st.text_input(label="Nome Funcionário", value=funcionarioRecuperado.nome_funcionario)
            input_CPF = st.text_input(label="CPF", value=funcionarioRecuperado.CPF)
        
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if funcionarioRecuperado == None:
            funcionario.funcionario_id = 0
            funcionario.nome_funcionario = input_nome_funcionario
            funcionario.CPF = input_CPF

            funcionarioController.incluirFuncionario(funcionario)
            st.success("Funcionário Incluido com Sucesso!")
        else:
            st.experimental_set_query_params()
            funcionario.funcionario_id = funcionarioRecuperado.funcionario_id
            funcionario.nome_funcionario = input_nome_funcionario
            funcionario.CPF = input_CPF

            funcionarioController.alterarFuncionario(funcionario)
            st.success("Funcionário Alterado com Sucesso!")