#!/usr/bin/python

from __future__ import with_statement
import os
import re
import codecs
from docutils.core import publish_parts
from docutils.writers import html4css1
from django.template import Context, Template
from django.conf import settings
settings.configure()


class Page(dict):
    ""
    _re_config_end = r'^---+ *\n?$'

    @staticmethod
    def parse_config(line):
        i = line.find(':')
        if i:
            return line[:i].strip(),line[i+1:].strip()
        else:
            return None,None

    def __init__(self, template, file_name):
        super(Page, self).__init__()

        self['time_modified'] = os.path.getmtime(file_name)

        with codecs.open(file_name, 'r','utf8') as f:
            self.raw = f.readlines()

        self.file_name = file_name
        self.source = ""
        self.config = ""

        for line in self.raw:
            if not self.config and re.match(self._re_config_end, line):
                self.config = self.source
                self.source = "" # reset source
            else:
                self.source += line
    
        for line in self.config.split('\n'):
            key,value = Page.parse_config(line)
            print key,value
            if key:
                self[key] = value
    
    def __getattribute__(self, key):
        try:
            return super(Page, self).__getattribute__(key)
        except AttributeError, e:
            if key in self:
                return self[key]
            raise e


RST_PATTERN = r'\.(?:rst|rest)$'

def cmp_time(a,b):
   return cmp(a['date'],b['date'])

def build_pages():
    re_replace_with_stdout = re.compile(r'(?<!\\)(?:(?:<!--|{)%)((?:.*?\r?\n?)*)(?:%(?:-->|}))')

    pages = []
    for dir, dirs, files in os.walk('.'):
        for f in files:
            if re.search(RST_PATTERN, f):
                page = Page("page.html", os.path.join(dir, f))
                pages.append(page)

    pages.sort(cmp_time,reverse=True)

    for p in pages:
        try:
            print p["title"]
            print p["time_modified"]
        except:
            print 'no title'

        input = p.source
        output = publish_parts(
                source=input, 
                writer_name='html4css1',
        )['fragment']
        if p.has_key('abstract'):
            p['abstract'] = publish_parts(source=p['abstract'], writer_name='html4css1',)['fragment']

        t = Template(open("page.tpl",'r').read())
        c = Context({"page": p, "content": output})

        # create HTML pages
        file_name = re.sub(RST_PATTERN, ".html", p.file_name)
        p['url'] = file_name
        p['content'] = output
        with codecs.open(file_name, 'w', 'utf8') as f:
            f.write( t.render(c) )
    
    return pages

def build_index(pages):

    t = Template(open("index.tpl",'r').read())
    c = Context({"pages": pages})

    # create HTML pages
    file_name = "index.html"
    with codecs.open(file_name, 'w', 'utf8') as f:
        f.write( t.render(c) )

def main():
    pages = build_pages()
    build_index(pages)
            
if __name__ == '__main__':
    main()
