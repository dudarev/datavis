title: When Followers Tweet
date: 2009-12-16
---
.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

.. image:: http://4.bp.blogspot.com/_rZy4zSAOlB8/SyjEdL79EEI/AAAAAAAABTA/GVT_efUXYqk/s320/003_izba4i.png
   :alt: <http://4.bp.blogspot.com/_rZy4zSAOlB8/SyjEdL79EEI/AAAAAAAABTA/GVT_efUXYqk/s1600-h/003_izba4i.png>`_ 
   :align: center

One of the goals of `TweetingPlaces <http://www.tweetingplaces.com/>`_ is to help small local businesses to connect to their customers. One of the ways for them to increase exposure on Twitter may be to schedule tweets of non-immediate importance to times when the message may be seen by most of the followers. The plot above shows activity of followers on Twitter. It may help to get some insights on when to schedule tweets. Still, the best metric can be provided by direct measurements of the reactions on tweets posted at different times.

The plot is for a coffee shop "`Изба-читальня <http://www.izba4i.com/>`_" in Donetsk, Ukraine (during winter in UTC +2 timezone). Its tweets can be found at `@izba4i <http://twitter.com/izba4i>`_ . Most of its followers are Donetsk locals and tweet from 9 a.m. till 11 p.m. of local time with peak around 1 p.m. (lunch time).

The focus of `TweetingPlaces <http://www.tweetingplaces.com/>`_ is global, and scheduling tweets at particular times may be not a good strategy, but out of curiosity here is a plot for `@tweetingplaces <http://twitter.com/tweetingplaces>`_ followers:

.. image:: http://3.bp.blogspot.com/_rZy4zSAOlB8/SyjHlbzPZsI/AAAAAAAABTI/LQcLlFiajIk/s320/003_tweetingplaces.png
   :alt: <http://3.bp.blogspot.com/_rZy4zSAOlB8/SyjHlbzPZsI/AAAAAAAABTI/LQcLlFiajIk/s1600-h/003_tweetingplaces.png>`_
   :align: center

The minimum is much less pronounced and the followers start tweeting more than average after 8 a.m. Eastern Time.

`The code <http://github.com/dudarev/datavis/tree/master/003_twitter_time_of_day/>`_ for these plots is available at github. In addition to `Matplotlib <http://matplotlib.sourceforge.net/>`_ that has been used in all the previous examples, `tweepy <http://code.google.com/p/tweepy/>`_ library is used to interact with Twitter API (note that you may have to limit number of requests per hour if many of them have to be made). Also, `PyYAML <http://pyyaml.org/wiki/PyYAML>`_ does not come in standard library.
