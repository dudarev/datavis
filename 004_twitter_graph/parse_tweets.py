"""finds list of topics, mentionings graph, or tweeting times

by default find topics (hashes)
use options

    -h - for help
    -g - to find mentionings graph
    -t - to find times
"""

import sys
import getopt

argv = sys.argv
try:
    # options that require arguments are followed by :
    opts, args = getopt.getopt(argv[1:], "gth",['--help'])
except getopt.error, msg:
     raise Usage(msg)

is_finding_hashes,is_finding_graph,is_finding_times = True,False,False

# process options
for o, a in opts:
    if o in ("-h", "--help"):
        print __doc__
        sys.exit(0)
    if o == '-g':
        is_finding_hashes,is_finding_graph,is_finding_times = False,True,False
    if o == '-t':
        is_finding_hashes,is_finding_graph,is_finding_times = False,False,True

import os
import simplejson as json
from get_config import get_config
import tweepy
from tweepy.parsers import parse_status
from find_hash import find_hash

# we do not query twitter here, only use api for parsing, so no authorization is required
api = tweepy.API()

first = True
count = 0

if is_finding_graph:
    friends_count = {}
if is_finding_hashes:
    hash2people = {}

file = open('data/members.txt','r')
members = {}
for user in file:
    user_name = user.strip().lower()
    members[user_name] = {}

for user_name in members:
    print user_name
    if not os.path.exists('data/%s.txt' % user_name):
        continue
    f = open('data/%s.txt' % user_name)
    data = json.load(f)

    if is_finding_graph:
        friends = []

    if is_finding_times:
        hour_counts = {}

    for d in data:
        s = parse_status(d,api)

        if is_finding_hashes:
            hashes = find_hash(s.text)
            for h in hashes:
                if not hash2people.has_key(h):
                    hash2people[h] = []
                if not user_name in hash2people[h]:
                    hash2people[h].append(user_name)

        if is_finding_graph:
            people = find_hash(s.text,find_mentionings=True)
            for p in people:
                # only outside of the group
                # if not p in members
                if p in members:
                # weighted
                # friends.append(p)
                # friends_count[p] = friends_count.get(p,0)+1
                # members[user_name][p] = members[user_name].get(p,0)+1
                # non-weighted
                    if not p in members[user_name]:
                        members[user_name][p] = 1
                        friends.append(p)
                        friends_count[p] = friends_count.get(p,0)+1

        if is_finding_times:
            h = s.created_at.hour
            hour_counts[h] = hour_counts.get(h,0) + 1

    if is_finding_times:
        print hour_counts
        file_counts = open('data/%s_hour_counts.txt' % user_name,'w')
        file_counts.write(user_name)
        hours = range(24)
        for h in hours:
            file_counts.write(',%d' % hour_counts.get(h,0))
        file_counts.close()

    count += 1

def print_pairs(pairs,n=20):
    """print first n pairs (number,value) in the format
    value number"""
    i = 0
    for p in pairs:
        i+=1
        print p[1],p[0]
        if i >= n:
            break

def save_pairs(pairs,file_name):
    """saves pairs in the format
    value number"""
    f = open(file_name,'w')
    count = 1
    for p in pairs:
        f.write( '%d. %s (%s)\n' % (count, p[1].encode('utf8'),p[0]) )
        count += 1

if is_finding_hashes:
    print len(hash2people)
    hash_freq_pairs = zip(map(len,hash2people.values()),hash2people.keys())
    hash_freq_pairs.sort(reverse=True)
    print_pairs(hash_freq_pairs)
    save_pairs(hash_freq_pairs,'data/hash_counts.txt')

if is_finding_graph:
    friends_freq_pairs = zip(friends_count.values(),friends_count.keys())
    friends_freq_pairs.sort(reverse=True)

    print_pairs(friends_freq_pairs)
    save_pairs(friends_freq_pairs,'data/friends_counts.txt')

    f = open('data/friends_graph.txt','w')
    f.write(json.dumps(members))
    f.close()
