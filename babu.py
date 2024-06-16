def find_val(mp, source, n):
    st = []
    dist = [float('-inf') for _ in range(n)]
    dist[0] = 0
    st.append([0, 0])
    while st:
        ref = st.pop()
        dest = ref[0]
        cost = ref[1]
        for k in mp.get(dest, []):  # Safely retrieve the value associated with source key
            new_cost = k[1] + cost
            if new_cost > dist[k[0]]:
                dist[k[0]] = new_cost
                st.append([k[0], new_cost])
    return dist

n = 4
m = 5
mp = {}
for _ in range(m):
    arr = list(map(int, input().split()))
    mp.setdefault(arr[0] - 1, []).append([arr[1] - 1, arr[2]])
print(mp)
find_val(mp, 0, n)
