class BowlingGame:
    '''def score(self, rolls): #rolls es una lista porque puede variar el número de tiros al haber bonus
        # Sumamos todos los tiros, sin considerar strikes ni spares (aún)
        return sum(rolls)
    def score(self, rolls):
        total = 0
        i = 0  # índice dentro de la lista de tiros

        for frame in range(10):  # siempre hay 10 rondas
            if rolls[i] + rolls[i + 1] == 10:  # SPARE
                total += 10 + rolls[i + 2]     # 10 más el bonus (siguiente tiro)
                i += 2     # avanzamos 2 posiciones i es el índice que usamos para recorrer la lista rolls( los tiros del jugador) y cada ronda (o frame) tiene 2 tiros

            else:  # RONDA NORMAL (open frame)
                total += rolls[i] + rolls[i + 1]
                i += 2

        return total'''
    
    def score(self, rolls):
        total = 0
        i = 0  # índice dentro de la lista de tiros

        for frame in range(10):
            if rolls[i] == 10:  # STRIKE
                total += 10 + rolls[i + 1] + rolls[i + 2]
                i += 1  # avanzamos 1 porque el strike ocupa 1 tiro
            elif rolls[i] + rolls[i + 1] == 10:  # SPARE
                total += 10 + rolls[i + 2]
                i += 2
            else:  # RONDA NORMAL
                total += rolls[i] + rolls[i + 1]
                i += 2

        return total
