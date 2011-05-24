title: Cluster OpenStreetMap POIs
date: 2011-05-24
---
.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

.. image:: 007_pois_cluster.png
   :alt: cluster of openstreetmap POIs in Donetsk
   :align: center

In the first iteration of `Locopoly <http://www.locopoly.com/>`__ `rules <https://github.com/dudarev/locopoly/wiki/en%3ARules>`__ a player will randomly jump from one location to another within ``1 km``. Will it be possible to jump to every location in a city?

This question can be reduced to a `hierarhical clustering <http://en.wikipedia.org/wiki/Hierarchical_clustering>`__ problem, one of the standard problems of `machine learning <http://en.wikipedia.org/wiki/Machine_learning>`__. In general, the clusters can be calculated based on some `linkage criteria <http://en.wikipedia.org/wiki/Hierarchical_clustering#Linkage_criteria>`__. For the formulated problem we need to use minimum or single-linkage clustering.

The clustering is done based on various distances, not necessary in Euclidian space. Here, we parse POIs from an OpenStreetMap file and `convert <https://github.com/dudarev/datavis/blob/master/007_pois_distribution/parse_pois.py#L96>`__ them to ``(x,y)`` grid neglecting curvature of the Earth.

Any clustering libraries may be used. We use `mlpy <https://mlpy.fbk.eu/>`__, `scipy-cluster <http://code.google.com/p/scipy-cluster/>`__ also seems to be interesting.

For jumping distance of ``1 km`` several clusters are formed in Donetsk at the moment. The city was formed from many settlement and modern POIs distribution is a good indication of history. Still, all this clusters will be connected in the future when more places are mapped.

.. image:: 007_clusters_numbers.png
   :alt: number of POIs in each cluster
   :align: center

The largest cluster has more than ``450`` spots |---| a good initial playground.

`The code is available at Github <https://github.com/dudarev/datavis/tree/master/007_pois_distribution>`__. It is good to reference:

* GIS

  - parsing OSM file with cElementTree

    + choosing only POIs with ``name`` key

  - converting lat,lon to x,y

* mlpy (machine learning)
  
  - hierarhical clustering

* Matplotlib

  - scatter plot

  - bar plot with colors

  - getting colors from cmap

* Python

  - truncation of text
