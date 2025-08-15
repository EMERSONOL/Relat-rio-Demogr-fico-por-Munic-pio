# 📊 Dashboard Demográfico dos Municípios do Rio de Janeiro

## 📜 Descrição
Este projeto consiste em um **dashboard interativo** desenvolvido com **Streamlit** para a análise e visualização de dados demográficos dos municípios do estado do Rio de Janeiro.  

A aplicação permite uma análise comparativa da população e da sua distribuição por cor/raça (**Brancos** e **Pretos**) entre os dados do Censo de 2010 e as estimativas para 2022, baseadas na população total do Censo de 2022.  

O objetivo é fornecer uma **ferramenta visual e intuitiva** para explorar o crescimento populacional e as mudanças na composição demográfica em nível municipal e regional.

---

## ✨ Features

- **Dashboard Interativo**: Interface web amigável para explorar os dados sem a necessidade de conhecimento em programação.
- **Relatório por Município**:  
  - **KPIs (Indicadores-Chave)**: População em 2010, população em 2022 e taxa de crescimento.  
  - **Gráfico de Barras Comparativo**: Evolução do número absoluto de pessoas brancas e pretas (2010 → 2022 estimado).  
  - **Gráficos de Pizza**: Composição racial percentual para 2010 e a estimativa para 2022.  
- **Análise Regional**: Seção expansível com agrupamento por regiões de governo do estado (Metropolitana, Serrana, etc.).  
- **Visualização de Dados Brutos**: Acesso à tabela de dados completa utilizada na análise.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit** — Criação da aplicação web interativa
- **Pandas** — Manipulação e estruturação de dados
- **Plotly** — Gráficos dinâmicos e interativos

---

## 📊 Fonte dos Dados e Metodologia

Os dados utilizados neste relatório são provenientes de fontes oficiais do **IBGE (Instituto Brasileiro de Geografia e Estatística)**.

- **População Total (2010 e 2022)**: Censo Demográfico do IBGE de 2010 e 2022  
- **Distribuição por Cor/Raça**: Percentuais extraídos do Censo Demográfico do IBGE de 2010  

### 🔍 Metodologia de Estimativa para 2022
Os dados de cor/raça para 2022 são **estimativas** calculadas da seguinte forma:

1. Obtiveram-se os percentuais de cor/raça do Censo de 2010.  
2. Aplicaram-se esses percentuais sobre a população total de cada município divulgada no Censo de 2022.  

💡 Essa abordagem permite analisar a evolução do volume populacional de cada grupo, assumindo que a proporção racial se manteve constante desde 2010.

---
