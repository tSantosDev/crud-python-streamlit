import streamlit as st;
import controllers.vendaController as vendaController
import models.venda as venda


def cadastrar_venda():
    idAlteracao = st.experimental_get_query_params()
    vendaRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        vendaRecuperado = vendaController.selecionarIdVenda(idAlteracao)
        st.experimental_set_query_params(Id=vendaRecuperado.venda_id)
        st.title("Alterar Venda")
    else:
        st.title("Cadastrar Venda")

    with st.form(key="include_venda"):
        if vendaRecuperado == None:
            input_bomba_id = st.number_input(label="Id Bomba", format="%d", step=1)
            input_combustivel_id = st.number_input(label="Id Combustível", format = "%d", step=1)
            input_quantidade_venda = st.number_input(label="Quantidade", step=15.00)
        else:
            input_bomba_id = st.number_input(label="Id Bomba", step=1, value=vendaRecuperado.bomba_id)
            input_combustivel_id = st.number_input(label="Id Combustível", step=1, value=vendaRecuperado.combustivel_id)
            input_quantidade_venda = st.number_input(label="Quantidade", step=15.00, value=vendaRecuperado.quantidade_venda)
        
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if vendaRecuperado == None:
            venda.venda_id = 0
            venda.bomba_id = input_bomba_id
            venda.combustivel_id = input_combustivel_id
            venda.quantidade_venda = input_quantidade_venda

            vendaController.incluirVenda(venda)
            st.success("Venda Incluida com Sucesso!")
        else:
            st.experimental_set_query_params()
            venda.venda_id = vendaRecuperado.venda_id
            venda.bomba_id = input_bomba_id
            venda.combustivel_id = input_combustivel_id
            venda.quantidade_venda = input_quantidade_venda

            vendaController.alterarVenda(venda)
            st.success("Venda Alterado com Sucesso!")