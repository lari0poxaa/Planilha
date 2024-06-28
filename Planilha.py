import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    'Data': [
        '01/06/2024', '15/06/2024', '30/06/2024', # Receitas
        '02/06/2024', '05/06/2024', '10/06/2024', '12/06/2024', '18/06/2024', '22/06/2024', '28/06/2024' # Gastos
    ],
    'Valor': [
        5000, 2500, 3000, # Receitas
        -200, -150, -300, -100, -50, -400, -250 # Gastos
    ],
    'Categoria': [
        'Receita', 'Receita', 'Receita', # Receitas
        'Alimentação', 'Transporte', 'Lazer', 'Educação', 'Saúde', 'Roupas', 'Alimentação' # Gastos
    ]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Separando receitas e gastos
receitas = df[df['Categoria'] == 'Receita']
gastos = df[df['Categoria'] != 'Receita']

# Plotando o gráfico
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Gráfico de receitas e gastos
ax[0].bar(receitas['Data'], receitas['Valor'], label='Receitas', color='green')
ax[0].bar(gastos['Data'], gastos['Valor'], label='Gastos', color='red')
ax[0].set_title('Receitas e Gastos')
ax[0].set_ylabel('Valor (R$)')
ax[0].legend()

# Gráfico de gastos por categoria
categorias = gastos.groupby('Categoria').sum().reset_index()
ax[1].bar(categorias['Categoria'], categorias['Valor'], color='orange')
ax[1].set_title('Gastos por Categoria')
ax[1].set_ylabel('Valor (R$)')
ax[1].set_xlabel('Categoria')

# Ajuste e exibição dos gráficos
plt.tight_layout()
plt.show()

# Salvar o DataFrame em um arquivo Excel
file_path = "/mnt/data/receitas_e_gastos.xlsx"
df.to_excel(file_path, index=False)

file_path
