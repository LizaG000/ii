def fibRecurse(n_1, n_2, fib, n):
    if len(fib) < n:
        fib.append(str(n_1 + n_2))
        return fibRecurse(n_2, n_1 + n_2, fib, n)
    return ', '.join(fib)

def fibSequence(n):
    assert n > 0
    series = [1]
    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    for i in range(len(series)):
        series[i] = str(series[i])
    return(', '.join(series))
print(fibSequence(int(input('Сколько чисел? '))))
print(fibRecurse(1, 1, ["1", "1"], int(input('Сколько чисел? '))))