def bucketsort(a, l):
    bucket = []

    # Createempty buckets
    for i in range(10):
        bucket.append([])

    print(bucket)

    for j in a:
        index = int(10 * j)
        bucket[index].append[j]

    print(bucket)

    for k in range(l):
        bucket[k] = bucket[k].sort()


a = [.5, .2, .6, .8]
bucketsort(a, len(a))
