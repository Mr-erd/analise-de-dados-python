
<h1 align="center">Análise e Visualização da Cotação Dólar (USD/BRL) 📈💵</h1>

<p align="center">
  <strong>Um projeto em Python que transforma dados históricos de câmbio em visualizações claras e intuitivas usando a biblioteca Matplotlib.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Matplotlib-3.7%2B-green?style=for-the-badge&logo=matplotlib" alt="Matplotlib">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License MIT">
</p>

---

## 📍 Tabela de Conteúdos

* [📌 Sobre o Projeto](#-sobre-o-projeto)
* [📊 As Visualizações Geradas](#-as-visualizações-geradas)
* [⚙️ Como o Código Funciona](#️-como-o-código-funciona)
* [💾 Formato dos Dados de Entrada](#-formato-dos-dados-de-entrada)
* [🚀 Como Começar](#-como-começar)
* [💡 Ideias para Melhorias Futuras](#-ideias-para-melhorias-futuras)
* [👨‍💻 Autor](#-autor)

---

## 📌 Sobre o Projeto

Você já se perguntou como o valor do Dólar flutuou ao longo do tempo? Este projeto responde a essa pergunta de forma visual! O script lê um arquivo de dados históricos (`.csv`) contendo a cotação diária do Dólar em relação ao Real e, com a ajuda da poderosa biblioteca **Matplotlib**, gera três gráficos distintos para uma análise completa e fácil de entender.

---

## 📊 As Visualizações Geradas

Cada gráfico conta uma parte diferente da história dos dados.

### 1. Gráfico de Linha: A Jornada do Dólar no Tempo 📉
Este gráfico é perfeito para visualizar a **tendência** da cotação ao longo do período analisado. Com ele, podemos identificar facilmente picos de alta, vales de baixa e momentos de maior estabilidade.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_plot_001.png" alt="Exemplo de Gráfico de Linha" width="600">
  <sub><em>Exemplo ilustrativo de um gráfico de linha temporal.</em></sub>
</p>

### 2. Histograma: A "Personalidade" do Preço 🧱
Quais valores o Dólar mais assumiu? O histograma agrupa as cotações em faixas de preço e mostra a **frequência** de cada uma. Ele revela os níveis de preço mais comuns e os mais raros.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_hist_001.png" alt="Exemplo de Histograma" width="550">
  <sub><em>Exemplo ilustrativo de um histograma.</em></sub>
</p>

### 3. Gráfico de Área: A Magnitude da Variação 🏞️
Visualmente impactante, o gráfico de área preenche o espaço sob a linha de cotação. Isso ajuda a dar uma noção de **volume e magnitude** da variação, destacando os períodos de cotações mais altas de forma dramática.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_fill_between_001.png" alt="Exemplo de Gráfico de Área" width="600">
  <sub><em>Exemplo ilustrativo de um gráfico de área.</em></sub>
</p>

---

## ⚙️ Como o Código Funciona

O script segue um fluxo de trabalho lógico e bem definido:

| Passo | Ação | Descrição |
| :---: | :--- | :--- |
| **1** | **📥 Ingestão de Dados** | Abre e lê o arquivo `USD_BRL_hist.csv`, pulando a linha de cabeçalho. |
| **2** | **🔄 Processamento** | Para cada linha, converte o texto da data em um objeto `datetime` e o texto do valor em um número `float`. |
| **3** | **🗄️ Armazenamento** | Guarda os dados processados em duas listas separadas: `datas` e `cotacoes`. |
| **4** | **⏳ Ordenação** | Garante que os dados estejam em ordem cronológica para que os gráficos de linha e área façam sentido. |
| **5** | **🎨 Visualização** | Utiliza o `matplotlib.pyplot` para criar, customizar (com títulos, cores e rótulos) e exibir cada um dos três gráficos. |

---

## 💾 Formato dos Dados de Entrada

Para que a mágica aconteça, o script precisa de um arquivo chamado `USD_BRL_hist.csv` localizado na mesma pasta.

* **Nome do Arquivo:** `USD_BRL_hist.csv`
* **Formato:** Duas colunas (`Data,Fechamento`), separadas por vírgula. A data deve estar no formato `dd.mm.yyyy`.

**Exemplo de conteúdo do arquivo:**
```csv
Data,Fechamento
29.06.2024,5.45
28.06.2024,5.42
27.06.2024,5.48
...
```

---

## 🚀 Como Começar

Siga estes passos para rodar o projeto em sua própria máquina.

### ✅ Pré-requisitos

* **Python 3** instalado em seu sistema.
* A biblioteca **Matplotlib**. Se não a tiver, instale com este comando no seu terminal:
    ```bash
    pip install matplotlib
    ```

### 🏃‍♀️ Passos para Execução

1.  **Clone o repositório** para sua máquina local:
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até a pasta** do projeto:
    ```bash
    cd seu-repositorio
    ```

3.  **Execute o script** Python. As janelas dos gráficos aparecerão uma após a outra.
    ```bash
    python seu_script.py
    ```

---

## 💡 Ideias para Melhorias Futuras

Este projeto é um ótimo ponto de partida! Algumas ideias para expandi-lo:

* [ ] Adicionar um gráfico de **médias móveis** para suavizar a linha de tendência.
* [ ] Usar a biblioteca `pandas` para uma manipulação de dados mais robusta.
* [ ] Buscar os dados em tempo real de uma API de finanças.
* [ ] Criar uma interface gráfica simples com `Tkinter` ou `PyQt` para selecionar o período de análise.

---

## 👨‍💻 Autor

Feito por **[Eugenio Santana]**.

