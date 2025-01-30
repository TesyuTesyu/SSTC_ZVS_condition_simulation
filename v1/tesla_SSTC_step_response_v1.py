import numpy as np
from control import matlab
from matplotlib import pyplot as plt

Lp=3.72e-6
Ls=164.5e-6
Rlp=0.5
fr=6.78e6
k=0.1
Cs=1/(2*np.pi*fr)**2/(1-k**2)/Ls
Rs=100e3

n=k*np.sqrt(Ls/Lp)
R1=n**2*Rlp
L1=k**2*Ls
L2=(1-k**2)*Ls
C1=Cs
R2=Rs
C11=100e-12
C12=C11/n**2

iL1_0=13.0e-3
iL2_0=596e-6
v3_0=11.7
v1_0=0.67

Omega=2*np.pi*fr
Cs=1/(Omega**2*Ls*(1-k**2))

# 2次系伝達関数モデル作成の関数
def tf_2nd_order():
   num=[C1*C12*L1*L2*R2*v1_0, (-C1*iL1_0*L1*L2*R2-C1*iL2_0*L1*L2*R2+C12*L1*L2*v1_0+C1*C12*L1*R1*R2*v1_0+C1*C12*L2*R1*R2*v1_0), (-iL1_0*L1*L2-iL2_0*L1*L2+C12*L1*R1*v1_0+C12*L2*R1*v1_0+C12*L1*R2*v1_0+C1*L1*R2*v3_0), -iL1_0*L1*R2+C12*R1*R2*v1_0]
   den=[C1*C12*L1*L2*R2, (C12*L1*L2+C1*C12*(L1+L2)*R1*R2), (C12*L1*R1+C12*L2*R1+C12*L1*R2+C1*(L1+L2)*R2), (L1+L2+C12*R1*R2), R2]
   G = matlab.tf(num, den)
   return G

# 伝達関数モデル作成
G2nd = tf_2nd_order()

# 伝達関数モデル出力
#print(G2nd)

# ステップ応答
t = np.linspace(0, 5e-6, 1000)
output, t = matlab.impulse(G2nd, T=t)

fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False, tight_layout=True, figsize=[8,6], sharex = "col")
ax[0,0].set_title('Lp=3.72e-6, Ls=164.5e-6, Rlp=0.5, fr=6.78e6, k=0.1')
ax[0,0].plot(t,output,"k-")
ax[0,0].set_xlabel('time [s]')
plt.show()