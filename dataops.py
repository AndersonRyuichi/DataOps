#install pymongo
#install pandas

import pymongo
import pandas as pd

def main():
    # Dados carros
    dados_carros = {
        'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
        'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
        'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
    }
    df_carros = pd.DataFrame(dados_carros)
    print("DataFrame Carros:")
    print(df_carros)

    # Dados montadoras
    dados_montadoras = {
        'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
        'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']
    }
    df_montadoras = pd.DataFrame(dados_montadoras)
    print("\nDataFrame Montadoras:")
    print(df_montadoras)

    # Conexão MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    local_database = client['local']
    Carros_collection = local_database['Carros']
    Montadoras_collection = local_database['Montadoras']

    # Inserir dados
    Carros_collection.insert_many(df_carros.to_dict(orient="records"))
    Montadoras_collection.insert_many(df_montadoras.to_dict(orient="records"))
    print("\nDados inseridos no MongoDB com sucesso!")

    # Lookup básico + projeção
    montadoras_lookup = {
        "$lookup": {
            "from": "Montadoras",
            "localField": "Montadora",
            "foreignField": "Montadora",
            "as": "Montadoras"
        }
    }
    projecao = {
        "$project": {
            "_id": 1,
            "Carro": 1,
            "Cor": 1,
            "Montadora": 1,
            "Montadoras": 1,
            "Pais": {
                "$arrayElemAt": ["$Montadoras.País", 0]
            }
        }
    }

    agrupamento = {
        "$group": {
            "_id": "$Pais",
            "Carros": {
                "$push": {
                    "Carro": "$Carro",
                    "Cor": "$Cor",
                    "Montadora": "$Montadora"
                }
            }
        }
    }

    # Pipeline agregação simples (lookup + projecao)
    pipeline_simples = [montadoras_lookup, projecao]
    resultados_simples = Carros_collection.aggregate(pipeline_simples)
    resultados_simples_list = list(resultados_simples)

    print("\nResultado da agregação simples (lookup + projeção):")
    for doc in resultados_simples_list:
        print(doc)

    # Pipeline agregação com agrupamento
    pipeline_completo = [montadoras_lookup, projecao, agrupamento]
    resultados_group = Carros_collection.aggregate(pipeline_completo)
    resultados_group_list = list(resultados_group)

    print("\nResultado da agregação completa (agrupado por País):")
    for doc in resultados_group_list:
        print(doc)

if __name__ == "__main__":
    main()