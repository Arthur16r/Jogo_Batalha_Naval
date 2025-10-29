def colocar_embarcacao(tabuleiro, tamanho, simbolo='^'):
    """
    Função para posicionar uma embarcação no tabuleiro.

    tabuleiro: representa em qual tabuleiro sera colocado essas posiçoes 
    tamanho: tamanho da embarcação 
    simbolo: caractere usado para marcar a embarcação
    """
    while True:
        try: #para impoedir erro 
            print(f"\nDigite a posição inicial da embarcação de tamanho {tamanho}:")  #decide a posição inicial
            posicao_inicial_x = int(input("x: "))
            posicao_inicial_y = int(input("y: "))

            if tabuleiro[posicao_inicial_x][posicao_inicial_y] != ' ': #confere se a posição inicial ja esta ocupada por outro barco 
                print(" Essa posição já está ocupada. Escolha outra.")
                continue

            colocado = False #serve para controlar se deu certo ou não colocara aembarcação no tabuleiro 

            while not colocado: #enquanto a embarcação nao for posta no tabuleiro 
                print("\nEscolha a direção:")
                print("1 - Para cima")
                print("2 - Para baixo")
                print("3 - Para direita")
                print("4 - Para esquerda")
                print("5 - Mudar posição inicial")

                sentido = int(input("Digite o número da direção: "))
                cabe = True #variavel para verificar se o sentido escolhido cabe dentro do tabuleiro 

                match sentido: 
                    case 1:  # Para cima
                        if posicao_inicial_x - (tamanho - 1) < 0: #verifica se ultrapassa o limite do tabuleiro para cima 
                            cabe = False
                        else:
                            for i in range(tamanho): #se não ultrapassa , confere se todas as posiçoes do sentido escolhido esta livre
                                if tabuleiro[posicao_inicial_x- i][posicao_inicial_y] != ' ':
                                    cabe = False
                                    break
                            if cabe: #se todos esses if estiverem incorretos quer dizer que o barco no sentido escolhido cabe no tabuleiro , logo agora é so adicionar os simbolos
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x- i][posicao_inicial_y] = simbolo
                                colocado = True

                    case 2:  # Para baixo
                        if posicao_inicial_x + (tamanho - 1) > len(tabuleiro) - 1:#verifica se ultrapassa o limite do tabuleiro para baixo
                            cabe = False
                        else:
                            for i in range(tamanho):#se não ultrapassa , confere se todas as posiçoes do sentido escolhido esta livre
                                if tabuleiro[posicao_inicial_x + i][posicao_inicial_y] != ' ':
                                    cabe = False
                                    break
                            if cabe:#se todos esses if estiverem incorretos quer dizer que o barco no sentido escolhido cabe no tabuleiro , logo agora é so adicionar os simbolos
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x + i][posicao_inicial_y] = simbolo
                                colocado = True

                    case 3:  # Para direita
                        if posicao_inicial_y + (tamanho - 1) > len(tabuleiro[0]) - 1:#verifica se ultrapassa o limite do tabuleiro para direita
                            cabe = False
                        else:
                            for i in range(tamanho): #se não ultrapassa , confere se todas as posiçoes do sentido escolhido esta livre
                                if tabuleiro[posicao_inicial_x][posicao_inicial_y + i] != ' ':
                                    cabe = False
                                    break
                            if cabe:#se todos esses if estiverem incorretos quer dizer que o barco no sentido escolhido cabe no tabuleiro , logo agora é so adicionar os simbolos
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x][posicao_inicial_y + i] = simbolo
                                colocado = True

                    case 4:  # Para esquerda
                        if posicao_inicial_y - (tamanho - 1) < 0:#verifica se ultrapassa o limite do tabuleiro para esquerda
                            cabe = False
                        else:
                            for i in range(tamanho):#se não ultrapassa , confere se todas as posiçoes do sentido escolhido esta livre
                                if tabuleiro[posicao_inicial_x][posicao_inicial_y - i] != ' ':
                                    cabe = False
                                    break
                            if cabe:#se todos esses if estiverem incorretos quer dizer que o barco no sentido escolhido cabe no tabuleiro , logo agora é so adicionar os simbolos
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x][posicao_inicial_y - i] = simbolo
                                colocado = True

                    case 5: # Sai do loop da direção e volta a pedir nova posição inicial
                        print(" Mudando posição inicial...")
                        break

                    case _: #se escolher algum case que não existe 
                        print(" Direção inválida.")
                        continue

                

                if not cabe: # se o barco não cabe no tabuleiro
                    print(" A embarcação não cabe nessa direção.")
                
                # Exibe o tabuleiro após cada tentativa
                print("\nTabuleiro do jogador atual:")
                mostra_tabuleiro(tabuleiro)

            if colocado:
                print("✅ Embarcação colocada com sucesso!")
                break  # Sai do loop principal (navio colocado)

        except (ValueError, IndexError):
            print(" Entrada inválida. Tente novamente.")


def mostra_tabuleiro(tabuleiro): #exibe o tabuleiro desejado 
    print("\n    0 1 2 3 4 5 6 7 8 9")
    print("   ---------------------")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} | " + " ".join(linha))
    print()


import random 


def colocar_embarcacao_aleatoria(tabuleiro, tamanho, simbolo='*'):  #é a mesma lógica da função que permite o jogador escolher os lugares , porem as posições aqui sao geradas aleatoriamente
    '''funçao para colocar os barcos do computador aleatoriamente 
        usa a mesma base da funcao colocar embarcacao , so q agr tudo 
        randomizado
    '''
    colocado=False
    while not colocado:
            posicao_inicial_x = random.randint(0,len(tabuleiro)-1)
            posicao_inicial_y = random.randint(0,len(tabuleiro[0])-1)

            sentido = random.randint(1,4)
            cabe = True

            match sentido:
                    case 1:  # Para cima
                        if posicao_inicial_x - (tamanho - 1) < 0:
                            cabe = False
                        else:
                            for i in range(tamanho):
                                if tabuleiro[posicao_inicial_x- i][posicao_inicial_y] != ' ':
                                    cabe = False
                                    break
                            if cabe:
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x- i][posicao_inicial_y] = simbolo
                                colocado = True

                    case 2:  # Para baixo
                        if posicao_inicial_x + (tamanho - 1) > len(tabuleiro) - 1:
                            cabe = False
                        else:
                            for i in range(tamanho):
                                if tabuleiro[posicao_inicial_x + i][posicao_inicial_y] != ' ':
                                    cabe = False
                                    break
                            if cabe:
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x + i][posicao_inicial_y] = simbolo
                                colocado = True

                    case 3:  # Para direita
                        if posicao_inicial_y + (tamanho - 1) > len(tabuleiro[0]) - 1:
                            cabe = False
                        else:
                            for i in range(tamanho):
                                if tabuleiro[posicao_inicial_x][posicao_inicial_y + i] != ' ':
                                    cabe = False
                                    break
                            if cabe:
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x][posicao_inicial_y + i] = simbolo
                                colocado = True

                    case 4:  # Para esquerda
                        if posicao_inicial_y - (tamanho - 1) < 0:
                            cabe = False
                        else:
                            for i in range(tamanho):
                                if tabuleiro[posicao_inicial_x][posicao_inicial_y - i] != ' ':
                                    cabe = False
                                    break
                            if cabe:
                                for i in range(tamanho):
                                    tabuleiro[posicao_inicial_x][posicao_inicial_y - i] = simbolo
                                colocado = True

import time 

def comecar_partidada(tabuleiro_jog,tabuleiro_comp,tabuleiro_simu): #a função para iniciar oficialmente a batalha 
    print('------------------VOCÊ DESEJA JOGAR NO MODO TESTE(O TABULEIRO DO ADVERSARIO FICARA VISIVEL PARA VOCÊ)?')# como solicitado essa decisão serve para entrar no modo de testes 
    teste=int(input('Digite 1 se deseja ativar essa opção, se não digite qualquer outro numero '))
    print('---------------------VAMOS COMEÇAR A JOGAR---------------------------')
    print('O PRIMEIRO QUE DERRUBAR TODOS OS BARCOS PERDE')
    pontos_jogador=0
    pontos_computador=0
    while pontos_computador < 16 and pontos_jogador <16: #começa as rodadas dos tiros e so termina quando alguem atingir 16 pontos , acertar 1 vez um barco da 1 ponto , logo precisa derrubar tds os barcos para ganhar 
            print('ecolha a posição q deseja atacar')
            posicao_atacar_x=int(input('x(0 ate 9): '))
            posicao_atacar_y=int(input('y(0 ate 9): '))
            if posicao_atacar_x >= 0 and posicao_atacar_x <= 9 and posicao_atacar_y <= 9 and posicao_atacar_y >= 0 : 
                print(f' a posição que vc deseja atacar é :{posicao_atacar_x},{posicao_atacar_y}')
                if tabuleiro_comp[posicao_atacar_x][posicao_atacar_y] =='*' :
                    pontos_jogador+=1
                    print('VOCE ACERTOU UM BARCO!!!!!')
                    tabuleiro_simu[posicao_atacar_x][posicao_atacar_y]='X'
                    print('como acertou , você pode jogar novamente ') #como solicitado se vc acertou um barco vc joga novamente 
                    continue
                else:
                    print(' VOCE NAO ACERTOU NENHUM BARCO ')
                    tabuleiro_simu[posicao_atacar_x][posicao_atacar_y]='~'
            else:
                print('posição invalida!')
                continue
            print('VEZ DO COMPUTADOR espere........') # com eça a rodada do computador 
            time.sleep(5)
            ataque_x_comp=random.randint(0,len(tabuleiro_jog)-1)
            ataque_y_comp=random.randint(0,len(tabuleiro_jog[0])-1)

            print(f' a posição que o computador atacou foi:{ataque_x_comp},{ataque_y_comp}')
            if tabuleiro_jog[ataque_x_comp][ataque_y_comp] == '^':
                tabuleiro_jog[ataque_x_comp][ataque_y_comp] = 'X'
                pontos_computador+=1
                print('UM BARCO SEU FOI ACERTADO!!!')
                time.sleep(2)
                print('como ele acertou ele pode tentar novamente: ') # ele tambem possui a oportunidade de tentar novamente se acertar o barco 
                acertou= True
                while acertou:
                    ataque_x2_comp=random.randint(0,len(tabuleiro_jog)-1)
                    ataque_y2_comp=random.randint(0,len(tabuleiro_jog[0])-1)
                    if tabuleiro_jog[ataque_x2_comp][ataque_y2_comp] == '^':
                        pontos_computador+=1
                        print('UM BARCO SEU FOI ACERTADO novamente!!!')
                        tabuleiro_jog[ataque_x2_comp][ataque_y2_comp]='X'
                    else:
                        tabuleiro_jog[ataque_x_comp][ataque_y_comp] ='~'
                        acertou=False

            else:
                tabuleiro_jog[ataque_x_comp][ataque_y_comp] ='~'
            print('---------tabuleiro do jogador atual------------------ ')
            mostra_tabuleiro(tabuleiro_jog) 
            print('---------tabuleiro simulado atual------------------ ')
            mostra_tabuleiro(tabuleiro_simu)
            if teste==1:
                mostra_tabuleiro(tabuleiro_comp)
    if pontos_jogador == 16:
        print("PARABÉNS! Você venceu o computador!")
    else:
        print("O computador venceu! Tente novamente.")