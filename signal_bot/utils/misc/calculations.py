from statistics import mean


def avg(scope, long_short):
    scope_l = list(map(float, [i.replace(',', '.') for i in scope.split('-')]))
    final_result, chunk = [], 10
    x = 1 if scope_l[0] > 1 else 5
    if len(scope_l) > 1:
        kek = max(scope_l)
        if long_short == 'Long':
            for i in range(chunk):
                different = abs(scope_l[0] - scope_l[1]) / chunk
                kek -= different
                final_result.append(round(kek, x))
                final_result.sort()
        else:
            for i in range(chunk):
                different = abs(scope_l[0] - scope_l[1]) / chunk
                kek -= different
                final_result.append(round(kek, x))
    else:
        if long_short == 'Long':
            for i in range(chunk):
                scope_l[0] += scope_l[0] * 0.01
                final_result.append(round(scope_l[0], x))
        else:
            for i in range(chunk):
                scope_l[0] -= scope_l[0] * 0.01
                final_result.append(round(scope_l[0], x))
    return ', '.join([str(element) for element in final_result]), round(mean(final_result), x)




