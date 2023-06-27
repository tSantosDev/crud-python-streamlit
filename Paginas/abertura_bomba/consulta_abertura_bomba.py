import streamlit as st;
import controllers.abertura_bombaController as abertura_bombaController
import Paginas.abertura_bomba.cadastrar_abertura_bomba as paginaCadastrarAbertura_bomba

def consulta_abertura_bomba():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Abertura de Bomba")   
        colunas = st.columns((0.5, 1.5, 1, 1, 1))
        campos = ['Id', 'Id Bomba', 'Id Funcionario', 'Valor Venda', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in abertura_bombaController.selecionarAberturaBomba():
            col1, col2, col3, col4, col5 = st.columns((0.5, 1.5, 1, 1, 1))
            col1.write(item.abertura_bomba_id)
            col2.write(item.bomba_id)
            col3.write(item.funcionario_id)
            col4.write(item.valor_venda)
            botao_espaco_alterar = col5.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.abertura_bomba_id))

            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.abertura_bomba_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarAbertura_bomba.cadastrar_abertura_bomba()