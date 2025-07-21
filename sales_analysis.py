import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Importação do Seaborn para garantir estilos

# Configuração do estilo dos gráficos
plt.style.use('seaborn-v0_8')  # Estilo compatível com Matplotlib recente

# 1. Criação de um dataset fictício de vendas
data = {
    'order_id': range(1, 101),
    'date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'produto': np.random.choice(['Notebook Samsung', 'Celular samsung', 'Tablet Apple', 'Fone'], 100),
    'category': np.random.choice(['Electronicos', 'Accessorios'], 100),
    'price': np.random.uniform(50, 2000, 100).round(2),
    'quantity': np.random.randint(1, 5, 100).astype(float),  # Converter para float
    'customer_id': np.random.randint(1000, 1100, 100),
    'region': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 100)
}
# Adicionando alguns dados faltantes e outliers para simular cenário real
data['price'][10:15] = np.nan
data['quantity'][20:25] = np.nan  # Agora funciona com quantity como float
data['price'][30] = 5000  # Outlier
df = pd.DataFrame(data)

# 2. Limpeza de Dados
def clean_data(df):
    print("=== Iniciando Limpeza de Dados ===")
    
    # Verificar valores ausentes
    print("\nValores ausentes iniciais:")
    print(df.isnull().sum())
    
    # Preencher valores ausentes
    df['price'] = df['price'].fillna(df['price'].median())
    df['quantity'] = df['quantity'].fillna(df['quantity'].mode()[0])
    
    # Tratar outliers (usando IQR para preço)
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df['price'] < (Q1 - 1.5 * IQR)) | (df['price'] > (Q3 + 1.5 * IQR)))]
    
    # Verificar tipos de dados
    df['date'] = pd.to_datetime(df['date'])
    
    print("\nValores ausentes após limpeza:")
    print(df.isnull().sum())
    print("\nFormato do dataset após limpeza:", df.shape)
    return df

# 3. Análise Exploratória
def exploratory_analysis(df):
    print("\n=== Análise Exploratória de Dados ===")
    
    # Resumo estatístico
    print("\nResumo estatístico:")
    print(df.describe())
    
    # Criar coluna de receita total
    df['total_revenue'] = df['price'] * df['quantity']
    
    # Visualização 1: Vendas por categoria
    plt.figure(figsize=(10, 6))
    df.groupby('category')['total_revenue'].sum().plot(kind='bar')
    plt.title('Receita Total por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Receita Total ($)')
    plt.tight_layout()
    plt.savefig('vendas_por_categoria.png')
    plt.close()
    
    # Visualização 2: Tendência de vendas ao longo do tempo
    df['month'] = df['date'].dt.to_period('M')
    monthly_sales = df.groupby('month')['total_revenue'].sum()
    plt.figure(figsize=(12, 6))
    monthly_sales.plot()
    plt.title('Tendência de Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Receita Total ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tendencia_de_vendas_por_mes.png')
    plt.close()
    
    # Visualização 3: Distribuição de preços por produto
    plt.figure(figsize=(10, 6))
    for produto in df['produto'].unique():
        product_data = df[df['produto'] == produto]
        plt.hist(product_data['price'], bins=20, alpha=0.5, label=produto)
    plt.title('Distribuição de Preços por Produto')
    plt.xlabel('Preço ($)')
    plt.ylabel('Frequência')
    plt.legend()
    plt.tight_layout()
    plt.savefig('distribuicao_de_preco.png')
    plt.close()
    
    # Visualização 4: Vendas por região
    plt.figure(figsize=(10, 6))
    df.groupby('region')['quantity'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribuição de Quantidade Vendida por Região')
    plt.tight_layout()
    plt.savefig('vendas_por_regiao.png')
    plt.close()

# 4. Função principal
def main():
    # Limpar dados
    cleaned_df = clean_data(df)
    
    # Realizar análise exploratória
    exploratory_analysis(cleaned_df)
    
    # Salvar dataset limpo como Excel
    cleaned_df.to_excel('dados_de_vendas.xlsx', index=False)
    print("\nDataset limpo salvo como 'dados_de_vendas.xlsx'")
    print("Gráficos salvos como arquivos PNG")

if __name__ == "__main__":
    main()