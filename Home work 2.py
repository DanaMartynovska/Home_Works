high = int(input('Веедити высоту'))

for i in range(high):
    print(' ' * (high - i) + ('^' * i) + ('^' * (i+1)))
