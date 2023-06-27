import streamlit as st;
import controllers.abastecimentoController as abastecimentoController
import models.abastecimento as abastecimento


def cadastrar_abastecimento():
    idAlteracao = st.experimental_get_query_params()
    abastecimentoRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        abastecimentoRecuperado = abastecimentoController.selecionarIdAbastecimento(idAlteracao)
        st.experimental_set_query_params(Id=abastecimentoRecuperado.abastecimento_id)
        st.title("Alterar Abastecimento")
    else:
        st.title("Cadastrar Abastecimento")

    with st.form(key="include_abastecimento"):
        if abastecimentoRecuperado == None:
            input_combustivel_id = st.number_input(label="Id Combustível", step=1)
            input_quantidade_abastecimento = st.number_input(label="Quantidade a ser abastecida", step=15.00)
        else:
            input_combustivel_id = st.number_input(label="Id Combustível", step=1, value=abastecimentoRecuperado.combustivel_id)
            input_quantidade_abastecimento = st.number_input(label="Quantidade a ser abastecida", step=15.00, value=abastecimentoRecuperado.quantidade_abastecimento)
        
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if abastecimentoRecuperado == None:
            abastecimento.abastecimento_id = 0
            abastecimento.combustivel_id = input_combustivel_id
            abastecimento.quantidade_abastecimento = input_quantidade_abastecimento

            abastecimentoController.incluirAbastecimento(abastecimento)
            st.success("Abastecimento Incluido com Sucesso!")
        else:
            st.experimental_set_query_params()
            abastecimento.abastecimento_id = abastecimentoRecuperado.abastecimento_id
            abastecimento.combustivel_id = input_combustivel_id
            abastecimento.quantidade_abastecimento = input_quantidade_abastecimento

            abastecimentoController.alterarAbastecimento(abastecimento)
            st.success("Abastecimento Alterado com Sucesso!")