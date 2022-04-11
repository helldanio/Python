#exercício 06 - By Helldânio Barros
import time

class Cronometro:

    def __init__(self, tempo):
        self.tempo = tempo
        
    def inicia(self):
        if self.tempo < 1: self.tempo = 1
        if self.tempo > 59: self.tempo = 59
        self.imprime()

    def imprime(self):

        n = []
        i = []
        for x in range(10):
            for w in range(7):
                i.append('')
            n.append(i)
            i = []

        n[0][0] = ''
        n[0][1] = '▓▓▓▓▓▓▓▓'
        n[0][2] = '▓▓    ▓▓'
        n[0][3] = '▓▓    ▓▓'
        n[0][4] = '▓▓    ▓▓'
        n[0][5] = '▓▓    ▓▓'
        n[0][6] = '▓▓▓▓▓▓▓▓'

        n[1][0] = ''
        n[1][1] = '  ▓▓▓▓  '
        n[1][2] = '▓▓  ▓▓  '
        n[1][3] = '    ▓▓  '
        n[1][4] = '    ▓▓  '
        n[1][5] = '    ▓▓  '
        n[1][6] = ' ▓▓▓▓▓▓▓'

        n[2][0] = ''
        n[2][1] = '▓▓▓▓▓▓▓▓'
        n[2][2] = '      ▓▓'
        n[2][3] = '      ▓▓'
        n[2][4] = '▓▓▓▓▓▓▓▓'
        n[2][5] = '▓▓      '
        n[2][6] = '▓▓▓▓▓▓▓▓'

        n[3][0] = ''
        n[3][1] = '▓▓▓▓▓▓▓▓'
        n[3][2] = '      ▓▓'
        n[3][3] = '      ▓▓'
        n[3][4] = '▓▓▓▓▓▓▓▓'
        n[3][5] = '      ▓▓'
        n[3][6] = '▓▓▓▓▓▓▓▓'

        n[4][0] = ''
        n[4][1] = '▓▓    ▓▓'
        n[4][2] = '▓▓    ▓▓'
        n[4][3] = '▓▓▓▓▓▓▓▓'
        n[4][4] = '      ▓▓'
        n[4][5] = '      ▓▓'
        n[4][6] = '      ▓▓'

        n[5][0] = ''
        n[5][1] = '▓▓▓▓▓▓▓▓'
        n[5][2] = '▓▓      '
        n[5][3] = '▓▓      '
        n[5][4] = '▓▓▓▓▓▓▓▓'
        n[5][5] = '      ▓▓'
        n[5][6] = '▓▓▓▓▓▓▓▓'

        n[6][0] = ''
        n[6][1] = '   ▓▓▓▓▓'
        n[6][2] = ' ▓▓     '
        n[6][3] = '▓▓      '
        n[6][4] = '▓▓▓▓▓▓▓▓'
        n[6][5] = '▓▓    ▓▓'
        n[6][6] = '▓▓▓▓▓▓▓▓'

        n[7][0] = ''
        n[7][1] = '▓▓▓▓▓▓▓▓'
        n[7][2] = '      ▓▓'
        n[7][3] = '     ▓▓ '
        n[7][4] = '    ▓▓  '
        n[7][5] = '   ▓▓   '
        n[7][6] = '   ▓▓   '

        n[8][0] = ''
        n[8][1] = '▓▓▓▓▓▓▓▓'
        n[8][2] = '▓▓    ▓▓'
        n[8][3] = '▓▓    ▓▓'
        n[8][4] = '▓▓▓▓▓▓▓▓'
        n[8][5] = '▓▓    ▓▓'
        n[8][6] = '▓▓▓▓▓▓▓▓'

        n[9][0] = ''
        n[9][1] = '▓▓▓▓▓▓▓▓'
        n[9][2] = '▓▓    ▓▓'
        n[9][3] = '▓▓    ▓▓'
        n[9][4] = '▓▓▓▓▓▓▓▓'
        n[9][5] = '      ▓▓'
        n[9][6] = '▓▓▓▓▓▓▓▓'

        for x in range(self.tempo+1):
            sTempo = str(x)
            print( '\n' * 130)
            n1 = int(sTempo[0])            
            if len(sTempo) > 1: n2 = int(sTempo[1])
            print(n[n1][1],n[n2][1] if len(sTempo) > 1 else '')
            print(n[n1][2],n[n2][2] if len(sTempo) > 1 else '')
            print(n[n1][3],n[n2][3] if len(sTempo) > 1 else '')
            print(n[n1][4],n[n2][4] if len(sTempo) > 1 else '')
            print(n[n1][5],n[n2][5] if len(sTempo) > 1 else '')
            print(n[n1][6],n[n2][6] if len(sTempo) > 1 else '')
            time.sleep(1)
     
#cronômentro de segundos, informar um número de 1 a 59
relogio = Cronometro(25)
relogio.inicia()
