"""Solve Burger's Equation and
simulate its evolution with time"""
import numpy as np
from scitools.std import *
import time
import glob, os

N = 850 #Simulate for long enough time
M = 400
dx = 2 * np.pi / M
cfl = 0.55
a = 1.3
dt = cfl * dx / np.sqrt(a)

#Initial conditions
def initialize():
    return 0.5 + np.sin(x)

x = np.linspace(0.0, 2 * np.pi, M + 1)
u = initialize()

def evolve_in_One_Timestep(u):
    #Create an array to store the new values of the solution
    u_new = np.zeros((M + 1,), float)
    for k in range(1, M):  # M-1
        u_new[k] = u[k] - 0.25 * (u[k + 1] ** 2 - u[k - 1] ** 2) * (dt / dx) \
        + 0.5 * np.sqrt(a) * (u[k + 1] - 2 * u[k] + u[k - 1]) * (dt / dx)
    #Apply boundary conditions
    u_new[0] = u_new[1]
    u_new[M] = u_new[M - 1]
    return u_new

iteration = 0
evolve = initialize()
for n in range(0, N):
    plot(np.linspace(0.0, 1.0, M + 1), evolve, 'm', linewidth=1.0, show=False,
         xlabel='x', ylabel='u(x,t)', title="Evolution of wave Equation", \
         markersize=8, legend='step=%4.0f' % n,
         hardcopy="wave%04d.png" % iteration)
    evolve = evolve_in_One_Timestep(evolve)
    iteration += 1

#Make movie
movie("wave*.png")

#Explicitly specify .gif movie using controls, fps means # of frames per second
movie('wave*.png', encoder='convert', fps=12,
      output_file='Burgers.gif')

#Generate an avi movie
movie('wave*.png', encoder='ffmpeg', fps=12,
      output_file='Burgers.avi')

savefig("shock_wave.png")

#Clean all created images
for filename in glob.glob('/home/elimboto/pde_simulations/wave*.png'):
    os.remove(os.path.join("/home/elimboto/pde_simulations", filename))
