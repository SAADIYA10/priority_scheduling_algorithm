def findWaitingTime(bt, n):
    wt = [0] * n
    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i-1]
    return wt

def findavgTime():
    data = [[1,8], [2,4], [3,9], [4,5]]
    data.sort(key=lambda x: x[1])

    p = [x[0] for x in data]
    bt = [x[1] for x in data]
    n = len(p)

    wt = findWaitingTime(bt, n)
    tat = [bt[i] + wt[i] for i in range(n)]

    print("Process BT WT TAT")
    for i in range(n):
        print(p[i], bt[i], wt[i], tat[i])

    print("Average Waiting Time =", sum(wt)/n)
    print("Average Turn Around Time =", sum(tat)/n)

findavgTime()
