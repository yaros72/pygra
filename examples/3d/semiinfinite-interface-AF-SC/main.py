
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian(has_spin=True)
h1 = h.copy()
h2 = h.copy()
h1.add_antiferromagnetism(0.5)
h1.add_swave(0.0)
#h1.add_haldane(0.1)
h2.add_swave(0.5)
h2.shift_fermi(1.0)
#h2.add_haldane(-0.1)

import kdos
kdos.interface(h1,h2)
