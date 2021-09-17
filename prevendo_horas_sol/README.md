Regressão Linear - Previsão de horas de sol em Sydney
==============================
![](https://www.sydney.com/sites/sydney/files/styles/landscape_992x558/public/2019-10/164154_0.jpg)

Essa analise tem o objetivo de aprendermos de forma básica como aplicar um modelo de regressão lienar para prever um valor.


Fonte de Dados
-----------

Para esse analise, a fonte de dados utilizada foi a [Rain in Australia](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package) hospedada no [Kaggle](https://www.kaggle.com/).

Realizei um ETL dentro da base original e temos esse detalhamento dentro desse arquivo: `ETL_data.ipynb`. 
Segue um breve detalhamento do que é realizado:
```
#Cria uma coluna de ano
df['year'] = pd.to_datetime(df['Date']).dt.year

#Faz um filtro entre 2014 e 2016 e que a cidade seja Sydney
s = (((df['year'] >= 2014) & (df['year'] <= 2016) ) & (df['Location'] == 'Sydney'))

#Limita as colunas para as que precisamos
["Date", "Location","MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine", "RainToday"]

#Ajusta a coluna RainToday para 0 ou 1
df['RainToday'] = np.where(df['RainToday'] == 'No', 0, 1)

#Drop valores nulos no DF
df = df.dropna()

# Salva novo arquivo
df.to_csv('rain_sydney.csv', sep=';', index=False)
```

Instruções de Uso
-----------
### Ambiente Conda
Para executar essa analise, será necessário ter um abiente conda. Sugiro o download do [Anaconda Navigator](https://www.anaconda.com/distribution/) caso não tenha um ambiente já configurado.

### Dependência de Uso
Essa analise contém dependencias de uso. Antes de executar os scripts, faça a instalação.

`$ pip install -r requirements.txt`

### Execução

- Para explorar a analise realizada, execute o arquivo `LR_Rain_Sydney.ipynb`.
- Para Apenas consumir o modelo gerado, execute o arquivo `testing_model.ipynb`. Será necessário passar os valores que deseja provisionar:
`valores = [[10.9, 20.8, 4.2, 0.2, 0]]`
- Para entender o ETL, execute o arquivo `ETL_data.ipynb`. Ele espera um arquivo de entrada com o nome `weatherAUS.csv`. 
