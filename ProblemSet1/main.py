import math, random
from ClassDef import Boson, Higgs

photon = Boson('Photon', 1, 0)
photon.PrintInfo()

higgs_boson = Higgs('Higgs', 0, 10, 125)
higgs_boson.PrintInfo() 

print(f"Higgs Energy: {higgs_boson.Energy():.2f}", "GeV")
      

