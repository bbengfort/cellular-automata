import matplotlib
matplotlib.use('TKAgg')

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N    = 100
ON   = 255
OFF  = 0
vals = (ON, OFF)

def init(n=N, randrow=False):
    grid = np.zeros(shape=(n,n))
    if randrow:
        grid[0] = np.random.choice(vals, n, p=(0.2, 0.8))
    else:
        grid[0,n/2] = ON
    return grid

def update(d):
    global row
    data = grid[row]
    row += 1
    if row >= N: return
    grid[row] = np.array([rule[int(4*data[((j-1))%N]/ON+2*data[j]/ON+data[((j+1))%N]/ON)]
               for j in range(N)])
    mat.set_data(grid)
    return mat


rulenum=90
fig, ax = plt.subplots()
ax.axis('off')
row = 0
grid = init()
rule = [((rulenum/pow(2,i)) % 2) * ON for i in range(8)]
mat = ax.matshow(grid, cmap=cm.Greens)
ani = animation.FuncAnimation(fig, update, frames=99, interval=60, save_count=50, repeat=False)
ani.save('rule90.mp4', writer='ffmpeg', fps=30, dpi=300)
#plt.show()
