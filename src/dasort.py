# DA-sort
# https://open.kattis.com/problems/dasort
# TAGS: sorting
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
Some frustrating design choices with this exercise:

a) weird input format
b) the "point" is to discover the insight that e.g. in  1 4 5 2 7 3 6 the elements that you must delete are the ones that are
   in the incorrect relative order i.e. wrt to [1,2,3,4,5,6,7]
   you would look from l->r for 1 at first: ok it occurs at first spot, so now look for 2:
   -> you encounter 4 (BAD), 5 (BAD), then 2 (FOUND IT) -> so you will need to delete 4,5
   -> now look for 3: 7 (BAD), 3 (FOUND IT) -> delete 7
   -> now look for 4: 6 (BAD), end of array -> need to delete 6
So you see that you need to delete: 4,5,7,6 AND THAT BY DOING SO IN THE "INTELLIGENT ORDER" [which is always possible, i.e you are free to choose]
you can append them in the order 4,5,6,7 to get the sorted list

But the reason the exercise is weird to me is that it complicates it needlessly by making the variables *not* 1->N, but some
random collection (WITH DUPLICATES!) which doesn't add anything at all, just makes it seem more difficult for no reason and
involves sorting the array rather than just maintaining a "next_val_needed" that would start at 1, then ++ each time you find
next correct element in order.
"""
P = int(input())
for _ in range(P):
    K, N = map(int, input().split())
    xs = []
    for _ in range(1 + (N - 1) // 10): # weird input format: 10 elements per line -.- so there are 1 + (N-1)//10 lines to input
        xs.extend(map(int, input().split()))

    # count elements that are out of place wrt REF sorted list O_o
    REF = sorted(xs)
    cnt = 0
    i_ref = 0
    for x in xs:
        if x == REF[i_ref]:
            i_ref += 1
        else:
            cnt += 1

    print(K, cnt)