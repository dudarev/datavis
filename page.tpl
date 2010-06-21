<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
    <head> 
        <meta http-equiv="Content-Type" content="text/html; charset=utf8" />
        <title>{{ page.title }}</title> 
        <link type="image/x-icon" href="/favicon.ico" rel= "shortcut icon" /> 
        <link rel="stylesheet" href="screen.css" type="text/css" media="screen, projection">
        <link rel="stylesheet" href="print.css" type="text/css" media="print">
        <!--[if lt IE 8]><link rel="stylesheet" href="ie.css" type="text/css" media="screen, projection"><![endif]-->
        <meta name="description" content="{{ description }}" />
        <meta name="keywords" content="{{ keywords }}" />
        <link rel="stylesheet" type="text/css" href="writings.css" />
    </head> 
 
    <body id="index" class="home"> 

        <div id="navigation">
            <div class="navigation-container">
            <a href="/datavis">Simple Data Visualization</a>: <span class="title">{{page.title}}</span>
            </div>
        </div>

        <div class="container">

            <h1> {{page.title}}</h1>

            <div id="abstract">
            {{page.abstract|safe}}
            </div>
            
            <div class="span-16" id="content">
            {{content|safe}}
            </div>

        </div>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-17075003-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

    </body> 
</html> 
