import streamlit as st;
import controllers.abastecimentoController as abastecimentoController
import Paginas.abastecimento.cadastrar_abastecimento as paginaCadastrarAbastecimento


def consulta_abastecimento():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Abastecimento")
        colunas = st.columns((2, 1.5, 2, 1.5, 1.5))
        campos = ['Id Abastecimento', 'Id Combustível', 'Quantidade', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in abastecimentoController.selecionarAbastecimento():
            col1, col2, col3, col4, col5 = st.columns((2, 1.5, 2, 1.5, 1.5))
            col1.write(item.abastecimento_id)
            col2.write(item.combustivel_id)
            col3.write(item.quantidade_abastecimento)
            botao_espaco_excluir = col4.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.abastecimento_id))
            botao_espaco_alterar = col5.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.abastecimento_id))

            if botao_excluir:
                abastecimentoController.excluirAbastecimento(item.abastecimento_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.abastecimento_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.abastecimento_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarAbastecimento.cadastrar_abastecimento()