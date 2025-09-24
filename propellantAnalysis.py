from rocketcea.cea_obj import CEA_Obj
import numpy as np, matplotlib.pyplot as plt

Pc_bar, eps = 120.0, 40.0
Pc_psia = Pc_bar * 14.5037738
OF = np.arange(3, 4, 0.02)

cea = CEA_Obj(oxName='LOX', fuelName='CH4')

IspSL = [cea.estimate_Ambient_Isp(Pc=Pc_psia, MR=mr, eps=eps, Pamb=14.7)[0] for mr in OF]
Tc    = [cea.get_Temperatures(Pc=Pc_psia, MR=mr, eps=eps)[0]               for mr in OF]

idx = int(np.nanargmax(IspSL))
OF_opt = float(OF[idx])
Isp_sl_opt = float(IspSL[idx])

print(f'Optimal O/F for max sea-level Isp: {OF_opt:.3f}')
print(f'Max Isp_SL: {Isp_sl_opt:.1f} s  (Pc={Pc_bar:.0f} bar, ε={eps:.0f})')


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(OF, IspSL, label='Isp (SL)')
ax2.plot(OF, Tc, color='orange', label='T_comb')

ax1.set_title(f'LOX/CH4  Pc={Pc_bar:.0f} bar, ε={eps:.0f}')
ax1.set_xlabel('O/F'); ax1.set_ylabel('Isp_SL [s]'); ax2.set_ylabel('T_comb [K]')
ax1.grid(True)
ax1.legend(loc='best')
plt.tight_layout(); plt.show()
