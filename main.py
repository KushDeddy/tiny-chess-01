import os,json,urllib.request as U
E=os.environ;U_=E['MAKEFUN_ENV_URL'];T={};N=60000;H=0
B=[0]*128
PST=[[0]*64 for _ in range(12)]
V=[0,100,320,330,500,900,0]
def gB():global B;B=[0]*128
def n(s):v=B[s];return abs(v)if v else 0
def c(s):return B[s]>0
def gm():
 r=[]
 for s in range(64):
  if not B[s]:continue
  nv=n(s);o=s>>3;c=s&7
  if nv==1:
   for d in[(1,0),(2,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
    t=s+d[0]*8+d[1]
    if 0<=t<64 and 0<=abs(t&7-c)<=1 and 0<=(t>>3)-o<=2:
     if not B[t]:r+=[(s,t)];continue
     if nv!=c(s):r+=[(s,t)]
   continue
  if nv==2:
   for d in[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(2,0),(2,-2),(-2,2),(-2,-2)]:
    t=s+d[0]*8+d[1]
    if 0<=t<64 and 0<=abs(t&7-c)<=2 and 0<=(t>>3)-o<=2:
     if not B[t]or nv!=c(s):r+=[(s,t)]
   continue
  if nv==3:
   for d in[(1,1),(1,-1),(-1,1),(-1,-1)]:
    t=s+d[0]*8+d[1]
    while 0<=t<64 and abs(t&7-c)==abs(t>>3-o):
     if B[t]:
      if nv!=c(s):r+=[(s,t)]
      break
     r+=[(s,t)];t+=d[0]*8+d[1]
   continue
  if nv==4:
   for d in[(1,0),(-1,0),(0,1),(0,-1)]:
    t=s+d[0]*8+d[1]
    while 0<=t<64 and((d[0]and t&7==c)or(d[1]and t>>3==o)):
     if B[t]:
      if nv!=c(s):r+=[(s,t)]
      break
     r+=[(s,t)];t+=d[0]*8+d[1]
   continue
  if nv==5:
   for d in[(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]:
    t=s+d[0]*8+d[1]
    while 0<=t<64 and(abs(d[0])and t&7==c or abs(d[1])and t>>3==o):
     if B[t]:
      if nv!=c(s):r+=[(s,t)]
      break
     r+=[(s,t)];t+=d[0]*8+d[1]
   continue
 return r
def ev():
 v=0
 for s in range(64):
  if not B[s]:continue
  v+=V[abs(B[s])]+PST[abs(B[s])][s]
 return v
def pv(d,a,b,nodes):
 if nodes[0]>N:return ev()
 if d==0:return qs(a,b,nodes)
 km=[]
 for f,t in gm():
  ct=B[t];mv=B[f];B[f]=0;B[t]=mv
  sc=-pv(d-1,-b,-a,nodes)
  B[t]=ct;B[f]=mv
  if sc>a:a=sc;km.append((f,t))
  nodes[0]+=1
  if a>=b:break
 if not km:return 0
 return a
def qs(a,b,nodes):
 sv=ev()
 if sv>=b:return sv
 if sv>a:a=sv
 for f,t in gm():
  ct=B[t];mv=B[f];B[f]=0;B[t]=mv
  sc=-qs(-b,-a,nodes)
  B[t]=ct;B[f]=mv
  if sc>a:a=sc
  nodes[0]+=1
  if a>=b:break
 return a
def to_uci(f,t):
 S='abcdefgh';return S[f&7]+str(8-f>>3)+S[t&7]+str(8-t>>3)
def main():
 gB();nodes=[0]
 while True:
  r=P('/')
  if r['status']=='done':break
  if r['status']=='over':continue
  ms=gm()
  best=None;ba=-999999
  for f,t in ms:
   ct=B[t];mv=B[f];B[f]=0;B[t]=mv
   sc=pv(4,-999999,999999,nodes);nodes[0]=0
   B[t]=ct;B[f]=mv
   if sc>ba:ba=sc;best=(f,t)
  if best:
   f,t=best;P('/move',{'game':r['game'],'move':to_uci(f,t)})
  else:P('/resign',{'game':r['game']})
if __name__=='__main__':main()
