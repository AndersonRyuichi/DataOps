# 📦 Avaliação DataOps

Este repositório contém a solução completa da avaliação técnica para a área de **DataOps**, desenvolvida utilizando **Python**, **pandas** e **MongoDB**, com foco em persistência de dados, consulta, agregação e agrupamento.

---

## 📂 Estrutura do repositório

| Arquivo | Descrição |
| ------- | --------- |
| **`dataops.py`** | Script Python principal que cria e popula as collections `Carros` e `Montadoras` no MongoDB, realiza as agregações e imprime os resultados no terminal. |
| **`DataOps.ipynb`** | Notebook interativo com todo o desenvolvimento, explicações e execução dos passos da avaliação. |
| **`Agregação_e_Agrupamento.js`** | Arquivo com os resultados extraídos das consultas de agregação e agrupamento, servindo como evidência de execução correta. |
| **`local.Carros.json`** | Exportação da collection `Carros` em formato JSON. |
| **`local.Montadoras.json`** | Exportação da collection `Montadoras` em formato JSON. |
| **`Finalização.txt`** | Documento com análise pessoal de desempenho, destacando pontos fáceis, medianos e difíceis encontrados durante a atividade. |
| **`AVALIACAO_DATAOPS.docx`** | Documento original da avaliação contendo a descrição do desafio, instruções e a autoavaliação respondida no ínicio e no final. |


---

## 📝 Detalhes da solução

### 📊 **Fluxo implementado**
- Criação de `DataFrame` com dados de carros e montadoras.
- Conexão e persistência dos dados no MongoDB local.
- Execução de agregações MongoDB:
  - **Agregação simples:** lookup + projeção para incluir `País` no resultado.
  - **Agregação completa:** agrupamento por `País` consolidando veículos em array `Carros`.

---

## ⚙️ Como executar

### 1️⃣ Pré-requisitos:
- MongoDB em execução local na porta `27017`.
- Python 3.x com bibliotecas:
  ```bash
  pip install pymongo pandas
