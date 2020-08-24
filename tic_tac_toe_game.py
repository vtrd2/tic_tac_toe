class Posição():
    '''Uma classe de cada posição'''
    def __init__(self):
        '''Inicia o atributo de valor que pode ser X O ou nada'''
        self.valor = None
    
    def define_valor(self, novo_valor):
        '''Define o valor de uma posição'''
        if self.valor:
            raise 'posição já ocupada'
        else:
            self.valor = novo_valor
    
    def retorna_valor(self):
        '''Retorn o valor da posição'''
        if self.valor:
            return self.valor.upper()
        else:
            return ' '
            
            
class Posiçoes():
    '''Junta todas as posiçoes'''
    def __init__(self):
        '''inicia as posições'''
        self.posiçoes = {}

    def novas_posiçoes(self):
        self.posiçoes = {
        1: Posição(),
        2: Posição(),
        3: Posição(),
        4: Posição(),
        5: Posição(),
        6: Posição(),
        7: Posição(),
        8: Posição(),
        9: Posição(),
        }

    def posição_ocupada(self, class_posição):
        '''Verifica a disponibilidade de uma posição'''
        if class_posição.valor: 
            return True
        else:
            return False

    def recebe_jogada(self, jogador):
        '''pergunta a posição em que o jogador quer jogar,  retorna a classe da posição'''
        while True:
            try:
                posição_escolhida = int(input(f'\n{jogador.upper()} digite a posição que você quer jogar: '))
                posição_escolhida = self.posiçoes[posição_escolhida]
                break
            except KeyError:
                print('\n---Digite apenas números de 1 à 9---')
        return posição_escolhida

    def define_jogada(self,class_posição, jogador):
        '''Coloca x ou o na posição'''
        class_posição.define_valor(jogador.lower())    
        

class Jogadores():
    '''Classe que define  jogador'''
    def __init__(self, jogador='x'):
        self.jogador = jogador
    
    def pede_jogador(self):
        '''Pede o jogador que ira começar'''
        while True:
            jogador_escolhido = input('\nDigite o Jogador que ira começar (X, O): ').lower()
            if jogador_escolhido != 'x' and jogador_escolhido != 'o':
                print('\n---Digite apenas X ou O---')
            else:
                break
        self.jogador = jogador_escolhido
    
    def alterna_jogador(self):
        '''Alterna o jogador entre x e o'''
        if self.jogador == 'x':
            self.jogador = 'o'
        elif self.jogador == 'o':
            self.jogador = 'x'


class Vencedor():
    '''Serve para verificar vencedor'''
    def __init__(self):
        '''Inicia a tupla que contém as linhas que permitem a vitoria'''
        self.linhas = (
            (1,2,3),
            (4,5,6),
            (7,8,9),
            (7,4,1),
            (8,5,2),
            (9,6,3),
            (7,5,3),
            (9,5,1),
            )

    def verifica_vencedor(self, jogador, dict_posiçoes):
        '''Verifica o vencedor com base nos valores das posiçoes'''
        for linha in self.linhas:
            if dict_posiçoes[linha[0]].valor == jogador and dict_posiçoes[linha[1]].valor == jogador and dict_posiçoes[linha[2]].valor == jogador:
                Vencedor.exibe_vencedor(jogador, dict_posiçoes)
                return True
        else:
            return False

    @staticmethod
    def exibe_vencedor(jogador, dict_posiçoes):
        print(f'\n---O jogador {jogador.upper()} venceu---')
        Jogo.exibe_tabuleiro(dict_posiçoes)      


class Jogo():
    '''Classe que junta todas as classes'''
    def __init__(self):
        '''Inicia as posiçoes jogadores e verificação de vencedor'''
        self.posiçoes = Posiçoes()
        self.vencedor = Vencedor()
        self.jogadores = Jogadores()
    
    @staticmethod
    def exibe_tabuleiro(dict_posiçoes):
        '''Exibe o tabuleiro com os x e o'''
        print(f'''
         {dict_posiçoes[7].retorna_valor()} | {dict_posiçoes[8].retorna_valor()} | {dict_posiçoes[9].retorna_valor()}
        ---+---+---
         {dict_posiçoes[4].retorna_valor()} | {dict_posiçoes[5].retorna_valor()} | {dict_posiçoes[6].retorna_valor()}
        ---+---+---
         {dict_posiçoes[1].retorna_valor()} | {dict_posiçoes[2].retorna_valor()} | {dict_posiçoes[3].retorna_valor()}
        ''')

    def faz_jogada(self, jogador_atual):
        '''recebe uma posição e a verifica e retorna essa posição'''
        while True:
            posição = self.posiçoes.recebe_jogada(jogador_atual)
            if self.posiçoes.posição_ocupada(posição):
                print('\n---Posição ocupada, digite uma outra posição---')
            else:
                break
        return posição
    
    def execute(self):
        '''Executa oprograma'''
        self.jogadores.pede_jogador()
        self.posiçoes.novas_posiçoes()
        for _ in range(9):
            Jogo.exibe_tabuleiro(self.posiçoes.posiçoes)
            jogador_atual = self.jogadores.jogador
            posição = self.faz_jogada(jogador_atual)
            posição.define_valor(jogador_atual)
            if self.vencedor.verifica_vencedor(jogador_atual, self.posiçoes.posiçoes):
                break
            self.jogadores.alterna_jogador()
        else:
            print('\n\t---VELHA---')
    
    def execute_many_times(self):
        while True:
            self.execute()

            while True:
                jogar_mais = input('\nVocê deseja jogar mais uma vez (S/N): ').lower()
                if jogar_mais != 's' and jogar_mais != 'n':
                    print('\n---Digite apenas S e N---\n')
                else:
                    break
            if jogar_mais == 'n':
                break


if __name__ == '__main__':
     jogo_da_velha = Jogo()
     jogo_da_velha.execute_many_times()