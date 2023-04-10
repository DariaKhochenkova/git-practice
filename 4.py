a = [str(i) for i in input().split()]
b = [str(i) for i in input().split()]
def match(l1, l2):
    return {l1[i]: l2[i] for i in range(len(l1))}
print(match(a, b))