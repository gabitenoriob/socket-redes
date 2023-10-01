# Conexão via Sockets

Um projeto  que demonstra o poder e as funcionalidades do uso de sockets e threadings em Python, como ferramenta de conexão entre duas maquinas visando executar um programa que faça-os interagir dinâmicamente

## Propósito
* Trabalho na Disciplina de Redes de Computadores, professor Almir Pereira Guimarães, 3ºperíodo.

* Jogo clássico nomeado "Jogo Da Velha" usando socket de conexão UDP

---
### COMO RODAR A APLICAÇÃO

### Função "Host_Game"
```
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", port)) 
        server.listen(1)
```
  * Passamos como parâmetro "Self" que é a instância do objeto criado na função anterior a essa, esse objeto aloca os componentes do jogo
    
  * Passamos HOST e PORT que vão ser passados como parâmetro, se estivermos a nível de uso em LAN( Land Area Network ) HOST sera o IP do 
     servidor que está rodando o programa e PORT será a Porta que esse servidor vai querer usar.
    
  * *SOCKET.SOCKET()* essa instancia do objeto socket, cria um Socket com determinadas caracteriticas, que pode-se passar como parametro, no caso, precisaremos passar socket.AF_INET socket.SOCK_STREAM, indicam o endereço da rede será do tipo IPV4 e que vai usar TCP/IP protocol.
  * *SOCKET.BIND()* essa instancia do objeto socket, associa estrutura socket e o endereço/porta do servidor
  * *SOCKET.LISTEN()* essa instancia do objeto socket, o servidor entra no estado de aguardar por alguma solicitação de clientes que desejam se comunicar,recebe como parâmetro  a quantidade de conexões que serão permitidas pelo protocolo TCP, esse número depende do tipo de aplicação e capacidade do servidor.
  * *SOCKET.ACCEPT()* essa instancia do objeto socket, aceita o cliente que está tentando se conectar e retorna uma tupla, que indica o endereço do cliente que solicitou a conexão


      ############### escrevi ate aqui somente ##################
## Lógica Matemática por Trás do Problema

Precisamos pensar nos cálculos em função de P, pois esse é o valor que vai ser atualizado a todo momento, lembrando que 0 < P < 1.

- Minha função vai definir a velocidade com que o P cresce.
  
- Mas para nossa barra funcionar, a função precisa respeitar as seguintes regras:

      Quando P = 0, f(p) = 0
      Quando P = 1, f(p) = 1
      A inclinacao da curva precisa comecar mais acentuada e terminar mais branda

- Pensei em usar uma função do segundo grau, você também pode usar uma função exponencial, porém acho que é bem mais fácil usar uma função do segundo grau em JavaScript.

### Usando x^2 + 2x, temos:

<p align="center">
  <img src="/krl.png" alt="Texto alternativo da imagem" width="600">
</p>


       - Note que quando x = 0, f(x) passa pela origem
       - Note tambem que, quando x = 1, f(x) = 1
       - A concavidade eh virada para baixo, pois dessa maneira, dentro do intervalo entre 0 e 1, a funcao eh crescente.
  
  
---

## Criando o Player

No trecho de código abaixo, eu simplesmente pego a div do player e configuro a página para exibir o vídeo. Para obter mais detalhes, consulte a documentação do React Player, que foi a biblioteca que eu usei neste projeto -> [Documentação do React Player](https://www.npmjs.com/package/react-player)

```
<div className="playerWrapper">
        <ReactPlayer
          playing
          onDuration={(d) => setDuration(d)}
          progressInterval={100}
          onProgress={(p) => {
            setPlayed(p.playedSeconds);
            setLoaded(p.loadedSeconds);
          }}
          config={{
            youtube: {
              playerVars: { showinfo: 1 },
            },
          }}
          url="https://www.youtube.com/watch?v=YLslsZuEaNE"
          controls={true} // Adicione esta linha para exibir os controles, incluindo a barra de volume
        />

```

## Inserindo a Barra de Progressão Modificada

Como mencionei anteriormente, a barra de progressão pode ser feita dividindo o instante atual do vídeo pela duração total do mesmo. Estou chamando uma função que será explicada abaixo e passando como parâmetro um número entre 0 e 1 que representa quanto do vídeo já foi consumido. Essa função é chamada milhares de vezes em um único minuto, dando o efeito de uma barra progredindo.


```
<ProgressBar progress={barra_de_progressao(played / duration)}>
          <div />
        </ProgressBar>
```

## A Função
A função é dada por


```
function barra_de_progressao(x) {
  return -(x * x)+(2*x)
}
```
### Resumo
É incrível como esse problema consegue ser ao mesmo tempo complexo, a ponto de exigir conhecimento em diferentes áreas para ser resolvido. No entanto, sua aplicação se baseia em uma função de apenas 1 linha.
