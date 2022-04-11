# Quero representar tempo/horario

class Tempo:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.segundos_totais = horas * 3600 + minutos * 60 + segundos

    def __repr__(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

    def __add__(self, outro):
        soma_dos_segundos_totais = self.segundos_totais + outro.segundos_totais

        horas = soma_dos_segundos_totais // 3600 
        minutos = soma_dos_segundos_totais // 60 % 60
        segundos = soma_dos_segundos_totais % 60

        return Tempo(horas, minutos, segundos)

    @staticmethod
    def criar_tempo_por_string(string_de_tempo):
        separados = string_de_tempo.split(':')
        horas = int(separados[0])
        minutos = int(separados[1])
        segundos = int(separados[2])
        return Tempo(horas, minutos, segundos)


string_de_horario = "20:40:15"
novo_horario = Tempo.criar_tempo_por_string(string_de_horario)
print(novo_horario)





