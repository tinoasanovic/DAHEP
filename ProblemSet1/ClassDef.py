import math, random

class Boson:
    isFermion = False

    def __init__(self, name, spin, momentum):
        self.name = name
        self.spin = spin
        self.momentum = momentum

    def PrintInfo(self):
        print(f"Boson Name: {self.name}, Spin: {self.spin}, Momentum: {self.momentum}," 
              f" Is Fermion: {self.isFermion}")

class Higgs(Boson):
    MassSigma = 1

    def __init__(self, name, spin, momentum, MassMean):
        super().__init__('Higgs', 0, momentum)
        self.MassMean = MassMean

    def Energy(self):
        mass = random.gauss(self.MassMean, self.MassSigma)
        return math.sqrt(self.momentum**2 + mass**2)
    
        

    
