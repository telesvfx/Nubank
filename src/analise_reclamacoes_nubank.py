import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Configurações de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Carregando dados
print("Carregando dados...")
df = pd.read_csv('/mnt/user-data/uploads/dados_nubank_extraidos.csv')

# Limpeza básica
df.columns = ['Reclamacao']
df = df.dropna()
df = df[df['Reclamacao'].str.len() > 10]

print(f"Total de reclamações: {len(df)}")
print("\nPrimeiras reclamações:")
print(df.head())

# ========== ANÁLISE DE PALAVRAS-CHAVE ==========
print("\n" + "="*60)
print("ANÁLISE DE PALAVRAS-CHAVE")
print("="*60)

# Palavras-chave para categorização
categorias = {
    'Bloqueio de Conta': ['bloqueado', 'bloqueio', 'desativação', 'desativada', 'encerramento'],
    'Cobrança Indevida': ['cobrança', 'cobrado', 'indevida', 'indevido', 'juros', 'dívida'],
    'Problemas com PIX': ['pix', 'transferência', 'estorno'],
    'Acesso à Conta': ['acesso', 'não consigo', 'impede', 'impossibilidade'],
    'Cartão de Crédito': ['cartão', 'limite', 'compra', 'transação'],
    'Atendimento': ['atendimento', 'recusa', 'suporte', 'mal educado'],
    'Empréstimo': ['empréstimo', 'consignado', 'desconto folha']
}

# Categorizar reclamações
df['Categoria'] = 'Outros'
texto_lower = df['Reclamacao'].str.lower()

for categoria, palavras in categorias.items():
    mask = texto_lower.str.contains('|'.join(palavras), case=False, na=False)
    df.loc[mask, 'Categoria'] = categoria

print("\nDistribuição de categorias:")
print(df['Categoria'].value_counts())

# ========== GRÁFICO 1: TOP 10 CATEGORIAS ==========
print("\nGerando gráficos...")
fig = plt.figure(figsize=(16, 12))

ax1 = plt.subplot(3, 2, 1)
categoria_counts = df['Categoria'].value_counts()
cores = plt.cm.Set3(np.linspace(0, 1, len(categoria_counts)))
categoria_counts.plot(kind='barh', ax=ax1, color=cores)
ax1.set_title('Tipos de Reclamações (Categorização)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Quantidade de Reclamações')
ax1.grid(axis='x', alpha=0.3)

# Adicionar valores nas barras
for i, v in enumerate(categoria_counts.values):
    ax1.text(v + 0.1, i, str(v), va='center')

# ========== GRÁFICO 2: PALAVRAS MAIS FREQUENTES ==========
ax2 = plt.subplot(3, 2, 2)

# Extrair palavras-chave
todas_palavras = ' '.join(df['Reclamacao']).lower()
from collections import Counter
palavras_stop = {'nubank', 'cliente', 'conta', 'de', 'que', 'em', 'e', 'a', 'o', 'na', 'não', 'para', 'com', 'sem', 'do', 'ou', 'ao', 'pela', 'pelo', 'da', 'dos', 'das', 'um', 'uma', 'após', 'foi', 'não', 'por', 'no'}

palavras_tokens = [p for p in todas_palavras.split() if len(p) > 4 and p not in palavras_stop]
contagem_palavras = Counter(palavras_tokens).most_common(15)

palavras, freq = zip(*contagem_palavras)
cores2 = plt.cm.Spectral(np.linspace(0, 1, len(palavras)))
ax2.barh(range(len(palavras)), freq, color=cores2)
ax2.set_yticks(range(len(palavras)))
ax2.set_yticklabels(palavras)
ax2.set_title('Palavras-Chave Mais Frequentes', fontsize=14, fontweight='bold')
ax2.set_xlabel('Frequência')
ax2.invert_yaxis()
ax2.grid(axis='x', alpha=0.3)

for i, v in enumerate(freq):
    ax2.text(v + 0.1, i, str(v), va='center')

# ========== GRÁFICO 3: DISTRIBUIÇÃO DE COMPRIMENTO DE RECLAMAÇÕES ==========
ax3 = plt.subplot(3, 2, 3)
df['Comprimento'] = df['Reclamacao'].str.len()
ax3.hist(df['Comprimento'], bins=40, color='skyblue', edgecolor='black', alpha=0.7)
ax3.set_title('Distribuição do Comprimento das Reclamações', fontsize=14, fontweight='bold')
ax3.set_xlabel('Número de caracteres')
ax3.set_ylabel('Frequência')
ax3.grid(axis='y', alpha=0.3)

# ========== GRÁFICO 4: PIE CHART DE CATEGORIAS ==========
ax4 = plt.subplot(3, 2, 4)
categoria_counts_top = df['Categoria'].value_counts().head(8)
colors_pie = plt.cm.Set3(np.linspace(0, 1, len(categoria_counts_top)))
wedges, texts, autotexts = ax4.pie(categoria_counts_top, labels=categoria_counts_top.index, 
                                     autopct='%1.1f%%', colors=colors_pie, startangle=90)
ax4.set_title('Distribuição de Categorias (%)', fontsize=14, fontweight='bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# ========== CLUSTERING COM K-MEANS (O GRÁFICO PRINCIPAL!) ==========
print("Executando clustering K-Means com análise TF-IDF...")

# Vetorização TF-IDF
# Palavras comuns em português para filtrar
stop_words_pt = ['o', 'a', 'de', 'e', 'que', 'do', 'da', 'em', 'para', 'é', 'com', 'não', 'uma', 'um', 'no', 'na', 'os', 'as', 'dos', 'das', 'ou', 'quando', 'muito', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'ele', 'você', 'essa', 'esse', 'este', 'fosse', 'esse', 'deles', 'delas']

vectorizer = TfidfVectorizer(max_features=100, stop_words=stop_words_pt, ngram_range=(1, 2))
X_tfidf = vectorizer.fit_transform(df['Reclamacao'])

# Determinar número ótimo de clusters
print("Calculando número ótimo de clusters...")
inertias = []
silhuetas = []
K_range = range(2, 11)

from sklearn.metrics import silhouette_score

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_tfidf)
    inertias.append(kmeans.inertia_)
    silhuetas.append(silhouette_score(X_tfidf, kmeans.labels_))

# Usar 4 clusters (bom balanço)
optimal_k = 4
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans_final.fit_predict(X_tfidf)

print(f"Clusters gerados: {optimal_k}")
print(f"Distribuição dos clusters:\n{df['Cluster'].value_counts().sort_index()}")

# Reduzir dimensionalidade com PCA para visualização
print("Reduzindo dimensionalidade com PCA para visualização...")
X_dense = X_tfidf.toarray()
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_dense)

# GRÁFICO 5: SCATTER PLOT DOS CLUSTERS (GRÁFICO PRINCIPAL COM CLUSTERING!)
ax5 = plt.subplot(3, 2, 5)
scatter = ax5.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Cluster'], 
                      cmap='viridis', s=100, alpha=0.6, edgecolors='black', linewidth=0.5)

# Plotar centroides
centroides_pca = pca.transform(kmeans_final.cluster_centers_)
ax5.scatter(centroides_pca[:, 0], centroides_pca[:, 1], 
           c='red', marker='X', s=300, edgecolors='black', linewidth=2, label='Centróides')

ax5.set_title(f'Clustering de Reclamações (K-Means, k={optimal_k})\n(Visualização PCA)', 
             fontsize=14, fontweight='bold')
ax5.set_xlabel(f'Componente Principal 1 ({pca.explained_variance_ratio_[0]:.1%})')
ax5.set_ylabel(f'Componente Principal 2 ({pca.explained_variance_ratio_[1]:.1%})')
ax5.legend()
ax5.grid(True, alpha=0.3)
cbar = plt.colorbar(scatter, ax=ax5)
cbar.set_label('Cluster', rotation=270, labelpad=20)

# GRÁFICO 6: COTOVELO (ELBOW) E SILHUETA
ax6 = plt.subplot(3, 2, 6)
ax6_twin = ax6.twinx()

line1 = ax6.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8, label='Inércia')
line2 = ax6_twin.plot(K_range, silhuetas, 'rs-', linewidth=2, markersize=8, label='Silhueta')

ax6.set_xlabel('Número de Clusters (k)', fontsize=11)
ax6.set_ylabel('Inércia', color='b', fontsize=11)
ax6_twin.set_ylabel('Score de Silhueta', color='r', fontsize=11)
ax6.set_title('Análise de Número Ótimo de Clusters', fontsize=14, fontweight='bold')
ax6.tick_params(axis='y', labelcolor='b')
ax6_twin.tick_params(axis='y', labelcolor='r')
ax6.grid(True, alpha=0.3)

# Adicionar legenda
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax6.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/analise_reclamacoes_completa.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfico salvo: analise_reclamacoes_completa.png")

# ========== ANÁLISE DOS CLUSTERS ==========
print("\n" + "="*60)
print("ANÁLISE DETALHADA DOS CLUSTERS")
print("="*60)

for cluster_id in range(optimal_k):
    cluster_data = df[df['Cluster'] == cluster_id]
    print(f"\n{'='*60}")
    print(f"CLUSTER {cluster_id} ({len(cluster_data)} reclamações)")
    print(f"{'='*60}")
    
    # Categorias mais comuns neste cluster
    print("\nCategorias mais frequentes:")
    print(cluster_data['Categoria'].value_counts().head(3))
    
    # Palavras-chave mais frequentes
    cluster_texto = ' '.join(cluster_data['Reclamacao']).lower()
    palavras_cluster = [p for p in cluster_texto.split() if len(p) > 4 and p not in palavras_stop]
    top_palavras = Counter(palavras_cluster).most_common(5)
    print("\nPalavras-chave mais frequentes:")
    for palavra, freq in top_palavras:
        print(f"  - {palavra}: {freq} vezes")
    
    # Exemplos de reclamações
    print("\nExemplos de reclamações:")
    for idx, reclamacao in enumerate(cluster_data['Reclamacao'].head(2).values, 1):
        print(f"  {idx}. {reclamacao[:100]}...")

# ========== CRIAR FIGURA ADICIONAL: HEATMAP DE CATEGORIAS POR CLUSTER ==========
fig2, ax = plt.subplots(figsize=(12, 6))

# Matriz de contingência
contingency = pd.crosstab(df['Cluster'], df['Categoria'])
sns.heatmap(contingency, annot=True, fmt='d', cmap='YlOrRd', ax=ax, cbar_kws={'label': 'Frequência'})
ax.set_title('Matriz de Categorias vs Clusters', fontsize=14, fontweight='bold')
ax.set_xlabel('Categoria de Reclamação')
ax.set_ylabel('Cluster')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/heatmap_categorias_clusters.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfico salvo: heatmap_categorias_clusters.png")

# ========== CRIAR FIGURA ADICIONAL: COMPARAÇÃO DE CARACTERÍSTICAS ==========
fig3, axes = plt.subplots(2, 2, figsize=(14, 10))

# Comprimento médio por cluster
ax = axes[0, 0]
df.groupby('Cluster')['Comprimento'].mean().plot(kind='bar', ax=ax, color='steelblue')
ax.set_title('Comprimento Médio de Reclamação por Cluster', fontsize=12, fontweight='bold')
ax.set_xlabel('Cluster')
ax.set_ylabel('Caracteres')
ax.grid(axis='y', alpha=0.3)

# Distribuição de clusters
ax = axes[0, 1]
df['Cluster'].value_counts().sort_index().plot(kind='bar', ax=ax, color='coral')
ax.set_title('Quantidade de Reclamações por Cluster', fontsize=12, fontweight='bold')
ax.set_xlabel('Cluster')
ax.set_ylabel('Quantidade')
ax.grid(axis='y', alpha=0.3)

# Top 3 categorias por cluster (stacked)
ax = axes[1, 0]
top_cats_by_cluster = pd.crosstab(df['Cluster'], df['Categoria']).iloc[:, :5]
top_cats_by_cluster.plot(kind='bar', stacked=True, ax=ax, colormap='Set3')
ax.set_title('Distribuição de Categorias por Cluster (Top 5)', fontsize=12, fontweight='bold')
ax.set_xlabel('Cluster')
ax.set_ylabel('Quantidade')
ax.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
ax.grid(axis='y', alpha=0.3)

# Silhueta por cluster
ax = axes[1, 1]
from sklearn.metrics import silhouette_samples
silhueta_valores = silhouette_samples(X_dense, df['Cluster'])
df_plot = pd.DataFrame({'Cluster': df['Cluster'], 'Silhueta': silhueta_valores})
df_plot.groupby('Cluster')['Silhueta'].apply(list).apply(lambda x: sorted(x)).apply(lambda x: np.mean(x)).plot(kind='bar', ax=ax, color='lightgreen')
ax.set_title('Score de Silhueta Médio por Cluster', fontsize=12, fontweight='bold')
ax.set_xlabel('Cluster')
ax.set_ylabel('Score de Silhueta')
ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/analise_clusters_detalhada.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico salvo: analise_clusters_detalhada.png")

# ========== EXPORTAR DADOS COM CLUSTERS ==========
df_export = df[['Reclamacao', 'Categoria', 'Cluster', 'Comprimento']]
df_export.to_csv('/mnt/user-data/outputs/reclamacoes_com_clusters.csv', index=False)
print("✓ Dados exportados: reclamacoes_com_clusters.csv")

print("\n" + "="*60)
print("ANÁLISE COMPLETA FINALIZADA!")
print("="*60)
print("\nArquivos gerados:")
print("  1. analise_reclamacoes_completa.png - Dashboard com 6 gráficos")
print("  2. heatmap_categorias_clusters.png - Matriz de contingência")
print("  3. analise_clusters_detalhada.png - Análise detalhada dos clusters")
print("  4. reclamacoes_com_clusters.csv - Dados com clusters atribuídos")

plt.show()
