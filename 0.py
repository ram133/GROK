import hashlib,json,datetime
class B:
 def __init__(s,i,t,d,p,n=0):s.i,s.t,s.d,s.p,s.n=i,t,d,p,n;s.h=s.c()
 def c(s):return hashlib.sha256(json.dumps({"i":s.i,"t":s.t,"d":s.d,"p":s.p,"n":s.n},sort_keys=1).encode()).hexdigest()
class C:
 def __init__(s,d=2):s.d=d;s.c=[s.m(0,"Genesis","0"*64)]
 def m(s,i,d,p):
  n=0
  while 1:
   b=B(i,datetime.datetime.now(datetime.timezone.utc).isoformat(),d,p,n)
   if b.h.startswith("0"*s.d):s.c.append(b);return b
   n+=1
 def a(s,d):return s.m(s.c[-1].i+1,d,s.c[-1].h)
 def v(s):
  for i,b in enumerate(s.c):
   if b.i!=i or b.h!=b.c() or not b.h.startswith("0"*s.d)or(i and b.p!=s.c[i-1].h):return 0
  return 1
if __name__=="__main__":
 b=C(2);b.a("Laptop");b.a("Passport")
 for x in b.c:print(f"[{x.i}] {x.d} n={x.n} {x.h[:12]}…")
 print("valid:",b.v())