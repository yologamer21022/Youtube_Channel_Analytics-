import matplotlib.pyplot as plt
import json

data = []

views = []
subs = []
time = []
counting_data = 0
with open("data.json", "r+") as outfile:
    data = json.load(outfile)

for i in data:
    subs.append(int(i['subs']))
    views.append(int(i['views']))
    time.append(i['time'])





## LINE GRAPH ##

fig, axs = plt.subplots(2)

plt.gcf().autofmt_xdate()

fig.suptitle('Youtube Statistics')

axs[0].grid(True)
axs[1].grid(True)

plt.xlabel('Subscribers')

axs[0].plot(time, subs)
axs[1].plot(time, views)


plt.show()
