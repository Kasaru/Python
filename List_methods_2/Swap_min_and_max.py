l = input().split(' ')
l = list(map(int,l))
imax = l.index(max(l))
imin = l.index(min(l))
l[imin],l[imax] = l[imax],l[imin]
print(*l)