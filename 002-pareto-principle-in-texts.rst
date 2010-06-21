title: Pareto Principle in Texts
date: 2009-09-11
---
.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

.. image:: http://1.bp.blogspot.com/_rZy4zSAOlB8/SrSlYqKUqHI/AAAAAAAABNM/kv8_jLFJH-U/s320/fraction.png
   :alt: <http://1.bp.blogspot.com/_rZy4zSAOlB8/SrSlYqKUqHI/AAAAAAAABNM/kv8_jLFJH-U/s1600-h/fraction.png>`_ 
   :align: center
   
A couple years ago I did a small project that would allow a language learner to estimate a fraction of text she would understand by answering which words she knows and which does not. The idea was to split all the words in the text into groups, so that each group is met a given fraction of times in the text. To be specific, at the time the groups were chosen so that each group corresponds to ``10%`` of all text. Further details of the testing algorithm may be found in a `small essay in Russian <http://dudarev.com/english_test/>`_ .

It was surprising to see how well `Pareto principle <http://en.wikipedia.org/wiki/Pareto_principle>`_ works with words. As it is stated in the Wikipedia article, the essence of Pareto's observation is that: 

    for many events, roughly ``80%`` of the effects come from ``20%`` of the causes.
    
As the graph above shows, this rule works remarkably well for words in a text too. That particular example shows a fraction of text contributed by a fraction of unique words for Lewis Carroll's " `Alice's Adventures in Wonderland <http://www.gutenberg.org/etext/11>`_ ".

`The code <http://github.com/dudarev/datavis/tree/c38d3c5232d97eea4bf9836b3f8cb9672663d77a/002_pareto_in_words>`_ for this post consists of two scripts. The first `sorts words <http://github.com/dudarev/datavis/blob/c38d3c5232d97eea4bf9836b3f8cb9672663d77a/002_pareto_in_words/word_count_list.py>`_ in the text by frequency, while the second does `plotting <http://github.com/dudarev/datavis/blob/c38d3c5232d97eea4bf9836b3f8cb9672663d77a/002_pareto_in_words/chart.py>`_ and also finds a number ``x`` such that ``x%`` of words are responsible for ``(100 - x)%`` of the text. For Carroll's book this number is ``17%``.
