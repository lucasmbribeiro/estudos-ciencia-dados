# INTRODUÇÃO AOS ALGORITMOS DE CLASSIFICAÇÃO

## NAIVE BAYES

* Tem uma abordagem probabilística.
* É baseado no __teorema de Bayes__.
* Exemplos de aplicações: Filtros de spam, mineração de emoção e separação de documentos.
* __Funciona como classificador e baseia-se na probabilidade de cada evento ocorrer, desconsiderando a correlação entre features.__ [link](https://medium.com/turing-talks/turing-talks-16-modelo-de-predi%C3%A7%C3%A3o-naive-bayes-6a3e744e7986)

__COMO O ALGORITMO APRENDE?__

1. Precisamos capturar um conjunto de dados histórico.
2. Preparamos essa base para que contenham apenas valores númericos.

![](..\Imagens\tabela_naive_bayes.png)
_Imagem retirada do curso Udemy_

3. O algoritmo irá criar uma tabela de probabilidade. É com essa tabela que o algoritmo aprende!

![](..\Imagens\tabela_probabilidade_naive_bayes.png)
_Imagen retirada do curso Udemy_

4. Com a tabela de probabilidade montada, vamos submeter novos registros a serem classificados pelo algoritimo.

* História = Boa
* Dívida = Alta
* Garantias = Nenhuma
* Renda => 35

5. Vamos calcular a estimativa de probabilidade para cada classe.


__P() = Risco de Crédito (probabilidade de acontecer) * História do Crédito * Dívida * Garantias * Renda Anual__

Risco de Crédito __ALTO__
```
P(Alto) = 6/14 * 1/6 * 4/6 * 6/6 * 1/6
P(Alto) = 0,0079
```

Risco de Crédito __MODERADO__
```
P(Moderado) = 3/14 * 1/3 * 1/3 * 2/3 * 1/3
P(Moderado) = 0,0052
```

Risco de Crédito __BAIXO__
```
P(Baixo) = 5/14 * 3/5 * 2/5 * 3/5 * 5/5
P(Baixo) = 0,0514
```

6. Com isso o modelo classificou os inputs como Risco de Crédito __BAIXO__.

7. Podemos converter os valores da probibilidade em porcentagem:
```
1. Soma as probabilidades encontradas

Soma = 0,0079 + 0,0052 + 0,0514

%_Alto = (0,0079 / Soma) * 100 --> 12,24%

%_Moderado = (0,0052 / Soma) * 100 --> 8,06%

%_Baixo = (0,0514 / Soma) * 100 --> 79,68%

```

### Correlação Laplaciana

Quando temos um coluna com valor zero (0), faz com que a multiplicação fique zerada. Vamos precisar ajustar para quando isso aconteça.

* Correção para evitar multiplicação por valores zerado.
* Basicamente, onde temos valores zerados, vamos adicionar 1.
* Isso é ajustado para as linhas e colunas que o valor zero está. Se tinhamos 4 registros, passamos a ter 5 e assim por diante, tanto para linha quanto para coluna! 