# 📦 Avaliação DataOps

Este repositório contém a solução completa do teste técnico de **DataOps**, solicitado no processo seletivo. A proposta consiste no uso de **Python**, **pandas** e **MongoDB**, com foco em manipulação, persistência, agregação e agrupamento de dados.

---

## 📂 Estrutura do repositório

| Arquivo | Descrição |
| ------- | --------- |
| **`README.md`** | Documento de apresentação com explicação sobre a estrutura e instruções de execução. |
| **`AVALIACAO_DATAOPS.docx`** | Documento original do teste, preenchido com as respostas solicitadas, autoavaliação e conclusões. |
| **`dataops.py`** | Script Python principal. Cria os DataFrames, insere os dados no MongoDB, executa a agregação (lookup e projeção) e agrupamento por País, com saída detalhada no terminal. Código estruturado para execução standalone. |
| **`DataOps.ipynb`** | Notebook interativo contendo o desenvolvimento passo a passo, útil para acompanhamento detalhado e reprodutibilidade visual. |
| **`Agregação_e_Agrupamento.js`** | Arquivo com os resultados da agregação e do agrupamento, representando evidência de execução correta. |
| **`local.Carros.json`** | Exportação da collection `Carros` em formato JSON, pronta para reimportação via `mongoimport`. |
| **`local.Montadoras.json`** | Exportação da collection `Montadoras` em formato JSON, pronta para reimportação via `mongoimport`. |
| **`Finalização.txt`** | Reflexão pessoal sobre a execução da atividade, destacando pontos fáceis, medianos e as dificuldades enfrentadas. |

---

## 📝 Descrição geral da solução

- Criação de dois `DataFrames` utilizando pandas:
  - `Carros`: contendo dados de carros, cores e montadoras.
  - `Montadoras`: contendo dados de montadoras e respectivos países.
  
- Persistência dos dados no MongoDB local (`Carros` e `Montadoras` collections).

- Execução de agregações no MongoDB:
  - **Agregação simples:** junção entre collections `Carros` e `Montadoras` utilizando `$lookup` e `$project`.
  - **Agregação com agrupamento:** agrupamento por `País` consolidando os carros de cada montadora no campo `Carros`.

- Exportação das collections para JSON, conforme solicitado.

---

## ⚙️ Como executar o projeto

### 1️⃣ Pré-requisitos
- MongoDB rodando localmente (`localhost:27017`).
- Python 3.x com as bibliotecas necessárias:
  ```bash
  pip install pymongo pandas
