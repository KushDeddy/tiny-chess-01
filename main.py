import os,json,urllib.request as ur
E=os.environ;U=E['MAKEFUN_ENV_URL']
def post(p,d={}):
 r=ur.Request(U+p,data=json.dumps(d).encode(),headers={'Content-Type':'application/json'})
 return json.loads(ur.urlopen(r,timeout=12).read())
N=70000;nodes=0;TT={};H=0
BB=[0]*128
PST=[
[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,20,20,0,0,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,5,0,0,0,0,0,0,0,0,0],
[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,5,15,20,20,15,5,-30,-30,0,10,10,10,10,0,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50],
[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,10,10,10,5,5,-10,-10,5,10,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20],
[0,0,0,5,5,5,5,0,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0],
[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20],
[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,10,20,0,0,20,10,20,10,20,0,0,20,10,20,10,10,0,0,0,0,10,20,-5,-10,0,0,0,-10,-5,-10,-20,-10,-10,-5,-5,-10,-10,-20,-30,-20,-15,-10,-10,-15,-20,-30]
]
VAL=[0,100,320,330,500,900,20000]
def gB():global BB;BB=[0]*128
def n(s):v=BB[s];return abs(v)if abs(v)else 0
def c(s):return BB[s]>0
def m():
 r=[];i=0
 while i<64:
  if not BB[i]:r+=[(i,i+1),(i,i-1),(i+8,i-8)];i+=1;continue
  nv=n(i)
  if nv==1:
   for d in[(-8,-1),(-8,1),(8,-1),(8,1)]:
    j=i+d[0];k=i+d[1]
    if 0<=j<64 and k>=0 and k<8 and abs((k-i%8))<=1:
     if not BB[k]:r+=[(i,k)];continue
     if nv!=c(i):r+=[(i,k)]
   continue
  if nv==2:
   for d in[(-16,0),(16,0),(0,-16),(0,16),(-15,1),(-15,-1),(15,1),(15,-1),(-17,1),(-17,-1),(17,1),(17,-1)]:
    j=i+d[0];k=i+d[1]
    if 0<=j<64 and k>=0 and k<8 and abs((k-i%8))<=2:
     if not BB[k]or nv!=c(i):r+=[(i,k)]
   continue
  if nv==3:
   for d in[(8,8),(8,-8),(-8,8),(-8,-8)]:
    j=i+d[0];k=i+d[1]
    while 0<=j<64 and k>=0 and k<8 and abs((k-i%8))==abs(j)//8:
     if BB[k]:
      if nv!=c(i):r+=[(i,k)]
      break
     r+=[(i,k)];j+=d[0];k+=d[1]
   continue
  if nv==4:
   for d in[(8,0),(-8,0),(0,8),(0,-8)]:
    j=i+d[0];k=i+d[1]
    while 0<=j<64 and k>=0 and k<8 and ((d[0]!=0 and (k-i%8)==0) or (d[1]!=0 and abs(j)//8==1)):
     if BB[k]:
      if nv!=c(i):r+=[(i,k)]
      break
     r+=[(i,k)];j+=d[0];k+=d[1]
   continue
  if nv==5:
   for d in[(8,8),(8,-8),(-8,8),(-8,-8),(8,0),(-8,0),(0,8),(0,-8)]:
    j=i+d[0];k=i+d[1]
    while 0<=j<64 and k>=0 and k<8:
     cd=abs(d[0])==8 and abs((k-i%8))==abs(j)//8 or abs(d[1])==8 and ((d[0]!=0 and (k-i%8)==0) or (d[1]!=0 and abs(j)//8==1))
     if not cd:break
     if BB[k]:
      if nv!=c(i):r+=[(i,k)]
      break
     r+=[(i,k)];j+=d[0];k+=d[1]
   continue
  i+=1
 return r
def E2():
 v=0
 for s in range(64):
  if not BB[s]:continue
  nv=n(s);v+=nv*PST[BB[s]][s]
 return v
def pv(d,a,b,nodes):
 if nodes[0]>N:return E2()
 if d==0:return qs(a,b,nodes)
 ms=m();km=[]
 for f,t in ms:
  ct=BB[t];mv=BB[f];BB[f]=0;BB[t]=mv
  sc=-pv(d-1,-b,-a,nodes)
  BB[t]=ct;BB[f]=mv
  if sc>a:a=sc;km.append((f,t))
  nodes[0]+=1
  if a>=b:break
 if not km:return 0
 return a
def qs(a,b,nodes):
 sv=E2();if sv>=b:return sv;if sv>a:a=sv
 ms=m(c=True);nm=[]
 for f,t in ms:
  nm+=[(f,t)];ct=BB[t];mv=BB[f];BB[f]=0;BB[t]=mv
  sc=-qs(-b,-a,nodes)
  BB[t]=ct;BB[f]=mv
  if sc>a:a=sc
  nodes[0]+=1
  if a>=b:break
 return a
def to_uci(f,t):
 S='abcdefgh';return S[f%8]+str(8-f//8)+S[t%8]+str(8-t//8)
def main():
 gB();nodes=[0]
 while True:
  r=post('/')
  if r['status']=='done':break
  if r['status']=='over':continue
  ms=m()
  best=None;ba=-999999
  for f,t in ms:
   ct=BB[t];mv=BB[f];BB[f]=0;BB[t]=mv
   sc=pv(3,-999999,999999,nodes)
   nodes[0]=0
   BB[t]=ct;BB[f]=mv
   if sc>ba:ba=sc;best=(f,t)
  if best:
   f,t=best;post('/move',{'game':r['game'],'move':to_uci(f,t)})
  else:post('/resign',{'game':r['game']})
if __name__=='__main__':main()
