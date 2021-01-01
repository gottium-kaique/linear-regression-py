# Porque eu fiz esse código

Esse código apesar de muito simples, muitas pessoas não tentam fazer sem auxílio de um framework.
Eu prefiro entender as coisas por debaixo dos panos.

# O que é Regressão Linear?

Você que quer entrar no mundo da Inteligência Artificial, você vai ouvir falar da Regressão Linear, 
Imagine que você tem uma gráfico de uma função, em que x é [1, 2, 3] e y [2, 4, 6], se você perceber 
você pode fazer uma linha que passa entre esses pontos. Mais você deve estar se perguntando, porque 
vou usar isso se posso usar razões. 

A Regressão Linear não precisa ser números totalmente contínuos, já para prever algum número com 
frações é preciso que os todos os números tenham um padrão. 

Então..., continuando você deve ter percebido que se pode fazer uma linha nesse gráfico, tem um 
método muito usado para descobrir qual é essa linha, que é Regressão Linear, ele ajuda muito em 
problemas desse tipo.

Vamos como nós calculamos essa reta?

Para isso tem algumas fórmulas que ajudam nisso.

α = (n Σ XiYi - Σ Xi Σ Yi) / (n Σ Xi² - (Σ Xi)²)

α -> Coeficiente Angular
n -> Números de dados x ou y
X -> Entrada de dados no eixo X
Y -> Entrada de dados no eixo Y


β = Ym - α.Xm


Ym -> Média do y

Xm -> Média do x

Ym = 1/n Σ Yi
Xm =  1/n Σ Xi

f(x) = αx + β
f(x) -> Reta que tenta passar no meio desses pontos.

Pronto, simples, e você já tem uma linha feita com a Regressão Linear.

Eu usei Ym e Xm nas fórmulas, mas normalmente para indicar a média desses números vai aparecer 
um traço em cima.
