# APRENDENDO SOBRE MACHINELE LEARNING & DATA SCIENCE

## APRENDIZAGEM DE MÁQUINA

| SUPERVISIONADA | NÃO SUPERVISIONADA  | POR REFORÇO |
| :------------: | :-----------------: | :---------: |
| Classificação  | Associação          |             |
| Regressão      | Agrupamento         |             |
|                | Detecção de Desvios |             |
|                | Padrões Sequenciais |             |
|                | Sumarização         |             |

### APRENDIZAGEM SUPERVISIONADA
__Definição:__ A aprendizagem supervisionada ter uma classificação pré definida do que se deseja analisa.

__Exemplo:__ Quero classificar as imagens entre __carro__ e __casa__.

1. Extrair as caracteristicas do que é um carro e do que é uma casa. _(classe)_
2. Subemeter a base de imagens e a classe ao algoritimo de aprendizagem.
3. Por fim temos uma modelo de aprendizagem baseado em uma supervisão.

__Supervisão__: Alguém definiu uma classe/caracteristicas sobre aquilo que se deja analisar, submeteu um conjunto de dados com os itens da classe para o algoritimo e forneceu as classes. Basicamente o modelo analise os dados, extrai as caracteristicas e classifica perante a classe (supervisão).

### APRENDIZAGEM NÃO SUPERVISIONADA
__Definição__: Analisa automaticamente os dados e identifica padrões nos dados _(Sem precisar da classe, supervisão)_. Após o processamento do algoritimo é necessário analisar os resultados encontrados.

__Exemplo__: Quero entender qual item do meu carrinho é comprado junto com outro item.

1. Forneço os dados de compras ao algoritmo. Ele irá processar e criar as associações.
2. Com o outpout do modelo, vamos analisar as associações criadas e com conhecimento de negócio podemos dizer se essas associações fazem sentido ou não.
3. Retro alimento o modelo para que sua change de cada vez mais acertar fique maior.

### APRENDIZAGEM POR REFORÇO
__Definição__: Basicamente é o aprendizado baseado em interações, dado uma interação qual é a causa e qual foi o seu efeito, logo o modelo aprende com sua experiencia. Muito utilizado em robos.

__Exemplo__: Aspirador de pó inteligente.

1. Você compra o robo e coloca ele para aspirar seu apartamento.
2. No primeiro dia ele irá esbarrar em quase todos os moveis e irá coletar as informações de causa e efeito.
3. O robo irá armazenar suas interações com o seu ambiente _(sua casa)_ e irá aprender o ambiente da sua casa.
4. O modelo irá processar esses dados para ter uma acertividade maior em sua limpreza/caminho a ser seguido.
