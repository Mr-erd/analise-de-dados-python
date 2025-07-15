import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 1. Ler o CSV manualmente
datas = []
cotacoes = []

with open('USD_BRL_hist.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Pular cabeçalho
    for linha in reader:
        data_str, valor_str = linha
        data = datetime.strptime(data_str, '%d.%m.%Y')
        valor = float(valor_str)
        datas.append(data)
        cotacoes.append(valor)

# 2. Ordenar os dados por data
datas, cotacoes = zip(*sorted(zip(datas, cotacoes)))

# === Gráfico 1: Linha ===
plt.figure(figsize=(12, 6))
plt.plot(datas, cotacoes, color='blue')
plt.title('Cotação USD/BRL ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Cotação (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()

# === Gráfico 2: Histograma ===
plt.figure(figsize=(10, 5))
plt.hist(cotacoes, bins=20, color='green', edgecolor='black')
plt.title('Distribuição da cotação USD/BRL')
plt.xlabel('Cotação (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.tight_layout()
plt.show()

# === Gráfico 3: Área (simples) ===
plt.figure(figsize=(12, 6))
plt.fill_between(datas, cotacoes, color='skyblue', alpha=0.5)
plt.plot(datas, cotacoes, color='blue')
plt.title('Gráfico de Área da Cotação USD/BRL')
plt.xlabel('Data')
plt.ylabel('Cotação (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()
