import csv

reader = csv.reader(open("cities15000.txt"), delimiter='\t')

# index of population and country in the file
population_index = 14
country_index = 8

pop = [int(row[population_index]) for row in reader]
pop.sort(reverse=True)

pop1 = 1e6
for i in range(len(pop)):
    if pop[i] < pop1:
        rank1 = i-1
        break

print rank1, pop[rank1] 

rank2 = 1000-1
print rank2, pop[rank2] 

import numpy as np
import pylab as P

ax = P.axes([0.15, 0.15, 0.75, 0.75])
P.loglog(range(len(pop)),pop)

def plot_point(rank1,style=None):
    if not style:
        style = 'r--'
    # plot lines to point (rank1,pop1)
    pop1 = pop[rank1]
    P.loglog([rank1,rank1],[0.1,pop1], style)
    P.loglog([1,rank1],[pop1,pop1], style)

plot_point(rank1)
plot_point(rank2, 'g--')

labels = ax.get_xticklabels()
P.setp(labels, fontsize=14)
labels = ax.get_yticklabels()
P.setp(labels, fontsize=14)
 
P.ylim(15000,20e6)
P.xlabel('Rank',fontsize=20);
P.ylabel('Population',fontsize=20);


# P.xticks([1e5, 2e5, 4e5, 8e5, 16e5, 32e5, 64e5, 128e5])
P.grid()

P.savefig('006_rank_size.png', dpi=54)

P.show()
