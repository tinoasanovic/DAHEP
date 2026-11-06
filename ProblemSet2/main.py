import uproot
import numpy as np
import matplotlib.pyplot as plt

# 1. Čitanje grana (Awkward Arrays, 4 leptona po događaju)
tree = uproot.open("ggH125_ZZ4lAnalysis.root")["ZZTree/candTree"]
pt  = tree["LepPt"].array()
eta = tree["LepEta"].array()
phi = tree["LepPhi"].array()

# 2. Transformacija koordinata (leptoni bez mase)
px = pt * np.cos(phi)
py = pt * np.sin(phi)
pz = pt * np.sinh(eta)
E  = np.sqrt(px**2 + py**2 + pz**2)   # m = 0

# 3. Invarijantna masa: m^2 = E^2 - px^2 - py^2 - pz^2
def inv_mass(sl):
    Es, pxs, pys, pzs = (np.sum(v[:, sl], axis=1) for v in (E, px, py, pz))
    m2 = Es**2 - pxs**2 - pys**2 - pzs**2
    return np.sqrt(np.maximum(m2, 0))

m_higgs = inv_mass(slice(0, 4))   # sva 4 leptona
m_z1    = inv_mass(slice(0, 2))   # prva dva leptona (Z1)

# 4. Crtanje na istom canvasu
bins = np.linspace(0, 200, 101)
plt.hist(m_higgs, bins=bins, color="red",  label="Higgs (4 leptona)")
plt.hist(m_z1,    bins=bins, color="blue", label="Z1 (2 leptona)")
plt.xlabel("Invariant mass [GeV]")
plt.ylabel("Events / 2 GeV")
plt.legend()
plt.savefig("masses.png")
plt.show()