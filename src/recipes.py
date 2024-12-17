# Scaling Recipes
# https://open.kattis.com/problems/recipes
# TAGS: basic
# CP4: 1.6f, Real Life, Medium
# NOTES:
T = int(input())

for testcase in range(1, T + 1):
    R, P, D = map(int, input().split())

    xs = []
    for _ in range(R):
        name, w, pc = input().split()
        if pc == "100.0":
            REF = float(w) * D / P
        xs.append((name, float(pc)))

    print("Recipe #", testcase)
    for name, pc in xs:
        print(name, f"{pc * 0.01 * REF:.1f}")
    print("-" * 40) # output requirements O_o