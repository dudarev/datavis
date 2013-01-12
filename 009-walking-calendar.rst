title: Walking calendar
date: 2012-07-05
---
.. |NBSP| unicode:: U+00A0
.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

`Matt Cutts`_ popularizes the idea of `30-days challenges`_.  I wanted to show results of such a challenge in a callendar view, with days when the challenge was met highlighted.

.. image:: 009_walking_calendar.png
   :alt: Days when walking challenge was met.
   :align: center
   :target: 009_walking_calendar.png

The challenge was to walk at least 5 kilometers per day. I tracked walking with `My Tracks`_
app on my Android phone. In fact, in a few days I could not track the walking because of low battery.

In the `source code`_ there are a few scripts that allow to get GPX tracks from the phone (I am using `FTP server app`_ there), calculate tracks length for one day (I've forked and modified 
`pygpx library`_ for this), and generate the image above.

.. _Matt Cutts: http://www.mattcutts.com/blog/
.. _30-days challenges: http://www.youtube.com/watch?v=VxhynMlg6S4
.. _My Tracks: http://mytracks.appspot.com/
.. _source code: https://github.com/dudarev/datavis/tree/master/009_walking_distance
.. _FTP server app: https://play.google.com/store/apps/details?id=lutey.FTPServer&amp;hl=en
.. _pygpx library: http://github.com/dudarev/pygpx
