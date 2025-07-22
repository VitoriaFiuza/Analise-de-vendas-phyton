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
    'produto': np.random.choice(['Notebook Samsung', 'Celular Samsung', 'Tablet Apple', 'Fones'], 100),
    'category': np.random.choice(['Electronics', 'Accessories'], 100),
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
    plt.savefig('revenue_by_category.png')
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
    plt.savefig('monthly_sales_trend.png')
    plt.close()
    
    # Visualização 3: Distribuição de preços por produto (subplots alinhados mas independentes)
products = df['produto'].unique()
n_products = len(products)

# Criar figura com subplots
fig, axes = plt.subplots(n_products, 1, figsize=(12, 5 * n_products), sharex=False)  # sharex=False para liberdade nos eixos
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

# Definir bins consistentes para todos os produtos (opcional)
bins = np.linspace(df['price'].min(), df['price'].max(), 15)  # 15 bins com mesmo intervalo

for ax, product, color in zip(axes, products, colors):
    product_data = df[df['produto'] == product]
    ax.hist(product_data['price'], bins=bins, color=color, alpha=0.7, edgecolor='black', linewidth=1.2)
    ax.set_title(f'Distribuição de Preços - {product}', fontsize=12, pad=10)
    ax.set_ylabel('Frequência', fontsize=10)
    ax.set_xlabel('Preço ($)', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.tick_params(axis='both', labelsize=9)
    
    # Destacar média com linha vertical
    mean_price = product_data['price'].mean()
    ax.axvline(mean_price, color='red', linestyle='--', linewidth=1.5, label=f'Média: ${mean_price:.2f}')
    ax.legend()

plt.tight_layout()
plt.savefig('price_distribution_subplots.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Função principal
def main():
    # Limpar dados
    cleaned_df = clean_data(df)
    
    # Realizar análise exploratória
    exploratory_analysis(cleaned_df)
    
    # Salvar dataset limpo como Excel
    cleaned_df.to_excel('cleaned_sales_data.xlsx', index=False)
    print("\nDataset limpo salvo como 'cleaned_sales_data.xlsx'")
    print("Gráficos salvos como arquivos PNG")

if __name__ == "__main__":
    main()