import pandas as pd
import time
from sklearn.feature_extraction.text import CountVectorizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def coletar_reclamacoes(qtd_paginas=1):
    print("Iniciando o robô para coletar dados do Reclame Aqui...")
    
    # Configurando o navegador Chrome para abrir automaticamente
    servico = Service(ChromeDriverManager().install())
    opcoes = webdriver.ChromeOptions()
    # opcoes.add_argument("--headless") # Descomente essa linha se quiser que o navegador rode invisível (em segundo plano)
    
    navegador = webdriver.Chrome(service=servico, options=opcoes)
    
    reclamacoes = []
    
    # URL do Nubank no Reclame Aqui
    url_base = "https://www.reclameaqui.com.br/empresa/nubank/lista-reclamacoes/?pagina="
    
    for pagina in range(1, qtd_paginas + 1):
        print(f"Acessando página {pagina}...")
        navegador.get(url_base + str(pagina))
        
        # Pausa de 5 segundos para a página carregar (o Reclame Aqui demora um pouco)
        time.sleep(5) 
        
        # Pega todos os títulos das reclamações usando a classe CSS padrão do site
        # Nota: O Reclame Aqui pode mudar essa classe com o tempo
        elementos_titulo = navegador.find_elements(By.CSS_SELECTOR, "h4[class^='sc-1pe7b5t-1']")
        
        for elemento in elementos_titulo:
            texto = elemento.text
            if texto:
                reclamacoes.append(texto)
                
    navegador.quit()
    print(f"Coleta finalizada! {len(reclamacoes)} reclamações capturadas.")
    return reclamacoes

def gerar_insights(lista_reclamacoes):
    print("\nAnalisando os problemas mais comuns usando NLP...")
    
    if not lista_reclamacoes:
        print("Nenhuma reclamação encontrada para analisar.")
        return
        
    # Transformando a lista em um DataFrame do Pandas
    df = pd.DataFrame(lista_reclamacoes, columns=['Reclamacao'])
    
    # Palavras que não agregam valor e devem ser ignoradas
    palavras_inuteis = ['que', 'de', 'do', 'da', 'o', 'a', 'um', 'uma', 'no', 'na', 'com', 'para', 'nubank', 'nao', 'não', 'meu', 'minha']
    
    # Configurando o analisador de texto (pega as palavras mais frequentes, combinando até 2 palavras, ex: "cartão bloqueado")
    vetorizador = CountVectorizer(stop_words=palavras_inuteis, ngram_range=(1, 2))
    
    # Aplicando a matemática aos textos
    matriz_palavras = vetorizador.fit_transform(df['Reclamacao'])
    
    # Somando a frequência de cada palavra/termo
    soma_palavras = matriz_palavras.sum(axis=0)
    
    # Criando uma lista com as palavras e a quantidade de vezes que apareceram
    frequencia = [(palavra, soma_palavras[0, idx]) for palavra, idx in vetorizador.vocabulary_.items()]
    
    # Ordenando do maior problema para o menor
    frequencia_ordenada = sorted(frequencia, key=lambda x: x[1], reverse=True)
    
    print("\n--- TOP 10 PROBLEMAS MAIS COMENTADOS ---")
    for termo, qtd in frequencia_ordenada[:10]:
        print(f"Problema: '{termo.upper()}' -> {qtd} vezes mencionado")

# --- EXECUÇÃO DO PROJETO ---
if __name__ == "__main__":
    # Passo 1: Coleta as reclamações (coloque 2 ou 3 páginas para testar)
    dados_capturados = coletar_reclamacoes(qtd_paginas=5)    
    # Passo 2: Gera a solução baseada na frequência dos termos
    gerar_insights(dados_capturados)