# Problema do Labirinto

Este é um código Python que resolve o problema do labirinto. O programa recebe um labirinto 5x5 representado por uma matriz de inteiros (0 representa um caminho vazio, 1 representa uma parede) e determina se um ladrão pode escapar do labirinto ou não.

## O programa foi desenvolvido em `Python 3.8.` Ele utiliza funções recursivas e não requer nenhuma biblioteca externa.

## Como usar o código
Para usar este código, você deve fornecer os dados do labirinto na entrada padrão do programa.
O labirinto é representado por uma matriz 5x5 de inteiros (0 para caminho livre e 1 para parede).

Depois de fornecer os dados do labirinto, o programa executará a função procura para determinar se a saída pode ser alcançada.

A resposta será exibida na saída padrão do programa.

Exemplo de uso
Suponha que você tenha um labirinto representado por esta matriz:

```Copy code
1 0 0 0 0
1 1 0 0 0
0 1 1 0 0
0 0 1 1 0
0 0 0 1 1
```
Para verificar se um ladrão pode escapar do labirinto, você pode executar o seguinte comando no terminal:


```Copy code
python labirinto.py < input.txt
```

onde input.txt é um arquivo de texto que contém a matriz do labirinto.

O programa retornará a resposta 'ROBBERS', indicando que o ladrão pode escapar do labirinto.

Limitações do código
Este código assume que o labirinto fornecido é uma matriz 5x5 de inteiros. Ele não verifica se os dados fornecidos são válidos ou não. Além disso, este código não fornece informações adicionais sobre como o ladrão pode escapar do labirinto. Ele apenas indica se é possível ou não alcançar a saída.

Licença
Este código é distribuído sob a licença MIT. Sinta-se livre para usá-lo para fins educacionais e pessoais.
