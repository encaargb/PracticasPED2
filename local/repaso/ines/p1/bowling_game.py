class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for frame in range(10):
            if i >= len(self.rolls):
                break

            if self.rolls[i] == 10:  # Strike
                if i + 2 < len(self.rolls):
                    total += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
            elif i + 1 < len(self.rolls):
                frame_score = self.rolls[i] + self.rolls[i + 1]
                if frame_score == 10:  # Spare
                    if i + 2 < len(self.rolls):
                        total += 10 + self.rolls[i + 2]
                    else:
                        total += 10  # parcial
                else:
                    total += frame_score
                i += 2
            else:
                total += self.rolls[i]  # caso raro: solo un tiro suelto
                i += 1

        return total
