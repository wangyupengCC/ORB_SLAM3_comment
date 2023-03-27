import matplotlib.pyplot as plt
import sys

delta_angle = []
delta_t_x = []
delta_t_y = []
delta_t_z = []
velcoticy_x = []
velcoticy_y = []
velcoticy_z = []
ImuBias = []

logfile = open(sys.argv[1],'r')
for line in logfile:
    line = line.split()
    if 'angular_distance' in line:
        if 'end'!= line[3]:
            # print(line)
            delta_angle.append(float(line[3]))
    elif 'delta_t' in line:
        delta_t_x.append(float(line[2]))
        delta_t_y.append(float(line[3]))
        delta_t_z.append(float(line[4]))
    elif 'Vwb2' in line:
        velcoticy_x.append(float(line[2]))
        velcoticy_y.append(float(line[3]))
        velcoticy_z.append(float(line[4]))

fig, ax = plt.subplots()
ax.plot(delta_angle)
ax.set_title('angular_distance')

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)
ax[0].set_title('delta_t')
ax[0].plot(delta_t_x)
ax[1].plot(delta_t_y)
ax[2].plot(delta_t_z)

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)
ax[0].plot(velcoticy_x)
ax[0].set_title('velcoticy_x')
ax[1].plot(velcoticy_y)
ax[0].set_title('velcoticy_y')
ax[2].plot(velcoticy_z)
ax[0].set_title('velcoticy_z')

plt.show()
