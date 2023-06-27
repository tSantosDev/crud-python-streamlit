import streamlit as st;
import controllers.fornecedorController as fornecedorController
import models.fornecedor as fornecedor


def cadastrar_fornecedor():
    idAlteracao = st.experimental_get_query_params()
    fornecedorRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        fornecedorRecuperado = fornecedorController.selecionarIdFornecedor(idAlteracao)
        st.experimental_set_query_params(Id=fornecedorRecuperado.fornecedor_id)
        st.title("Alterar Fornecedor")
    else:
        st.title("Cadastrar Fornecedor")

    with st.form(key="include_fornecedor"):
        if fornecedorRecuperado == None:
            input_nome_fornecedor = st.text_input(label="Nome Fornecedor")
            input_CNPJ = st.text_input(label="CNPJ")
        else:
            input_nome_fornecedor = st.text_input(label="Nome Fornecedor", value=fornecedorRecuperado.nome_fornecedor)
            input_CNPJ = st.text_input(label="CNPJ", value=fornecedorRecuperado.CNPJ)
        
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if fornecedorRecuperado == None:
            fornecedor.fornecedor_id = 0
            fornecedor.nome_fornecedor = input_nome_fornecedor
            fornecedor.CNPJ = input_CNPJ

            fornecedorController.incluirFornecedor(fornecedor)
            st.success("Fornecedor Incluido com Sucesso!")
        else:
            st.experimental_set_query_params()
            fornecedor.fornecedor_id = fornecedorRecuperado.fornecedor_id
            fornecedor.nome_fornecedor = input_nome_fornecedor
            fornecedor.CNPJ = input_CNPJ

            fornecedorController.alterarFornecedor(fornecedor)
            st.success("Fornecedor Alterado com Sucesso!")