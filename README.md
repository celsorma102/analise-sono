# 📊 Análise de Nível de Sono

Este projeto realiza uma análise exploratória e visualização interativa de dados sobre distúrbios do sono, utilizando Python, pandas, plotly, Jupyter Notebook e Streamlit. Os dados estão disponíveis no Kaggle [neste link](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset).

## 🎯 Objetivo

Investigar padrões e fatores associados a distúrbios do sono em diferentes perfis de pessoas, considerando variáveis como profissão, gênero, IMC, nível de atividade física, pressão arterial, entre outros.

## 🏗️ Estrutura do Projeto

- **analise.ipynb**: Notebook principal com todo o processo de leitura, tradução, limpeza, análise e visualização dos dados.
- **app.py**: Aplicação interativa desenvolvida com Streamlit para exploração dinâmica dos dados e gráficos.
- **dataset/dataset.csv**: Base de dados original utilizada na análise.
- **dataset/dataset_traduzido.csv**: Base de dados traduzida e tratada.
- **requirements.txt**: Lista de dependências do projeto.
- **README.md**: Este arquivo, com informações sobre o projeto.

## 📒 Principais etapas

1. **Leitura dos dados**  
   Importação do dataset em formato CSV hospedado no GitHub.

2. **Tradução e limpeza**  
   - Tradução dos nomes das colunas e valores categóricos para português.
   - Tratamento de valores ausentes (por exemplo, preenchendo distúrbios do sono ausentes como "Sem Distúrbio").
   - Criação de colunas auxiliares, como "Tem Distúrbio", para facilitar análises.
   - Separação dos valores de pressão arterial em colunas "Sistólica" e "Diastólica" para análises mais detalhadas.

3. **Análise exploratória**  
   - Geração de tabelas de frequência para variáveis categóricas.
   - Agrupamentos cruzando variáveis como profissão, gênero e IMC com a presença de distúrbios do sono.
   - Visualizações com gráficos interativos usando plotly, incluindo histogramas, gráficos de pizza, barras, linha, boxplots e violino.
   - Análise específica da distribuição da pressão arterial (sistólica e diastólica) entre grupos com e sem distúrbio do sono.

4. **Aplicação interativa (Streamlit)**  
   - Filtros dinâmicos por gênero, idade, profissão, IMC, tipo e qualidade do sono.
   - KPIs automáticos (idade média, estresse médio, profissão mais frequente, etc).
   - Diversos gráficos interativos para storytelling e exploração dos dados.
   - Visualização da tabela filtrada em tempo real.

5. **Funções auxiliares**  
   - Funções para criar tabelas de frequência e agrupamentos de forma automatizada.
   - Funções para geração de diferentes tipos de gráficos.
   - Facilidade para adaptar a análise para outras variáveis do dataset.

## 📊 Gráficos Utilizados

O projeto faz uso de uma variedade de gráficos interativos para explorar e comunicar os padrões dos dados de sono:

- **Gráficos de Barras e Histogramas**: Permitem visualizar a distribuição de variáveis categóricas e numéricas, como a frequência de distúrbios do sono por profissão ou a distribuição de idades por gênero.
- **Gráficos de Pizza**: Mostram a proporção de cada tipo de distúrbio do sono na amostra.
- **Boxplots**: Facilitam a comparação da distribuição de variáveis numéricas (como duração do sono) entre diferentes grupos (gênero, tipo de distúrbio).
- **Gráficos de Linha**: Usados para visualizar tendências ao longo de uma variável contínua, como a duração do sono.
- **Scatter Plot (Dispersão)**: Utilizado para analisar a relação entre duas variáveis numéricas, como duração do sono e nível de estresse. O scatter plot permite identificar padrões, tendências e possíveis correlações entre variáveis. No projeto, também foi adicionado um trendline para facilitar a visualização da tendência geral dos dados.
- **Violin Plot**: Um gráfico que combina características do boxplot e do histograma, mostrando a distribuição da variável (por exemplo, nível de estresse) para cada categoria (tipo de distúrbio do sono). O violin plot permite visualizar não só a mediana e os quartis, mas também a densidade dos dados, facilitando a identificação de padrões e diferenças entre grupos.

> **Destaque:**  
> O uso dos gráficos de dispersão (scatter) e violin foi um diferencial neste projeto, pois são ferramentas poderosas para análise exploratória, mas que raramente havia utilizado antes. O scatter plot ajudou a revelar relações entre variáveis contínuas, enquanto o violin plot trouxe uma visão mais rica da distribuição dos dados em diferentes categorias, indo além do que um boxplot tradicional mostraria.

Esses gráficos, aliados à interatividade do Streamlit e Plotly, tornam a análise mais dinâmica, visual e acessível para diferentes publicos.

## ✅ Variáveis analisadas

- **ID da Pessoa**: Identificador único.
- **Gênero**: Masculino ou Feminino.
- **Idade**
- **Profissão**
- **Duração do Sono**: Horas dormidas por noite.
- **Qualidade do Sono**: Escala de avaliação.
- **Nível de Atividade Física**
- **Nível de Estresse**
- **Categoria de IMC**: Peso normal, Sobrepeso, Obesidade, etc.
- **Pressão Arterial**: Valor original (ex: 120/80), além das colunas separadas "Sistólica" e "Diastólica".
- **Frequência Cardíaca**
- **Passos Diários**
- **Tipo de Distúrbio**: Insônia, Apneia do Sono ou Sem Distúrbio.
- **Tem Distúrbio**: Coluna booleana indicando presença ou ausência de distúrbio do sono.

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/analise-sono.git
   cd analise-sono
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Para análise exploratória, abra o arquivo `analise.ipynb` no Jupyter Notebook ou no VS Code e execute as células.
4. Para a aplicação interativa, execute:
   ```bash
   streamlit run app.py
   ```
   Acesse o endereço exibido no terminal para interagir com os filtros e gráficos.

## 📌 Resultados

O projeto apresenta tabelas e gráficos que mostram a distribuição dos distúrbios do sono por profissão, gênero, IMC, entre outros fatores.  
Permite identificar possíveis relações entre hábitos, características pessoais e a presença de distúrbios do sono.  
A análise da pressão arterial foi aprimorada, permitindo visualizar a distribuição dos valores sistólicos e diastólicos separadamente, além de comparações entre grupos.  
A aplicação Streamlit facilita a exploração dinâmica dos dados, tornando o storytelling mais acessível e visual.

## 🏷️ Principais tecnologias e tópicos

`python` `pandas` `plotly` `streamlit` `jupyter-notebook` `data-analysis` `data-visualization` `sleep` `health` `storytelling`

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhorias, novas análises ou correções.

## 📄 Licença

Este projeto é apenas para fins educacionais.