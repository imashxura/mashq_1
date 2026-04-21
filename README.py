# mashq_1
class Futbolchi:
    def __init__(self, ism, jamoa, gol_soni, yosh):
        self.ism = ism
        self.jamoa = jamoa
        self.gol_soni = gol_soni
        self.yosh = yosh

    def score_goal(self, count):
        self.gol_soni += count
        return self.gol_soni

    def get_info(self):
        return f"{self.ism}, {self.jamoa}, {self.gol_soni}, {self.yosh}"


fut1 = Futbolchi("Ronaldo", "Al-Nassr", 10, 39)
print(fut1.score_goal(2))
print(fut1.get_info())
