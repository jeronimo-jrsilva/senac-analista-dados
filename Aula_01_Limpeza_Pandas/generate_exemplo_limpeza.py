import pandas as pd
import numpy as np

# 1. Gerar semente determinística
seed = 42
np.random.seed(seed)

n_registros = 50
produtos = ["Smartphone", "Notebook", "Tablet", "Smartwatch"]
precos_base = {"Smartphone": 1500.0, "Notebook": 3200.0, "Tablet": 1000.0, "Smartwatch": 750.0}

registros = []
for i in range(1, n_registros + 1):
    prod = np.random.choice(produtos)
    qtd = float(np.random.randint(1, 5))
    
    # Colocar nulos determinísticos
    if i in [5, 12, 23, 34, 45]:
        qtd = np.nan
        
    valor_unit = precos_base[prod] * np.random.uniform(0.95, 1.05)
    if i in [8, 19, 41]:
        valor_unit = np.nan
        
    desconto = float(np.random.choice([0.0, 0.05, 0.10, 0.15]))
    if i in [3, 15, 27, 31, 39, 48]:
        desconto = np.nan
        
    categoria = np.random.choice(["VIP", "vip", "Vip", "Regular", "regular", np.nan])
    fidelidade = int(np.random.randint(100, 1000))
    
    registros.append({
        "id_venda": i,
        "produto": prod,
        "quantidade": qtd,
        "valor_unitario": round(valor_unit, 2) if not np.isnan(valor_unit) else np.nan,
        "desconto": desconto,
        "categoria_cliente": categoria,
        "pontuacao_fidelidade": fidelidade
    })

df = pd.DataFrame(registros)

# Inserir 1 outlier extremo de digitação
df.loc[14, "valor_unitario"] = 150000.0 # Linha de ID 15

# Inserir 5 duplicatas completas (linhas idênticas)
duplicatas = df.iloc[[2, 10, 25, 33, 44]].copy()
df = pd.concat([df, duplicatas], ignore_index=True)

# Embaralhar para ficar natural, mas de forma determinística
df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

df.to_csv("exemplo_limpeza.csv", index=False)
print("exemplo_limpeza.csv gerado com sucesso!")
