import streamlit as st;
import controllers.bombaController as bombaController
import Paginas.bomba.cadastrar_bomba as paginaCadastrarBomba


def consulta_bomba():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Bomba")   
        colunas = st.columns((1, 2, 2, 1.5))
        campos = ['Id Bomba', 'Id Combustível', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in bombaController.selecionarBomba():
            col1, col2, col3, col4 = st.columns((1, 2, 2, 1.5))
            col1.write(item.bomba_id)
            col2.write(item.combustivel_id)
            botao_espaco_excluir = col3.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.bomba_id))
            botao_espaco_alterar = col4.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.bomba_id))

            if botao_excluir:
                bombaController.excluirBomba(item.bomba_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.bomba_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.bomba_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarBomba.cadastrar_bomba()