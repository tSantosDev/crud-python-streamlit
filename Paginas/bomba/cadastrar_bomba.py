import streamlit as st;
import controllers.bombaController as bombaController
import models.bomba as bomba


def cadastrar_bomba():
    idAlteracao = st.experimental_get_query_params()
    bombaRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        bombaRecuperado = bombaController.selecionarIdBomba(idAlteracao)
        st.experimental_set_query_params(Id=bombaRecuperado.bomba_id)
        st.title("Alterar Bomba")
    else:
        st.title("Cadastrar Bomba")

    with st.form(key="include_bomba"):
        if bombaRecuperado == None:
            input_combustivel_id = st.number_input(label="Id Combustível", format="%d", step=1)
        else:
            input_combustivel_id = st.number_input(label="Id Combustível", step=1, value=bombaRecuperado.combustivel_id)
        
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if bombaRecuperado == None:
            bomba.bomba_id = 0
            bomba.combustivel_id = input_combustivel_id

            bombaController.incluirBomba(bomba)
            st.success("Bomba Incluido com Sucesso!")
        else:
            st.experimental_set_query_params()
            bomba.bomba_id = bombaRecuperado.bomba_id
            bomba.combustivel_id = input_combustivel_id

            bombaController.alterarBomba(bomba)
            st.success("Bomba Alterada com Sucesso!")