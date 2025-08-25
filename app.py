import pandas as pd
import plotly.express as px
import streamlit as st

def criar_tabela_agrupada(coluna1, coluna2):
    tabela = pd.DataFrame(df_filtrado.groupby(coluna1)[coluna2].value_counts()).sort_values(by=[coluna1,coluna2], ascending=False).reset_index()
    tabela.columns = [coluna1, coluna2, 'Frequência']
    return tabela

# Configurações da Página
st.set_page_config(
    page_title="Análise de Qualidade do Sono", 
    layout="wide",
    page_icon="🛌")

# Importando os Dados
df = pd.read_csv('https://raw.githubusercontent.com/celsorma102/analise-sono/refs/heads/main/dataset/dataset_traduzido.csv')

st.sidebar.header("Filtros")

# Filtros
genero_disponivel = sorted(df['Gênero'].unique())
genero_selecionado = st.sidebar.multiselect("Selecione o Gênero", genero_disponivel,default=genero_disponivel)

idade_disponivel = sorted(df['Idade'].unique())
idade_selecionada = st.sidebar.multiselect("Selecione a Idade", idade_disponivel,default=idade_disponivel)

profissao_disponivel = sorted(df['Profissão'].unique())
profissao_selecionada = st.sidebar.multiselect("Selecione a Profissão", profissao_disponivel,default=profissao_disponivel)

imc_disponivel = sorted(df['Categoria de IMC'].unique())
imc_selecionado = st.sidebar.multiselect("Selecione a Categoria de IMC", imc_disponivel,default=imc_disponivel)

disturbio_disponivel = sorted(df['Tipo de Distúrbio'].unique())
disturbio_selecionado = st.sidebar.multiselect("Selecione o Tipo de Distúrbio", disturbio_disponivel,default=disturbio_disponivel)

qualidade_sono_disponivel = sorted(df['Qualidade do Sono'].unique())
qualidade_sono_selecionada = st.sidebar.multiselect("Selecione a Qualidade do Sono", qualidade_sono_disponivel,default=qualidade_sono_disponivel)

# Gerar o DataFrame para os filtros selecionados
df_filtrado = df[
    (df['Gênero'].isin(genero_selecionado)) &
    (df['Idade'].isin(idade_selecionada)) &
    (df['Profissão'].isin(profissao_selecionada)) &
    (df['Categoria de IMC'].isin(imc_selecionado)) &
    (df['Tipo de Distúrbio'].isin(disturbio_selecionado)) &
    (df['Qualidade do Sono'].isin(qualidade_sono_selecionada))
]

# ítulos e Descrições
st.title("🛌 Análise de Qualidade do Sono")
st.markdown("Análise interativa dos dados de sono coletados em um estudo recente.")

st.subheader("Visão Geral dos Dados")

# Lógica dos KPIs
if df_filtrado.empty:
    st.write("Nenhum dado disponível para os filtros selecionados.")
else:
    total_registro = df_filtrado.shape[0]
    idade_media = df_filtrado['Idade'].mean()
    estresse_medio = df_filtrado['Nível de Estresse'].mean()
    qualidade_sono_media = df_filtrado['Qualidade do Sono'].mean()
    duracao_media = df_filtrado['Duração do Sono'].mean()
    profissao_mais_frequente = df_filtrado['Profissão'].mode()[0]

# KPIs
col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Total de Registros", f"{total_registro}")
col2.metric("Profissão Mais Frequente", f"{profissao_mais_frequente}")
col3.metric("Idade Média", f"{idade_media:.0f} anos")
col4.metric("Estresse Médio", f"{estresse_medio:.1f}")
col5.metric("Qualidade do Sono Média", f"{qualidade_sono_media:.1f}")
col6.metric("Duração do Sono Média", f"{duracao_media:.1f} horas")

st.markdown("---")

# Gráficos
st.subheader("Gráficos")

# Linha 1
col_graf1, col_graf2 = st.columns(2)

profissao_disturbio = criar_tabela_agrupada('Profissão', 'Tem Disturbio')

with col_graf1:
    if not df_filtrado.empty:
        fig1 = px.bar(profissao_disturbio, y="Profissão", x="Frequência", color="Tem Disturbio", barmode="overlay", orientation='h')
        fig1.update_layout(title="Distribuição de Distúrbios do Sono por Profissão", xaxis_title="Profissão", yaxis_title="Contagem")
        st.plotly_chart(fig1)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

with col_graf2:
    if not df_filtrado.empty:
        fig2 = px.histogram(df_filtrado, x="Idade", color="Gênero", barmode="overlay")
        fig2.update_layout(title="Distribuição da Idade por Gênero")
        st.plotly_chart(fig2)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

# Linha 2
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        fig3 = px.box(df_filtrado, x="Gênero", y="Duração do Sono", color="Gênero")
        fig3.update_layout(title="Duração do Sono por Gênero")
        st.plotly_chart(fig3)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

with col_graf4:
    if not df_filtrado.empty:
        fig4 = px.violin(df_filtrado, x="Tipo de Distúrbio", y="Nível de Estresse", color="Tipo de Distúrbio")
        fig4.update_layout(title="Nível de Estresse por Tipo de Distúrbio")
        st.plotly_chart(fig4)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

# Linha 3
col_graf5, col_graf6 = st.columns(2)

with col_graf5:
    if not df_filtrado.empty:
        fig5 = px.scatter(df_filtrado, x="Duração do Sono", y="Nível de Estresse", color="Gênero", trendline="ols")
        fig5.update_layout(title="Relação entre Duração do Sono e Nível de Estresse")
        st.plotly_chart(fig5)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

tipo_disturbio = criar_tabela_agrupada('Tipo de Distúrbio', 'Tem Disturbio')

with col_graf6:
    if not df_filtrado.empty:
        fig6 = px.pie(tipo_disturbio, names="Tipo de Distúrbio", values="Frequência", title="Distribuição dos Tipos de Distúrbio")
        st.plotly_chart(fig6)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

# Linha 4
col_graf7, col_graf8 = st.columns(2)

with col_graf7:
    if not df_filtrado.empty:
        fig7 = px.histogram(df_filtrado, x="Tipo de Distúrbio", color="Gênero", barmode="overlay")
        fig7.update_layout(title="Distribuição dos Tipos de Distúrbio por Gênero")
        st.plotly_chart(fig7)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

with col_graf8:
    if not df_filtrado.empty:
        fig8 = px.box(df_filtrado, x="Tipo de Distúrbio", y="Duração do Sono", color="Tipo de Distúrbio")
        fig8.update_layout(title="Duração do Sono por Tipo de Distúrbio")
        st.plotly_chart(fig8)
    else:
        st.warning("Nenhum dado disponível para os filtros selecionados.")

st.table(df_filtrado)