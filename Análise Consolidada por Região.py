import streamlit as st
import pandas as pd
import plotly.express as px
import io

# --- Configuração da Página ---
st.set_page_config(
    page_title="Relatório Demográfico do Rio de Janeiro",
    page_icon="🏙️",
    layout="wide"
)

# --- Carregamento e Preparação dos Dados ---
@st.cache_data
def carregar_dados():
    # Dados extraídos da análise anterior, incluindo Pop. 2010 e classificação regional
    csv_data = """Município,Região,Pop. 2010,Pop. 2022,% Brancos (2010),% Pretos (2010)
Angra dos Reis,Médio Paraíba,169511,181228,45.0,11.2
Aperibé,Noroeste Fluminense,10213,10893,59.1,7.9
Araruama,Baixadas Litorâneas,112008,126726,39.0,15.8
Areal,Serrana,11423,11765,50.1,15.7
Armação dos Búzios,Baixadas Litorâneas,27560,39033,45.3,15.0
Arraial do Cabo,Baixadas Litorâneas,27715,31030,47.8,12.9
Barra do Piraí,Médio Paraíba,95390,91025,38.3,22.3
Barra Mansa,Médio Paraíba,177813,166654,45.4,16.3
Belford Roxo,Metropolitana,469332,446731,27.1,19.8
Bom Jardim,Serrana,25372,28166,63.2,10.6
Bom Jesus do Itabapoana,Noroeste Fluminense,35411,35797,49.0,15.0
Cabo Frio,Baixadas Litorâneas,186227,214057,41.8,15.4
Cachoeiras de Macacu,Metropolitana,54370,53887,41.6,9.2
Cambuci,Noroeste Fluminense,14816,14245,57.5,7.0
Campos dos Goytacazes,Norte Fluminense,463731,474667,42.0,17.6
Cantagalo,Serrana,20130,19443,48.8,18.8
Carapebus,Norte Fluminense,13427,13360,37.6,9.5
Cardoso Moreira,Noroeste Fluminense,12480,12686,49.0,12.1
Carmo,Serrana,17436,17149,48.1,20.2
Casimiro de Abreu,Baixadas Litorâneas,35359,45570,48.4,12.0
Duque de Caxias,Metropolitana,855048,782799,35.3,14.5
Itaboraí,Metropolitana,218008,231004,35.7,12.1
Itaguaí,Metropolitana,116841,132867,38.8,9.4
Japeri,Metropolitana,95492,96595,23.2,21.6
Magé,Metropolitana,227322,248208,35.8,14.5
Maricá,Metropolitana,128489,223938,55.5,7.5
Mesquita,Metropolitana,168376,168849,35.9,14.8
Nilópolis,Metropolitana,157425,150281,42.7,13.4
Niterói,Metropolitana,487562,523664,57.1,12.5
Nova Iguaçu,Metropolitana,796257,825388,36.4,13.6
Petrópolis,Serrana,295917,298020,58.7,13.2
Queimados,Metropolitana,137961,139975,27.8,21.6
Rio de Janeiro,Metropolitana,6320446,6211223,45.4,15.6
São Gonçalo,Metropolitana,999728,896744,38.5,15.5
Teresópolis,Serrana,163746,165123,61.9,10.9
"""
    
    df = pd.read_csv(io.StringIO(csv_data))
    
    # Cálculos de números absolutos
    df['Brancos (2010)'] = (df['Pop. 2010'] * df['% Brancos (2010)'] / 100).round().astype(int)
    df['Pretos (2010)'] = (df['Pop. 2010'] * df['% Pretos (2010)'] / 100).round().astype(int)
    df['Brancos (est. 2022)'] = (df['Pop. 2022'] * df['% Brancos (2010)'] / 100).round().astype(int)
    df['Pretos (est. 2022)'] = (df['Pop. 2022'] * df['% Pretos (2010)'] / 100).round().astype(int)
    
    return df

df = carregar_dados()

# --- Interface Principal ---
st.title("🏙️ Relatório Demográfico por Município")
st.markdown("Selecione um município para visualizar a análise detalhada de sua população e composição racial.")

# Seletor de Município
municipios = sorted(df['Município'].unique())
municipio_selecionado = st.selectbox("Escolha um Município:", municipios)

# --- Seção do Relatório Municipal ---
if municipio_selecionado:
    st.header(f"Análise de {municipio_selecionado}")

    # Filtrar dados para o município selecionado
    dados_municipio = df[df['Município'] == municipio_selecionado].iloc[0]

    # Calcular métricas
    pop_2010 = dados_municipio['Pop. 2010']
    pop_2022 = dados_municipio['Pop. 2022']
    crescimento_percentual = ((pop_2022 - pop_2010) / pop_2010) * 100 if pop_2010 > 0 else 0

    # Exibir KPIs (Key Performance Indicators)
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="População em 2010", value=f"{pop_2010:,.0f}")
    kpi2.metric(label="População em 2022", value=f"{pop_2022:,.0f}")
    kpi3.metric(label="Crescimento Populacional", value=f"{crescimento_percentual:.2f}%")

    st.divider()

    # Preparar dados para os gráficos
    dados_grafico_barras = pd.DataFrame({
        'Ano': ['2010', '2022 (est.)'],
        'Brancos': [dados_municipio['Brancos (2010)'], dados_municipio['Brancos (est. 2022)']],
        'Pretos': [dados_municipio['Pretos (2010)'], dados_municipio['Pretos (est. 2022)']]
    }).melt(id_vars='Ano', var_name='Cor/Raça', value_name='População')

    percent_outros = 100 - dados_municipio['% Brancos (2010)'] - dados_municipio['% Pretos (2010)']
    dados_grafico_pizza = pd.DataFrame({
        'Cor/Raça': ['Brancos', 'Pretos', 'Outros (Pardos, Amarelos, Indígenas)'],
        'Percentual': [dados_municipio['% Brancos (2010)'], dados_municipio['% Pretos (2010)'], percent_outros]
    })
    
    # Exibir Gráficos
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Crescimento da População (Absoluto)")
        fig_bar = px.bar(
            dados_grafico_barras,
            x='Ano',
            y='População',
            color='Cor/Raça',
            barmode='group',
            text_auto='.2s', # Formata o texto para números grandes
            title=f"População Branca e Preta em {municipio_selecionado}"
        )
        fig_bar.update_traces(textposition='outside')
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("Composição Racial (Percentual)")
        
        st.warning("""
        **Atenção:** A proporção para 2022 é **idêntica** à de 2010 porque os dados são uma estimativa. 
        Para ver a mudança real nos **números**, observe o gráfico de barras à esquerda.
        """)

        fig_pie_2010 = px.pie(
            dados_grafico_pizza,
            names='Cor/Raça',
            values='Percentual',
            hole=0.4,
            title=f"Distribuição em 2010 (Total: {pop_2010:,.0f})"
        )
        
        fig_pie_2022 = px.pie(
            dados_grafico_pizza,
            names='Cor/Raça',
            values='Percentual',
            hole=0.4,
            title=f"Distribuição Estimada em 2022 (Total: {pop_2022:,.0f})"
        )
        
        st.plotly_chart(fig_pie_2010, use_container_width=True)
        st.plotly_chart(fig_pie_2022, use_container_width=True)


# --- Seções Adicionais (Expansíveis) ---
with st.expander("Clique para ver a Análise Consolidada por Região"):
    st.header("Análise Consolidada por Região")
    df_regiao = df.groupby('Região').sum(numeric_only=True)
    df_regiao['Crescimento Pop. (%)'] = ((df_regiao['Pop. 2022'] - df_regiao['Pop. 2010']) / df_regiao['Pop. 2010'] * 100).round(2)
    st.dataframe(df_regiao[['Pop. 2010', 'Pop. 2022', 'Crescimento Pop. (%)']].style.format("{:,.0f}", subset=['Pop. 2010', 'Pop. 2022']))

with st.expander("Clique para ver a Tabela de Dados Completa"):
    st.header("Tabela de Dados Completa")
    st.dataframe(df)

st.info("""
**Fonte dos Dados:** IBGE, Censos Demográficos de 2010 e 2022.
**Observação:** Os números de 2022 para cor/raça são estimativas baseadas na proporção racial do Censo de 2010 aplicada à população total de 2022.
""")