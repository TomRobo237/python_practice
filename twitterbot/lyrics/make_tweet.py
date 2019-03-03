import os
from random import choice, seed, randint
seed(os.urandom(10))
folder = os.path.dirname(__file__)

def build_tweet():
    files = [myfile for myfile in os.listdir(folder) if myfile.endswith('.txt')]

    with open(folder + '/' + choice(files),'r') as fp:
        song = ''.join(fp.readlines())
        artist, title = os.path.basename(fp.name).replace('_',' ').replace('.txt','').split('-')
    start = randint(0, len(song) - 120)
    lyrics = song[start:start + 120]

    return lyrics + '\n\nfrom: ' + artist + ' - ' + title
