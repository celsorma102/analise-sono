# 📊 Análise de Nivel de Sono

Este projeto realiza uma análise exploratória de dados sobre distúrbios do sono disponível no Kaggle [por este link](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset), utilizando Python e bibliotecas como pandas e plotly.

## 🎯 Objetivo

Investigar padrões e fatores associados a distúrbios do sono em diferentes perfis de pessoas, considerando variáveis como profissão, gênero, IMC, nível de atividade física, entre outros.

## 🏗️ Estrutura do Projeto

- **analise.ipynb**: Notebook principal com todo o processo de leitura, tradução, limpeza, análise e visualização dos dados.
- **dataset/dataset.csv**: Base de dados utilizada na análise.
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
   - Visualizações com gráficos interativos usando plotly, incluindo histogramas, gráficos de pizza, barras, linha e boxplots.
   - Análise específica da distribuição da pressão arterial (sistólica e diastólica) entre grupos com e sem distúrbio do sono.

4. **Funções auxiliares**  
   - Funções para criar tabelas de frequência e agrupamentos de forma automatizada.
   - Funções para geração de diferentes tipos de gráficos.
   - Facilidade para adaptar a análise para outras variáveis do dataset.

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

## Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/analise-sono.git
   cd analise-sono
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install pandas plotly
   ```
3. Abra o arquivo `analise.ipynb` no Jupyter Notebook ou no VS Code.
4. Execute as células para reproduzir a análise.

## 📌 Resultados

O notebook apresenta tabelas e gráficos que mostram a distribuição dos distúrbios do sono por profissão, gênero, IMC, entre outros fatores.  
Também permite identificar possíveis relações entre hábitos, características pessoais e a presença de distúrbios do sono.  
A análise da pressão arterial foi aprimorada, permitindo visualizar a distribuição dos valores sistólicos e diastólicos separadamente, além de comparações entre grupos.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhorias, novas análises ou correções.

## Licença

Este projeto é apenas para fins educacionais.

---