import streamlit as st;
import controllers.vendaController as vendaController
import Paginas.venda.cadastrar_venda as paginaCadastrarVenda


def consulta_venda():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Venda")   
        colunas = st.columns((1, 2, 2, 2, 1, 1.5))
        campos = ['Id', 'Id Bomba', 'Id Combustivel', 'Quantidade Venda', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in vendaController.selecionarVenda():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 2, 2, 1, 1.5))
            col1.write(item.venda_id)
            col2.write(item.bomba_id)
            col3.write(item.combustivel_id)
            col4.write(item.quantidade_venda)
            botao_espaco_excluir = col5.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.venda_id))
            botao_espaco_alterar = col6.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.venda_id))

            if botao_excluir:
                vendaController.excluirVenda(item.venda_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.venda_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.venda_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarVenda.cadastrar_venda()