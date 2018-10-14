import os

os.path.dirname(os.path.abspath(__file__))

bands = list()
path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(path)

for file in files:
    if file.endswith('.txt'):
        f = (path + '/' + file);

        with open (f) as org:
            for line in org:
                bands.append(line.strip())
                bands.sort()

        filename = path + '/' + 'Sorted_' + file

        with open(filename, 'w') as result:
            for band in bands:
                result.write(band + '\n')
