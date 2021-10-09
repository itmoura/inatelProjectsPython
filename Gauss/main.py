def MetodoGauss(m):
    # eliminação de colunas
    for col in range(len(m[0])):
        for row in range(col + 1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
        print("---------------")
        print(m)
    # Resolver por substituição
    ans = []
    m.reverse()
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1] / m[sol][-2])
        else:
            inner = 0
            # Substituir em todos os coeficientes conhecidos
            for x in range(sol):
                inner += (ans[x] * m[sol][-2 - x])
            # A equação está agora reduzida a ax + b = c
            # Resolve-se com (c - b) / a
            ans.append((m[sol][-1] - inner) / m[sol][-sol - 2])
    ans.reverse()
    return ans


print(MetodoGauss([[4.0, -2.0, -1.0, 0.0, 10.0],
                   [-1.0, 0.0, 6.0, -3.0, 0.0],
                   [-2.0, 9.0, 0.0, -5.0, -5.0],
                   [0.0, 5.0, -3.0, 10.0, 0.0]]))
