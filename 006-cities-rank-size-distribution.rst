title: Cities Rank-Size Distribution
date: 2011-05-17
---
.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

If to scale an information service to ``1,000`` cities what kind of cities will be covered? Or a reverse questions: how many cities have population of more than ``1,000,000``?

The answers can be found from `geonames.org <http://www.geonames.org/>`__ `data <http://download.geonames.org/export/dump/>`__ just with `a couple of lines of Python code <https://github.com/dudarev/datavis/tree/master/006_cities_population_distribution>`__: 

    more than ``340`` cities have population more than ``1,000,000``; the city ranked 1,000th *in that data* has population of around ``400,000``.

This is curious to see how cities population is distributed. The plot below is for cumulative distribution of cities population.

.. image:: 006_distribution_hist.png
   :alt: cumulative distribution of cities in dependence on population
   :align: center

The linear dependence in a log-log plot is an indication of `power law <http://en.wikipedia.org/wiki/Power_law>`__ dependence. At some population the distribution changes the slope. Below ``1,000,000`` inhabitants the slope is almost ``-1`` which indicates ``1/x`` dependence. Then it changes, and changes again at 7 million, and 10 million inhabitants. I would attribute changes at 1 and 10 million to psychology of regional and national governments that treat cities above and below this numbers differently.

Typically, this dependence is plotted in the form of size (population) *vs.* rank. 

.. image:: 006_rank_size.png
   :alt: rank-size distribution of cities
   :align: center

`Rank-size distribution <http://en.wikipedia.org/wiki/Rank-size_distribution>`__ of cities population was noticed more than half a century ago and is a subject of multiple research studies.

`The code <https://github.com/dudarev/datavis/tree/master/006_cities_population_distribution>`__ to produce the plots is available at github. This is fascinating to play with it: to see if the distribution is universal from a country to country (it's not for large populations), to come up with a simple interpolation formula that approximates it and so on. But, to keep the note brief, these exercises are for a truly curious reader.
