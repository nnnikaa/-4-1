##s = 'aaabca'
##for sym in s:
##    count = 0
##    for sub_sym in s:
##        if sub_sym in s:
##            if sub_sym == sym:
##                count+=1
##    print(sym, count)

#Итераций:4
#O(N) =N**2


##print(set('aaabbdufu'))


##s = 'abc'
##for sym in set(s):
##    count = 0
##    for sub_sym in s:
##        if sub_sym in s:
##            if sub_sym == sym:
##                count+=1
##    print(sym, count)
#Итераций:6
#O(N) = M * N


##s = 'aab'
##syms_counter = {}
##for sym in s:
##    syms_counter[sym] = syms_counter.get(sym, 0) +1
##
##print(syms_counter)
#Итераций:3
#O(N) = N
