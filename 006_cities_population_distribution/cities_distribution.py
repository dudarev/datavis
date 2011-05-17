import csv

reader = csv.reader(open("cities15000.txt"), delimiter='\t')

# index of population and country in the file
population_index = 14
country_index = 8

pop = [int(row[population_index]) for row in reader]

# uncomment these lines to see distribution for a country
# country = 'UA'
# pop = [int(row[population_index]) for row in reader if row[country_index]==country]

import numpy as np
import pylab as P

n, bins, patches = P.hist(pop, 100, normed=1, histtype='stepfilled', cumulative=-1, log=True)
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

P.figure(2)
ax = P.axes([0.15, 0.15, 0.75, 0.75])
P.loglog(bins[:-1],n)

def plot_fit(pop1, pop2):
    pop_fraction_selected = [ [pop,fraction] for pop,fraction in zip(bins,n) if pop > pop1 and pop < pop2]
    pop_selected = [ p for p,f in pop_fraction_selected ]
    fraction_selected = [ f for p,f in pop_fraction_selected ]

    pop_selected = pop_selected[1:]
    fraction_selected = fraction_selected[1:]

    x = P.log10(pop_selected)
    y = P.log10(fraction_selected)

    a,b = np.polyfit(x,y,1)
    print a,b

    x = pop_selected
    y = [10**b*xx**a for xx in x]

    P.loglog(x,y)

pop_ranges_to_fit = [
        [1e3, 1e6],
        [1e6, 7e6],
        [7e6, 1e7],
        [1e7, 1e8],
        ]

for pops in pop_ranges_to_fit:
    pop1, pop2 = pops
    plot_fit(pop1,pop2)

labels = ax.get_xticklabels()
P.setp(labels, fontsize=14)
labels = ax.get_yticklabels()
P.setp(labels, fontsize=14)
 
P.xlabel('Population',fontsize=20);
P.ylabel('Fraction',fontsize=20);


P.ylim(0.00001,0.1)
# P.xticks([1e5, 2e5, 4e5, 8e5, 16e5, 32e5, 64e5, 128e5])
P.grid()

P.savefig('006_distribution_hist.png', dpi=54)

P.show()
