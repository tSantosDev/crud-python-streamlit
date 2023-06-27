import streamlit as st;
import controllers.combustivelController as combustivelController
import models.combustivel as combustivel


def cadastrar_combustivel():
    idAlteracao = st.experimental_get_query_params()
    combustivelRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        combustivelRecuperado = combustivelController.selecionarIdCombustivel(idAlteracao)
        st.experimental_set_query_params(Id=combustivelRecuperado.combustivel_id)
        st.title("Alterar Combustível")
    else:
        st.title("Cadastrar Combustível")

    with st.form(key="include_combustivel"):
        if combustivelRecuperado == None:
            input_nome = st.text_input(label="Nome Combustível")
            input_estoque = st.number_input(label="Estoque", step=15.00)
            input_preco_venda = st.number_input(label="Preço de Venda", step=1.00)
            input_preco_compra = st.number_input(label="Preço de Compra", step=1.00)
            input_fornecedor_id = st.number_input(label="Selecione o Identificador do Fornecedor", format="%d", step=1)
        else:
            input_nome = st.text_input(label="Nome Combustível", value=combustivelRecuperado.nome_combustivel)
            input_estoque = st.number_input(label="Estoque", step=15.00, value=combustivelRecuperado.estoque)
            input_preco_venda = st.number_input(label="Preço de Venda", step=1.00, value=combustivelRecuperado.preco_venda)
            input_preco_compra = st.number_input(label="Preço de Compra", step=1.00, value=combustivelRecuperado.preco_compra)
            input_fornecedor_id = st.number_input(label="Selecione o Identificador do Fornecedor", step=1, value=combustivelRecuperado.fornecedor_id)

        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if combustivelRecuperado == None:
            combustivel.combustivel_id = 0
            combustivel.nome_combustivel = input_nome
            combustivel.estoque = input_estoque
            combustivel.preco_venda = input_preco_venda
            combustivel.preco_compra = input_preco_compra
            combustivel.fornecedor_id = input_fornecedor_id

            combustivelController.incluirCombustivel(combustivel)
            st.success("Combustível Incluido com Sucesso!")
        else:
            st.experimental_set_query_params()
            combustivel.combustivel_id = combustivelRecuperado.combustivel_id
            combustivel.nome_combustivel = input_nome
            combustivel.estoque = input_estoque
            combustivel.preco_venda = input_preco_venda
            combustivel.preco_compra = input_preco_compra
            combustivel.fornecedor_id = input_fornecedor_id

            combustivelController.alterarCombustivel(combustivel)
            st.success("Combustível Alterado com Sucesso!")