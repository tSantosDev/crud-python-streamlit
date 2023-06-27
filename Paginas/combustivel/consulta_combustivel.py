import streamlit as st;
import controllers.combustivelController as combustivelController
import Paginas.combustivel.cadastrar_combustivel as paginaCadastrarCombustivel


def consulta_combustivel():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Combustível")   
        colunas = st.columns((0.5, 1.5, 1, 1, 1.5, 1, 1, 1))
        campos = ['Id', 'Nome Combus.', 'Estoque', 'Preço Venda', 'Preço Comp.', 'Id Forn.', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in combustivelController.selecionarCombustivel():
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((0.5, 1.5, 1, 1, 1.5, 1, 1, 1))
            col1.write(item.combustivel_id)
            col2.write(item.nome_combustivel)
            col3.write(item.estoque)
            col4.write(item.preco_venda)
            col5.write(item.preco_compra)
            col6.write(item.fornecedor_id)
            botao_espaco_excluir = col7.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.combustivel_id))
            botao_espaco_alterar = col8.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.combustivel_id))

            if botao_excluir:
                combustivelController.excluirCombustivel(item.combustivel_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.combustivel_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.combustivel_id]
                )
                st.experimental_rerun()

    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarCombustivel.cadastrar_combustivel()
