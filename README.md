
# 🟣 Nubank: Avaliação de Negócios e Análise Preditiva

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

## 📌 Sobre o Projeto
Este repositório documenta uma análise avançada focada no ecossistema do Nubank. O objetivo principal é extrair e identificar problemas e oportunidades de negócio a partir de fontes de dados públicos (dados macroeconômicos, balanços financeiros, sentimento do consumidor, etc.). 

Através de análises preditivas e modelagem, o projeto busca avaliar a saúde financeira e o direcionamento estratégico da empresa, culminando em uma apresentação gerencial com foco em tomadas de decisão.

---

## 📂 Estrutura do Repositório

A arquitetura foi desenhada para garantir a reprodutibilidade da análise, separando dados brutos da experimentação e do código final:

```text
├── data/
│   ├── processed/          # Dados limpos e tratados para modelagem
│   └── raw/                # Dados originais e extrações (imutáveis)
├── notebooks/              # Explorações e testes de hipóteses (.ipynb)
├── reports/                # Apresentação final e dashboards exportados
├── src/                    # Scripts em Python consolidados
│   ├── data_collection.py  # Automações e web scraping (ex: Reclame Aqui)
│   ├── feature_engineering.py
│   ├── modeling.py         # Algoritmos de regressão e forecast
│   └── visualization.py    # Geração de gráficos para a apresentação
├── .gitignore              
├── README.md               
└── requirements.txt        # Bibliotecas necessárias (pandas, scikit-learn, etc.)


👥 Equipe e Divisão de Responsabilidades

O pipeline de dados foi dividido estrategicamente para cobrir toda a esteira do projeto, desde a coleta até a apresentação final:

Pessoa 1 – Data Engineer: Coleta dos dados (balanço + macro), limpeza e organização estrutural na pasta /data.

Pessoa 2 – Feature Engineer: Criação de métricas, transformações de dados e elaboração de variáveis derivadas para enriquecer as análises.

Pessoa 3 – Modelagem: Desenvolvimento das análises preditivas (Regressão, Forecast) e construção de cenários e simulações.

Pessoa 4 – Visualização + Business Insights: Construção dos dashboards, formulação da análise estratégica do negócio e escrita do relatório/apresentação final.

Integrantes:
Thiago Teles Silva | Paulo Futagawa | Thaís | Felipe Tavares

🔄 Fluxo de Trabalho (Code Review)

Nenhum código vai direto para a branch principal. O fluxo oficial da equipe é:

Trabalhar em uma branch dedicada à sua tarefa.

Abrir um Pull Request (PR).

Todo PR exige revisão cruzada (Code Review) de pelo menos um colega antes do merge.

⚙️ Como Reproduzir o Ambiente

Clone o repositório:

Bash
git clone [https://github.com/SEU_USUARIO/nubank-financial-analysis-ds.git](https://github.com/SEU_USUARIO/nubank-financial-analysis-ds.git)
cd nubank-financial-analysis-ds
Crie e ative o ambiente virtual:

Bash
python -m venv .venv
.venv\Scripts\activate  # Windows
Instale as dependências:

Bash
pip install -r requirements.txt
📄 Licença
Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


---

 2. Copie e cole em um novo arquivo chamado `LICENSE` (sem extensão, direto na raiz do projeto)

```text
MIT License

Copyright (c) 2026 Thiago Teles Silva, Paulo Futagawa, Thaís, Felipe Tavares

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.