import numpy as np

Workspace_lower = []
Workspace_upper = []
Filter_Kernel = []

M = 800
FC = 0.196

for i in range(800):
    if i - M/2 == 0:
        Workspace_lower[i] = 2 * np.pi * FC
    else:
        Workspace_lower[i] = np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2)
    Workspace_lower[i] = Workspace_lower[i] * (0.42 - 0.5 * np.cos(2 * np.pi * i / M) + 0.08 * np.cos(4 * np.pi * i/M))

SUM = 0
for i in range(800):
    SUM = SUM + Workspace_lower[i]

for i in range(800):
    Workspace_lower[i] = Workspace_lower[i] / SUM

FC = 0.204
for i in range(800):
    if i - M/2 == 0:
        Workspace_upper[i] = 2 * np.pi * FC
    else:
        Workspace_upper[i] = np.sin(2 * np.pi * FC * (i - M/2)) / (i - M/2)
    Workspace_upper[i] = Workspace_upper[i] * (0.42 - 0.5 * np.cos(2 * np.pi * i/M) + 0.08 * np.cos(4 * np.pi * i / M))

SUM = 0
for i in range(800):
    SUM = SUM + Workspace_upper[i]

for i in range(800):
    Workspace_upper[i] = Workspace_upper[i] / SUM

for i in range(800):
    Workspace_upper[i] = not Workspace_upper[i]

Workspace_upper[400] = Workspace_upper[400] + 1

for i in range(800):
    Filter_Kernel[i] = Workspace_lower[i] + Workspace_upper[i]

for i in range(800):
    Filter_Kernel[i] = not Filter_Kernel

Filter_Kernel[400] = Filter_Kernel[400] + 1

