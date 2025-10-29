# ----------- BATALHA NAVAL -----------

# tabuleiros do jogador e computador inicialmente vazios
tabuleiro_jogador = [[' ' for i in range(10)] for i in range(10)]
tabuleiro_computador = [[' ' for i in range(10)] for i in range(10)]
tabuleiro_simula_comp = [[' ' for i in range(10)] for i in range(10)]
# embarcações: 1 de 5 casas, 1 de 4 casas, 1 de 3 casas e 2 de 2 casas
# As posições verticais do tabuleiro são organizadas da esquerda para a direita começando do 0 até 9
# As posições horizontais do tabuleiro começam de cima para baixo começando do 0 até 9
# ------------------------------------------------------
from funcoes_batalha_naval import colocar_embarcacao
from funcoes_batalha_naval import colocar_embarcacao_aleatoria
from funcoes_batalha_naval import mostra_tabuleiro
from funcoes_batalha_naval import comecar_partidada
#importei todas as funçoes que irei utilizar do file: funcoes_batalha_naval

print('---------------------------BEM VINDO AO JOGO BATALHA NAVAL!')
print('VAMOS COMEÇAR COLOCANDO SUA EMBARCAÇOES NO SEU TABULEIRO:')
print(' nesse jogo teremos 1 barco de 5 lugares , 1 de 4 lugares , 1 de 3 lugares e 2 de 2 lugares ')
print('esse é o seu tabuleiro :')
print("\nTabuleiro do jogador atual:")
mostra_tabuleiro(tabuleiro_jogador) 
#mostrei o tabuleiro e seus limites 

print(' agora vamos colocar seus barcos ')
print('lembrando o x é a coordenada  de cima para baixo ( VERTICALMENTE ) e a y é da esquerda para direita(HORIZONTALMENTE )')
print('começando com o barco de 5 lugares: ')  #chamei a funçâo colocar_embarcação para um barco que ocupa 5 posiçoes no tabuleiro 
colocar_embarcacao(tabuleiro_jogador, tamanho=5, simbolo='^')  
print('agora o barco de 4 lugares: ')  #4 posiçoes
colocar_embarcacao(tabuleiro_jogador, tamanho=4, simbolo='^')
print('agora o barco de 3 lugares : ')  #3 posiçoes
colocar_embarcacao(tabuleiro_jogador, tamanho=3, simbolo='^')
print('agora o primeiro barco de 2 lugares ')  #2 posiçoes 
colocar_embarcacao(tabuleiro_jogador, tamanho=2, simbolo='^')
print('agora o segundo barco de 2 lugares ')  #2 posiçoes
colocar_embarcacao(tabuleiro_jogador, tamanho=2, simbolo='^')

print('Seu tabuleiro foi formado com sucesso: ')
mostra_tabuleiro(tabuleiro_jogador) #mostra o tabuleiro com os barcos nos devidos lugares 

#agora crio o tabuleiro do computador e coloco aleatoriamente os barcos nele 
colocar_embarcacao_aleatoria(tabuleiro_computador,tamanho=5,simbolo='*')
colocar_embarcacao_aleatoria(tabuleiro_computador,tamanho=4,simbolo='*')
colocar_embarcacao_aleatoria(tabuleiro_computador,tamanho=3,simbolo='*')
colocar_embarcacao_aleatoria(tabuleiro_computador,tamanho=2,simbolo='*')
colocar_embarcacao_aleatoria(tabuleiro_computador,tamanho=2,simbolo='*')
#explicando para o usuario como vai funcionar 
print('------------------------------------------------------------------------------------------------------------------------------------------')
print('Expliicaçôes: ')
print('Você vai jogar contra o computador, a cada rodada  você escolhe uma posição do tabuleiro dele para atacar e ele escolherá uma posição para te atacar')
print(' cada começo de rodada será mostrado para você o seu tabuleiro, no qual os barcos serâo identificados pelo simbolo "^" ')
print(' e cada tentativa errada do computador  sera marcada como "~" no seu tabuleiro, porém se ele acertar o simbolo que antes era "^" se torna "X" mostrando q ele acertou seu barco')
print('alem disso , para vacê será mostrado um tabuleiro do mesmo tamanho , simulando o tabuleiro do computador para você se organizar nas coordenadas que usar, a cada tentativa sua, será marcado um simbolo na posiçao escolhida:')
print('se estiver marcado "X" quer dizer q vc acertou uma posição do barco inimigo , se estiver marcado "~" quer dizer q vc nao acertou um barco ' )
print(" -------------- ATENÇÃO SE VOCÊ ESCOLHER UMA CASA QUE JA TINHA ESCOLHIDO ANTERIORMENTE SEM QUERER , VOCÊ IRÁ PERDER A VEZ ----------------------")

comecar_partidada(tabuleiro_jogador,tabuleiro_computador,tabuleiro_simula_comp)

# ------------------------------------------------------

