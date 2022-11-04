n=int(input())
a=n//100
b=(n//10)%10
c=n%10
#abc,acb,bac,bca,cab,cba.
print(n, a*100+c*10+b, b*100+a*10+c, b*100+c*10+a, c*100+a*10+b, c*100+b*10+a, sep="\n")