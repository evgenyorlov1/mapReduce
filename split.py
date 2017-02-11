import os
from itertools import chain, islice


directory = 'chunks'


def chunks(iterable, n):
   "chunks(ABCDE,2) => AB CD E"
   iterable = iter(iterable)
   while True:
       # store one line in memory,
       # chain it to an iterator on the rest of the chunk
       yield chain([next(iterable)], islice(iterable, n-1))


def split(file_large, l):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_large) as bigfile:
        for i, lines in enumerate(chunks(bigfile, l)):
            file_split = '{}.{}'.format(file_large, i)
            with open(os.path.join(directory,file_split), 'w') as f:
                f.writelines(lines)



