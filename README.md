<h2 align="center">🟣 Nubank: Avaliação de Negócios e Análise Preditiva 🟣</h2>

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

## 📌 Sobre o Projeto

Este repositório documenta uma análise avançada focada no ecossistema do Nubank. O objetivo principal é extrair e identificar problemas e oportunidades de negócio a partir de fontes de dados públicos (dados macroeconômicos, balanços financeiros, sentimento do consumidor, etc.).

Através de análises preditivas e modelagem, o projeto busca avaliar a saúde financeira e o direcionamento estratégico da empresa, culminando em uma apresentação gerencial com foco em tomadas de decisão.

---

## 🗺️ Guia Visual do Repositório

![Guia do Repositório](<assets/guia o que cada pasta faz.png>)

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
```

## 👥 Equipe & Divisão de Responsabilidades  

O pipeline de dados foi estruturado estrategicamente para cobrir **toda a esteira do projeto**, desde a coleta até a geração de insights estratégicos:

### 🔹 Pessoa 1 — Data Engineer  

- Coleta de dados (balanço patrimonial + dados macroeconômicos)  
- Limpeza e tratamento inicial  
- Organização estrutural dos arquivos na pasta `/data`  

### 🔹 Pessoa 2 — Feature Engineer  

- Criação de métricas financeiras  
- Transformações e normalizações  
- Desenvolvimento de variáveis derivadas para enriquecer as análises  

### 🔹 Pessoa 3 — Modelagem  

- Desenvolvimento de modelos preditivos (Regressão e Forecast)  
- Construção de cenários  
- Simulações e análises estatísticas  

### 🔹 Pessoa 4 — Visualização & Business Insights  

- Construção de dashboards  
- Análise estratégica do negócio  
- Elaboração do relatório e apresentação final  

---

## 👤 Integrantes  

- **Thiago Teles**  
- **Paulo Futagawa**  
- **Thaís Nakazone**  
- **Felipe Tavares**  

## 🔄 Fluxo de Trabalho (Code Review)

Nenhum código vai direto para a branch principal.

Fluxo padrão:

- Criar uma **branch** para sua tarefa
- Abrir um **Pull Request (PR)**  
- Passar por **Code Review** de pelo menos um integrante antes do merge  

Esse processo garante organização, qualidade e colaboração no projeto.

## ⚙️ Como Reproduzir o Ambiente

Siga os passos abaixo para configurar o projeto localmente:

### 📥 1. Clone o repositório

```bash
git clone https://github.com/telesvfx/nubank.git
cd nubank
```

## 🐍 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

## Ativação no Windows

```bash
.venv\Scripts\activate
```

## 📦 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 📄 Licença

Este projeto está distribuído sob a **Licença MIT**.

Para mais detalhes sobre permissões, limitações e responsabilidades, consulte o arquivo `LICENSE` presente neste repositório.


# Nubank 2025: Diagnóstico Estratégico 360°

## Cruzamento entre Saúde Financeira (Pilar 3 / Bacen) e Percepção de Mercado (Análise de Sentimento)

**Confidencial — Uso Interno | Março 2026**

---

# O Contexto: Por Que Esta Análise Importa

## Uma instituição líder sob pressão silenciosa

- O Nubank é o maior banco digital da América Latina, com ~100 milhões de clientes
- Os relatórios regulatórios do Bacen (Pilar 3) revelam **tensões crescentes de capital e risco**
- As reclamações públicas revelam **onde o cliente já sente esse estresse operacional**
- Esta apresentação cruza essas duas lentes para propor **ações concretas e mensuráveis**

> *"Dados financeiros dizem o que está acontecendo. Dados de sentimento dizem por que o cliente está indo embora."*

---

# O Cenário Financeiro e de Risco

## Síntese dos Relatórios Pilar 3 — Q1 a Q3 2025

## Capital e Solvência: Crescimento com Buffer em Erosão

- **Patrimônio de Referência** cresceu de R$22,8B (Q1) → R$23,0B (Q3): sólido em termos absolutos
- **RWA Total** cresceu +16,4% em apenas 2 trimestres: R$135B → R$158B
- **Índice de Basileia** caiu de 16,86% (Q1) → 14,59% (Q3): queda de 2,27 pp em 6 meses
- **Margem Excedente de Capital Principal** em queda livre: 6,79% → 4,88% (≈ -1pp/trimestre)
- **Projeção Q4/2025:** Índice de Basileia em ~11,4% — perigosamente próximo do mínimo regulatório de 10,5%

*[Inserir Gráfico: Evolução do Índice de Basileia e Margem Excedente — Q1 a Q3 2025]*

## Risco de Crédito: Inadimplência em Aceleração

- **Ativos Problemáticos cresceram +64% em um único trimestre** (Q2): de R$13,5B → R$22,1B
- Taxa de formação bruta de inadimplência: **79,5% do estoque em 90 dias** — acima de qualquer benchmark saudável
- Baixa contábil (write-off) de apenas R$55M: indica que o estoque problemático **ainda não foi devidamente provisionado**

*[Inserir Gráfico: Waterfall CR2 — Fluxo de Ativos Problemáticos Q2 2025]*

## Alerta Emergencial: Risco Cambial Explodiu no Q3

- RWA de câmbio saltou **+882% em um trimestre**: R$522M → R$5,1B
- Análise OLS confirma: **câmbio é o driver dominante de compressão do Índice de Basileia**, superando o risco de crédito
- Cluster K-Means identifica Q3/2025 como **outlier isolado** — perfil de risco incompatível com os 4 trimestres anteriores

*[Inserir Gráfico: Decomposição do RWA por Tipo de Risco — Q1 a Q3 2025]*

---

# A Voz do Cliente

## Análise de Sentimento — 122 Reclamações (Reclame Aqui / Fontes Públicas)

## O Que o Cliente Está Gritando

- **Cartão de Crédito** é a categoria mais reclamada: 36 registros (29,5% do total)
- **Cobrança Indevida** em segundo lugar: 22 reclamações (18%) — com impacto financeiro médio de ~R$3.000 por caso
- **Problemas com PIX e Transferências**: 12 reclamações (10%) — impacto direto na operação do dia a dia
- **Bloqueio e Acesso à Conta**: 11 reclamações (9%) — gera abandono imediato e churn silencioso

*[Inserir Gráfico: Distribuição de Categorias de Reclamação — Barras Horizontais]*

## Segmentação por Tipo de Impacto

- **82% das reclamações envolvem Perda Financeira Direta** — o cliente está sendo prejudicado no bolso
- **15% são Problemas Funcionais** — o produto simplesmente não funciona quando o cliente precisa
- **3,3% envolvem Segurança** — minoritário em volume, mas de impacto catastrófico na confiança

*[Inserir Gráfico: Distribuição de Tipos de Problema — Pizza / Barras]*

## Clustering Semântico: 4 Perfis de Cliente Insatisfeito

| Cluster | Perfil | Volume | Risco |
|--------|--------|--------|-------|
| 0 | PIX e Contestações | 29 reclamações | Médio |
| 1 | Bloqueio e Acesso | 31 reclamações | Alto |
| **2** | **Cobrança Indevida Crítica** | **24 reclamações** | **🔴 Máximo** |
| 3 | Problemas com Cartão | 38 reclamações | Alto |

- **Cluster 2 é o ponto de risco máximo**: 62,5% dos casos envolve perda financeira comprovada
- Modelo Random Forest detecta reclamações graves com **94,6% de acurácia**
- Feature mais preditiva de severidade: "cobrança indevida" (29,1% de importância no modelo)

*[Inserir Gráfico: Heatmap Matriz de Categorias vs Clusters | Scatter PCA dos Clusters]*

## Tendência Temporal: O Cliente Está Voltando a Reclamar

- Setembro 2024: pico de 14.800 reclamações (crise de instabilidade técnica)
- Janeiro 2025: queda para ~1.000 reclamações (-93%) — infraestrutura melhorou
- **Porém: reclamações de cobrança e cartão mantêm frequência constante** — não são sazonais, são estruturais

*[Inserir Gráfico: Tendência de Instabilidades Técnicas 2024–2025]*

---

# Cruzamento de Dados

## Risco Financeiro × Experiência do Cliente: Onde as Duas Crises se Encontram

## Correlação 1: Inadimplência Alta → Bloqueios Indevidos

- O crescimento de 64% nos ativos problemáticos no Q2 pressiona os sistemas de análise de risco
- Para se proteger, o banco aciona **bloqueios preventivos automáticos** — muitos são falsos positivos
- Resultado no Reclame Aqui: **31 reclamações de bloqueio de conta** — cliente punido sem ter errado
- **O risco do banco vira a dor do cliente**

## Correlação 2: Modelo de Crédito Agressivo → Cobrança Percebida como Abusiva

- Inadimplência de 30% da carteira vs. 23% do SFN (acima da média do sistema)
- Estratégia "low and grow" concede crédito a perfis de maior risco → juros mais altos para compensar
- Cliente de baixa renda recebe limite alto, usa, não consegue pagar, recebe cobrança que percebe como injusta
- **Kata financeira → Crise de reputação**

## Correlação 3: Risco Cambial Elevado → Instabilidade Operacional Latente

- O salto do RWA cambial (+882%) pode indicar exposição em produtos internacionais (cartão global, crypto, remessas)
- Esses produtos são exatamente os que geram mais reclamações de "cobrança indevida em moeda estrangeira"
- **O mesmo vetor de risco regulatório alimenta o vetor de reclamação do cliente**

## Correlação 4: Compressão de Capital → Menos Investimento em Atendimento

- Com capital sendo consumido pelo crescimento do RWA, há pressão para reduzir custos operacionais
- Atendimento ao cliente é frequentemente o primeiro a sofrer cortes de headcount ou automação prematura
- Reclame Aqui confirma: **"Atendimento Deficiente" aparece como categoria recorrente**

---

# Os 3 Gargalos Críticos

## Problemas Confirmados pelos Dados — Sem Hipóteses, Apenas Evidências

## 🔴 Gargalo 1: Erosão Acelerada do Buffer de Capital

**O problema em números:**

- Margem excedente caindo ~1pp/trimestre: se mantida, atinge o mínimo regulatório em ~4 trimestres
- RWA crescendo 2x mais rápido que o capital
- Modelo preditivo aponta Índice de Basileia em 11,4% no Q4/2025

**Impacto para o negócio:**

- Risco de intervenção regulatória do Bacen
- Limitação obrigatória de crescimento de carteira
- Custo de captação aumenta (investidores exigem prêmio de risco)

## 🔴 Gargalo 2: Motor de Inadimplência Descontrolado

**O problema em números:**

- Taxa de formação bruta: 79,5% do estoque em 90 dias — sinal de deterioração estrutural, não cíclica
- Write-off de apenas R$55M vs. estoque de R$22B: provisões insuficientes
- Cluster 2 (Cobrança Indevida) com 62,5% de perda financeira confirmada

**Impacto para o negócio:**

- Pressão sobre RWA de crédito (já em R$108B e crescendo +10% trimestre a trimestre)
- Passivo jurídico crescente (danos morais reconhecidos em processos)
- Churn de clientes bons que se sentem contaminados pelo ambiente de cobrança

## 🟠 Gargalo 3: Exposição Cambial Fora de Controle

**O problema em números:**

- RWA de câmbio: R$522M (Q2) → R$5,1B (Q3) em um único trimestre
- Identificado pelo modelo OLS como o principal driver de compressão do IB
- K-Means isola Q3/2025 como outlier absoluto nos últimos 5 períodos

**Impacto para o negócio:**

- Consome capital regulatório que poderia financiar crescimento de carteira
- Exposição a choques externos (câmbio, juros internacionais)
- Difícil de comunicar para investidores sem plano de hedge estruturado

---

# Plano de Ação

## Soluções Estratégicas Baseadas em Dados — Priorizadas por Impacto e Urgência

## 🔴 Solução 1: Programa de Hedge Estrutural de Câmbio

**Para o Gargalo 1 (capital) e Gargalo 3 (câmbio)**

- **O que fazer:** Contratar NDFs (Non-Deliverable Forwards) ou swaps cambiais para reduzir exposição líquida abaixo de R$1B
- **Limite interno:** Implementar sistema de alertas em 3 níveis — Verde (<R$1B), Amarelo (R$1–3B), Vermelho (>R$3B)
- **Impacto esperado:** Liberação de ~R$4,6B em RWA → recuperação de ~0,3pp no Índice de Basileia
- **Prazo:** 30–60 dias para MVP; 90 dias para implementação completa
- **Benefício duplo:** Reduz risco regulatório E estabiliza produtos cambiais que geram reclamações de cobrança indevida

## 🔴 Solução 2: Recalibração do Motor de Crédito com Early Warning de Inadimplência

**Para o Gargalo 2 (inadimplência)**

- **O que fazer:** Implementar modelo de Early Warning (XGBoost + SHAP) para detectar migração de risco 90 dias antes do vencimento
- **Gatilho de ação:** Quando probabilidade de default superar 40%, acionar renegociação proativa — antes da cobrança
- **Revisão de política:** Reduzir concessão de crédito rotativo para segmentos com PD > 15%; migrar para produtos de menor FPR (consignado = 75% vs. rotativo = 100%)
- **Impacto esperado:** Redução da taxa de entrada bruta em ativos problemáticos de 79,5% → meta de ≤ 50% em 2 trimestres
- **Benefício duplo:** Menor inadimplência → menos bloqueios indevidos → menos reclamações no Reclame Aqui

## 🔴 Solução 3: Emissão de Capital Nível II + Securitização de Carteira

**Para o Gargalo 1 (erosão do buffer de capital)**

- **O que fazer:** Emitir R$2–3B em Letras Financeiras Subordinadas (elegíveis ao PR Nível II) até o Q4/2025
- **Alternativa complementar:** Securitizar carteiras de crédito consignado (FPR 75%) para liberar RWA sem reduzir carteira
- **Meta:** Manter Índice de Basileia ≥ 15,5% no Q4/2025 independente do crescimento orgânico
- **Prazo:** Estruturação em 60–90 dias; emissão em 90–120 dias
- **Benefício:** Sinaliza ao mercado e ao Bacen que o banco é pró-ativo na gestão de capital

## 🟠 Solução 4: Sistema Inteligente de Revisão de Bloqueios

**Para o Reclame Aqui — Cluster 1 (Bloqueio) e impacto reputacional**

- **O que fazer:** Implementar ML de revisão automática de falsos positivos em bloqueios de conta
- **Lógica:** Se cliente tem histórico limpo (>12 meses) e o trigger foi comportamental (não fraude confirmada), liberar automaticamente com notificação em tempo real
- **Meta:** Reduzir reclamações de bloqueio indevido em -50% em 60 dias
- **Benefício:** Redução direta do Cluster 1 do Reclame Aqui + menor passivo jurídico

## 🟡 Solução 5: Programa de Transparência Pós-Incidente

**Para confiança e retenção de clientes**

- **O que fazer:** Criar protocolo estruturado de comunicação durante e após falhas (técnicas, de cobrança ou segurança)
- **Canais:** Push notification, e-mail e status page pública em <15 minutos após detecção de incidente
- **Meta:** Elevar satisfação de atendimento de 79,5% → 90%+ em 6 meses
- **Benefício:** Confiança mantida mesmo em momentos de falha — diferencial competitivo sustentável

---

# Conclusão e Próximos Passos

## O Que os Dados Nos Dizem — e O Que Fazer Agora

## O Diagnóstico em Uma Frase

> O Nubank é uma máquina de crescimento extraordinária que começa a sentir o peso do próprio tamanho: capital sendo consumido mais rápido do que é recomposto, inadimplência estruturalmente elevada e um cliente que percebe o estresse operacional antes do regulador.

## Os Números Que Não Mentem

| Indicador | Situação Atual | Meta Proposta | Prazo |
|-----------|---------------|---------------|-------|
| Índice de Basileia | 14,59% (↓ 2,27pp em 6m) | ≥ 15,5% | Q4/2025 |
| RWA Câmbio | R$5,1B (+882%) | < R$1B | 60–90 dias |
| Ativos Problemáticos | R$22,1B (+64% em 1 trim.) | Taxa de entrada ≤ 50% | 2 trimestres |
| Reclamações Cobrança | Cluster crítico (62,5% perda $) | -40% em volume | 90 dias |
| Margem Excedente Capital | 4,88% (↓ 1pp/trim.) | ≥ 6% | Q2/2026 |

## Próximos Passos Imediatos

1. **Semana 1–2:** Acionar mesa de câmbio para estruturar hedge — decisão executiva de baixo atrito, alto impacto
2. **Mês 1:** Iniciar estruturação da emissão de LFs Subordinadas (Nível II)
3. **Mês 1–2:** Deploy do modelo de Early Warning de inadimplência em ambiente de staging
4. **Mês 2:** Lançar sistema de revisão automática de bloqueios indevidos
5. **Mês 3:** Revisão completa da política de concessão para segmentos de alto PD

## O Cenário Mais Provável (70% de probabilidade)

- Com as 5 ações implementadas: Índice de Basileia estabilizado acima de 15,5% no Q4/2025
- Redução de 40–50% nas reclamações de cobrança indevida até Q2/2026
- Crescimento de carteira mantido em 30–40% A/A com menor consumo de capital por unidade de risco
- **Resultado:** Nubank preserva liderança de mercado e confiança regulatória simultaneamente

---

*Análise realizada com dados públicos do Pilar 3 (Bacen Circular 3.930) e pesquisa de sentimento de clientes*
*Modelo preditivo baseado em Random Forest, K-Means, Regressão Polinomial e OLS*
*Período analisado: Q1 a Q3 2025 | Data de elaboração: Março 2026*
*Equipe: Thiago Teles Silva | Paulo Futagawa | Thaís | Felipe Tavares*