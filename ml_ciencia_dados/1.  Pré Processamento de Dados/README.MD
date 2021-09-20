# PRÉ PROCESSAMENTO DE DADOS

A etapa de __pré processamento dos dados__ é uma das princiapsi etapadas para se construir um modelo de Machine learning.

É nesse que passo que vamos fazer todos o tipo de tratativa nos dados, para que fique com o melhor formato possível.

Somente após o tratamento dos dados, que podemos seguir para a construção do modelo.

## Tipos de Variáveis

### Variáveis Numéricas

* __Contínua__: Geralmente do tipo float. Números reais (85.50, 96.30). _Exemplo: Temperatura, alturaa, peso, salário._

* __Discreta__: Conjunto de valores finito, do tipo inteiro. Geralmente é contagem de alguma coisa.

### Variáveis Categóricas _String_

* __Nominal__: Dados não mensuráveis, não possuem uma ordenação. _Exemplo: gênero, cor dos olhos, uf, id, nome._

* __Ordinal__: Categorização sob uma ordenação. _Exemplo: tamanhos._

## Divisão entre Previsores e Classe

* Quais são os atributos da base que se indentificam como previsores _ajudam a prever_?

* Qal é o atributo que classifica a base? 

* Variáveis previsoras: X_nm_var
* Variável de classe: Y_nm_var

```
X_variaveis = nome_dataframe.loc[:, ['var_name', 'var_name2']].values

Y_variaveis = nome_dataframe.loc[:, ['var_name']].values

```

## Escalonamento dos Valores

É importante aplicar a padronização dos dados, pois os modelos de Machine Learning trabalham com numeros e oeprações matenáticas, logo, valores maiores, pesos maiores. Isso pode enviezar seu modelo considerando que uma variável é mais importante que outra.

__PADRONIZAÇÃO (STANDARDISATION)__
<br> _--> Indicada para quando temos outliers na base de dados._
<br>``` x = ( x = média(x) ) / desvio padrão(x) ```

```
from sklearn.preprocessing import StandardScaler
scaler_census = StandardScaler()
X_variaveis = scaler_credit.fit_transform(X_variaveis)
```


__NORMALIZAÇÃO (NORMALIZATION)__

``` x = ( x - minimo(x) ) / ( maximo(x) - minimo(x) ) ```