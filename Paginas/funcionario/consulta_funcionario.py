import streamlit as st;
import controllers.funcionarioController as funcionarioController
import Paginas.funcionario.cadastrar_funcionario as paginaCadastrarFuncionario


def consulta_funcionario():
    parametroId = st.experimental_get_query_params()
    if parametroId.get("Id") == None:
        st.experimental_set_query_params()
        st.title("Consultar Funcionário")   
        colunas = st.columns((1, 2, 2, 1, 1.5))
        campos = ['Id', 'Nome Funcionário', 'CPF', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in funcionarioController.selecionarFuncionario():
            col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1.5))
            col1.write(item.funcionario_id)
            col2.write(item.nome_funcionario)
            col3.write(item.CPF)
            botao_espaco_excluir = col4.empty()
            botao_excluir = botao_espaco_excluir.button('Excluir', 'btnExcluir' + str(item.funcionario_id))
            botao_espaco_alterar = col5.empty()
            botao_alterar = botao_espaco_alterar.button('Alterar', 'btnAlterar' + str(item.funcionario_id))

            if botao_excluir:
                funcionarioController.excluirFuncionario(item.funcionario_id)
                botao_espaco_excluir.button('Excluído', 'btnExcluir1' + str(item.funcionario_id))
            if botao_alterar:
                st.experimental_set_query_params(
                    Id=[item.funcionario_id]
                )
                st.experimental_rerun()
    else:
        botaoVoltar = st.button("Voltar")
        if botaoVoltar:
            st.experimental_set_query_params()
            st.experimental_rerun()

        paginaCadastrarFuncionario.cadastrar_funcionario()