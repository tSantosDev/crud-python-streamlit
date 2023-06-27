import streamlit as st;
import controllers.fornecedorController as fornecedorController
import Paginas.fornecedor.cadastrar_fornecedor as paginaCadastrarFornecedor


def consulta_fornecedor():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Fornecedor")   
        colunas = st.columns((1, 2, 2, 1, 1.5))
        campos = ['Id', 'Nome Fornecedor', 'CNPJ', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in fornecedorController.selecionarFornecedor():
            col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1.5))
            col1.write(item.fornecedor_id)
            col2.write(item.nome_fornecedor)
            col3.write(item.CNPJ)
            botao_espaco_excluir = col4.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.fornecedor_id))
            botao_espaco_alterar = col5.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.fornecedor_id))

            if botao_excluir:
                fornecedorController.excluirFornecedor(item.fornecedor_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.fornecedor_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.fornecedor_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarFornecedor.cadastrar_fornecedor()