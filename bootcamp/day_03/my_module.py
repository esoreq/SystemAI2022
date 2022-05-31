sum_sq = lambda data: sum(x ** 2 for x in data)
mean = lambda data: sum(data)/float(len(data))
sq_mean = lambda data: sum_sq(data)/float(len(data)-1)
var = lambda data: sum((x - mean(data))**2/float(len(data)-1) for x in data)
