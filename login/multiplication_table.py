def run_multi():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i}*{j}={i * j:2d}', end='   ')
        print()