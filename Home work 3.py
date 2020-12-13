high = int(input('Веедити высоту'))

i=0

for i in range(high):
    print(' ' * (high - i) + ('^' * i) + ('^' * (i+1)))
