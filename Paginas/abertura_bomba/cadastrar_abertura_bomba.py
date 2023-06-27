import streamlit as st;
import controllers.abertura_bombaController as abertura_bombaController
import models.abertura_bomba as abertura_bomba


def cadastrar_abertura_bomba():
    idAlteracao = st.experimental_get_query_params()
    abertura_bombaRecuperado = None
    if idAlteracao.get("Id") != None:
        idAlteracao = idAlteracao.get("Id")[0]
        abertura_bombaRecuperado = abertura_bombaController.selecionarIdAberturaBomba(idAlteracao)
        st.experimental_set_query_params(Id=abertura_bombaRecuperado.abertura_bomba_id)
        st.title("Alterar Abertura Bomba")
    else:
        st.title("Cadastrar Abertura de Bomba")

    with st.form(key="include_abertura_bomba"):
        if abertura_bombaRecuperado == None:
            input_bomba_id = st.number_input(label="Selecione o Id da Bomba", format="%d", step=1)
            input_funcionario_id = st.number_input(label="Selecione o Id do Funcionario", format="%d", step=1)
            input_valor_venda = st.number_input(label="Valor Venda", step=1.00)
        else:
            input_bomba_id = st.number_input(label="Selecione o Id da Bomba", step=1, value=abertura_bombaRecuperado.bomba_id)
            input_funcionario_id = st.number_input(label="Selecione o Id do Funcionario", step=1, value=abertura_bombaRecuperado.funcionario_id)            
            input_valor_venda = st.number_input(label="Valor Venda", step=1.00, value=abertura_bombaRecuperado.valor_venda)

        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if abertura_bombaRecuperado == None:
            abertura_bomba.abertura_bomba_id = 0
            abertura_bomba.bomba_id = input_bomba_id
            abertura_bomba.funcionario_id = input_funcionario_id
            abertura_bomba.valor_venda = input_valor_venda

            abertura_bombaController.incluirAberturaBomba(abertura_bomba)
            st.success("Abertura de Bomba Incluida com Sucesso!")
        else:
            st.experimental_set_query_params()
            abertura_bomba.abertura_bomba_id = abertura_bombaRecuperado.abertura_bomba_id
            abertura_bomba.bomba_id = input_bomba_id
            abertura_bomba.funcionario_id = input_funcionario_id
            abertura_bomba.valor_venda = input_valor_venda

            abertura_bombaController.alterarAberturaBomba(abertura_bomba)
            st.success("Abertura de Bomba Alterada com Sucesso!")