# 📦 Avaliação DataOps

Este repositório contém a solução completa da avaliação técnica para a área de **DataOps**, desenvolvida utilizando **Python**, **pandas** e **MongoDB**, com foco em persistência de dados, consulta, agregação e agrupamento.

---

## 📂 Estrutura do repositório

| Arquivo | Descrição |
| ------- | --------- |
| **`dataops.py`** | Script Python principal. Cria e popula as collections `Carros` e `Montadoras` no MongoDB, realiza agregações (`lookup`, projeção e agrupamento) e imprime os resultados no terminal. Código estruturado para execução standalone. |
| **`DataOps.ipynb`** | Versão em **Jupyter Notebook** do trabalho, contendo o desenvolvimento passo a passo e explicações visuais. Facilita a leitura interativa e documentação didática do processo. |
| **`Agregação_e_Agrupamento.js`** | Arquivo contendo os **resultados da agregação e do agrupamento**, representados em formato JSON, conforme extraído das consultas realizadas. Serve como evidência do funcionamento correto da lógica de agregação no MongoDB. |
| **`local.Carros.json`** | Exportação da collection `Carros` do MongoDB, em formato JSON. Permite importação direta (`mongoimport`) e reuso dos dados. |
| **`local.Montadoras.json`** | Exportação da collection `Montadoras` do MongoDB, em formato JSON. Permite importação direta (`mongoimport`) e reuso dos dados. |
| **`Finalização.txt`** | Documento com autoavaliação e descrição do desempenho na execução da atividade, destacando pontos fáceis, medianos e difíceis. Demonstra reflexão crítica sobre o desenvolvimento. |

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
