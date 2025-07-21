a# Análise de Vendas - Python

## Descrição
Este projeto realiza uma análise de vendas com dados fictícios, incluindo limpeza de dados e análise exploratória. O script processa um dataset de vendas, trata valores ausentes e outliers, e gera visualizações para entender padrões nos dados. O resultado final é salvo como um arquivo Excel (`cleaned_sales_data.xlsx`).

### Funcionalidades
- **Limpeza de Dados**: Tratamento de valores ausentes e outliers na coluna de preços.
- **Análise Exploratória**:
  - Receita total por categoria (gráfico de barras)
  - Tendência de vendas mensais (gráfico de linha)
  - Distribuição de preços por produto (histograma)
  - Distribuição de quantidade vendida por região (gráfico de pizza)
- **Saída**: Gera um arquivo Excel com os dados limpos (`cleaned_sales_data.xlsx`). As visualizações são salvas como imagens PNG localmente, mas não são incluídas no repositório.

## Estrutura do Projeto
- `sales_analysis.py`: Script principal que realiza a limpeza e análise dos dados.
- `r.txt`: Arquivo com as dependências necessárias.
- `cleaned_sales_data.xlsx`: Exemplo de saída gerada pelo script (dataset limpo).

## Pré-requisitos
As bibliotecas necessárias estão listadas em `r.txt`. Instale-as com:

```bash
pip install -r r.txt
```

As dependências são:
- pandas
- numpy
- matplotlib
- openpyxl

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-de-vendas-python.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd analise-de-vendas-python
   ```
3. Instale as dependências:
   ```bash
   pip install -r r.txt
   ```
4. Execute o script:
   ```bash
   python sales_analysis.py
   ```
5. Verifique a saída:
   - Um arquivo `cleaned_sales_data.xlsx` será gerado com os dados limpos.
   - Quatro gráficos serão salvos localmente como arquivos PNG (não incluídos no repositório).

## Exemplo de Saída
O arquivo `cleaned_sales_data.xlsx` contém o dataset limpo com as seguintes colunas:
- `order_id`: ID do pedido
- `date`: Data do pedido
- `produto`: Nome do produto (NotebookSamsung, CelularSamsung, TabletApple, Fone)
- `category`: Categoria do produto (Electronics ou Accessories)
- `price`: Preço unitário
- `quantity`: Quantidade vendida
- `customer_id`: ID do cliente
- `region`: Região da venda (North, South, East, West)
- `total_revenue`: Receita total (preço * quantidade)

## Notas
- O dataset é fictício e gerado aleatoriamente para simular vendas. Para usar seus próprios dados, modifique a seção de criação do dataset em `sales_analysis.py`.
- Os gráficos gerados (PNG) não estão no repositório, mas são salvos localmente ao executar o script.
- Para personalizar os produtos ou análises, edite a lista de produtos na seção de criação do dataset ou adicione novas visualizações na função `exploratory_analysis`.

## Autor
[Seu Nome] (https://github.com/seu-usuario)

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).