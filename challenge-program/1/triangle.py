n = 5
a_list = [2, 3, 4, 5, 10]

def solve():
    sorted_list = sorted(a_list)
    list_len = len(sorted_list)
    ans = 0
    for i in range(list_len-1, 1, -1):
        triangle_len = sorted_list[i] + sorted_list[i-1] + sorted_list[i-2]
        if sorted_list[i-1] + sorted_list[i-2] > sorted_list[i]:
            ans = triangle_len
            break
    return ans

if __name__ == '__main__':
    print(solve())
