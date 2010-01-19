def extract_slug(list_name):
    start = list_name.find('/')
    return list_name[start+1:]

def classify_user(user):

    file = open('data/%s_lists.txt' % user,'r')
    lists_set= set()
    for line in file:
        lists_set.add(extract_slug(line.strip()))

    return lists_set

def classify_cluster(cluster):

    labels = {}

    for u in cluster:
        for l in classify_user(u):
            labels[l] = labels.setdefault(l,0) + 1

    label_count_pairs = zip(labels.values(),labels.keys())
    label_count_pairs.sort(reverse=True)

    for c,l in label_count_pairs[:10]:
        print l,c

    return labels
