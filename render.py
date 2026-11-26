from PIL import Image, ImageDraw, ImageFont
import math

W=H=1024
NAVY=(8,18,35); INK=(13,29,50); OCEAN=(16,43,66); LAND=(216,222,198)
GOLD=(241,181,65); ORANGE=(244,99,39); WHITE=(245,242,230); MUTED=(166,185,194)
RED=(205,72,53); TEAL=(72,178,170); PANEL=(232,231,211); DARK=(20,31,42)
img=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(img)
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=False): return ImageFont.truetype(bold if b else font,n)
def txt(x,y,s,size,color=WHITE,b=False,anchor=None): d.text((x,y),s,font=F(size,b),fill=color,anchor=anchor)
def wrap(x,y,s,width,size,color=WHITE,b=False,leading=3):
    words=s.split(); line=''; yy=y
    for w in words:
        t=(line+' '+w).strip()
        if d.textlength(t,font=F(size,b))>width and line:
            txt(x,yy,line,size,color,b); yy+=size+leading; line=w
        else: line=t
    if line: txt(x,yy,line,size,color,b); yy+=size+leading
    return yy

# masthead
d.rectangle((0,0,W,180),fill=INK); d.rectangle((0,174,W,180),fill=GOLD)
txt(34,24,'THURSDAY 26 NOVEMBER 2026',20,GOLD,True)
txt(34,52,'BLACKOUT ATLAS',48,WHITE,True)
txt(36,111,'Giza tanker fire kills 31  |  Nasdaq plunges 4 percent  |  first Pakistani in orbit',17,WHITE,True)
txt(36,139,'31 STORIES  ·  9 REGIONS  ·  REPORTING WINDOW: 00:00–23:59 UTC',13,MUTED,True)
# fire flare
d.ellipse((830,18,1010,180),fill=(117,48,28)); d.ellipse((855,38,982,170),fill=ORANGE); d.ellipse((886,58,956,151),fill=GOLD)
for i in range(7):
    a=i*0.55; x=915+int(math.cos(a)*78); y=90-int(math.sin(a)*65)
    d.line((915,110,x,y),fill=GOLD,width=3)

# lead panel
d.rounded_rectangle((28,198,996,366),radius=8,fill=(25,47,65),outline=(70,101,112),width=2)
txt(48,214,'LEAD  /  EGYPT',14,GOLD,True)
txt(48,240,'GIZA TANKER FIRE',38,WHITE,True)
txt(48,286,'31 KILLED  ·  21 INJURED',25,ORANGE,True)
wrap(48,320,'Al-Warraq, above Cairo’s Ring Road: petroleum tanker overturned; 27 vehicles charred. Toll remains preliminary.',515,13,WHITE,False)
d.rectangle((690,214,970,345),fill=(16,30,43)); txt(710,230,'PRELIMINARY TOLL',13,GOLD,True)
txt(710,255,'31',56,ORANGE,True); txt(793,276,'dead',18,WHITE,True)
txt(710,315,'21 injured · Wed 25 Nov',14,MUTED); txt(710,331,'Reuters / AP / CNN',12,MUTED)

# co-leads
d.rounded_rectangle((28,382,996,514),radius=8,fill=(224,225,207))
txt(48,394,'CO-LEADS',13,(157,89,27),True)
cols=[('−4%','AI ROUTE HITS NASDAQ','−4.15% intraday; Nvidia −8.7%. Section 301 tariffs proposed for 14–16 partners.'),('SHENZHOU-24','PAKISTANI IN ORBIT','Muhammad Zeeshan Ali, 40: first Pakistani and first foreign national on Tiangong.'),('NETANYAHU','JUDGES SEEK CASE RESET','Jerusalem judges recommend dropping Case 4000; recommendation, not a ruling.')]
for i,(big,head,body) in enumerate(cols):
    x=48+i*315
    if i: d.line((x-18,425,x-18,496),fill=(166,170,154),width=2)
    txt(x,422,big,25,(26,74,91) if i!=0 else RED,True)
    txt(x,454,head,14,DARK,True); wrap(x,477,body,285,11,(46,57,62),False)

# atlas
d.rounded_rectangle((28,530,996,732),radius=8,fill=OCEAN,outline=(67,112,124),width=2)
txt(48,540,'ATLAS PLATE  ·  14 VERIFIED DOTS  ·  LAT/LON CHECKED AGAINST SLATE',12,GOLD,True)
mx,my,mw,mh=46,562,930,154
# graticule
for lon in range(-180,181,30):
    x=mx+(lon+180)/360*mw; d.line((x,my,x,my+mh),fill=(63,101,113),width=1)
for lat in range(-60,91,30):
    y=my+(90-lat)/150*mh; d.line((mx,y,mx+mw,y),fill=(63,101,113),width=1)
# hand-drawn continent polygons in equirect projection
polys=[ [(-168,72),(-140,70),(-125,55),(-105,50),(-95,25),(-78,8),(-83,-5),(-105,8),(-120,25),(-145,45)],
 [(-82,12),(-70,8),(-60,-5),(-52,-20),(-60,-55),(-72,-45),(-78,-15)],
 [(-10,72),(40,70),(80,60),(120,52),(145,45),(160,30),(140,8),(120,0),(100,10),(80,25),(55,20),(40,5),(25,-10),(10,-35),(-5,-30),(-18,-5),(-5,20)],
 [(112,-10),(153,-12),(153,-38),(125,-42),(112,-28)] ]
def proj(lon,lat): return (mx+(lon+180)/360*mw, my+(90-lat)/150*mh)
for p in polys: d.polygon([proj(*q) for q in p],fill=LAND,outline=(27,45,54))
d.line((proj(-180,0),proj(180,0)),fill=(116,151,151),width=1)
points=[('GIZA',31.21,30.06),('NYC',-74.01,40.71),('JIUQUAN',100.3,41),('JERUSALEM',35.21,31.77),('CIKANDE',106.1,-6.1),('BENGHAZI',20.07,32.12),('HORMUZ',56.3,26.5),('PYONGYANG',125.75,39.02),('MINNA',6.55,9.61),('DHAKA',90.41,23.81),('MUMBAI',72.88,19.08),('BOGOTA',-74.07,4.71),('CARACAS',-66.88,10.48),('RIO',-43.17,-22.91)]
for i,(lab,lon,lat) in enumerate(points,1):
    x,y=proj(lon,lat); d.ellipse((x-4,y-4,x+4,y+4),fill=GOLD,outline=WHITE,width=1); txt(x+6,y-10,str(i),10,GOLD,True)
labels=[('GIZA',31.21,30.06),('NYC',-74.01,40.71),('JQ',100.3,41),('JLM',35.21,31.77),('Cikande',106.1,-6.1),('Benghazi',20.07,32.12),('Hormuz',56.3,26.5),('Pyongyang',125.75,39.02),('Minna',6.55,9.61),('Dhaka',90.41,23.81),('Mumbai',72.88,19.08),('Bogotá',-74.07,4.71),('Caracas',-66.88,10.48),('Rio',-43.17,-22.91)]
for lab,lon,lat in labels:
    x,y=proj(lon,lat); txt(x+8,y+4,lab,9,WHITE,True)

# numbers strip
d.rectangle((28,744,996,790),fill=(190,63,40)); txt(48,755,'A DAY IN NUMBERS',15,WHITE,True)
nums=[('31','Giza killed'),('−4%','Nasdaq intraday'),('174','Mumbai remembered'),('100th','Macy’s parade')]
for i,(n,l) in enumerate(nums):
    x=260+i*180; txt(x,752,n,22,WHITE,True); txt(x,777,l,10,WHITE)

# cards
cards=[('CIKANDE','26 dead in candy factory','Tue update · Indonesia',GOLD),('RUSSIA OIL','20+ year refining low','18+ refineries hit',RED),('HORMUZ','Mine claims in strait','Iran says ships struck',TEAL),('N. KOREA','Swiss diplomat expelled','Sanctions row',GOLD),('NIGERIA','30+ killed in Niger State','Attacks reported',RED),('BANGLADESH','100+ bank branches burned','Grameen Bank unrest',TEAL),('BTC','~$60,300','Fragile rebound',GOLD),('COLOMBIA','10 years after peace deal','Unfinished commitments',TEAL),('VENEZUELA','$237.5bn debt revealed','Economic reset',RED),('PETROBRAS','$122bn investment plan','Brazil energy',GOLD),('BEPICOLOMBO','Mercury reached','8-year journey',TEAL),('DART','Stadium-sized crater','Asteroid defence test',RED)]
for j,(head,body,sub,col) in enumerate(cards):
    row=j//4; coln=j%4; x=28+coln*242; y=804+row*68
    d.rounded_rectangle((x,y,x+226,y+58),radius=5,fill=PANEL)
    d.rectangle((x,y,x+7,y+58),fill=col)
    # distinct mini-mark
    if j%3==0: d.ellipse((x+15,y+17,x+34,y+36),outline=col,width=3); d.line((x+24,y+7,x+24,y+17),fill=col,width=2)
    elif j%3==1: d.polygon([(x+14,y+37),(x+25,y+12),(x+36,y+37)],outline=col,fill=None); d.line((x+14,y+42,x+40,y+42),fill=col,width=2)
    else: d.line((x+14,y+38,x+23,y+18,x+34,y+31,x+43,y+10),fill=col,width=3); d.ellipse((x+20,y+15,x+26,y+21),fill=col)
    txt(x+50,y+8,head,11,DARK,True); txt(x+50,y+26,body,10,DARK,True); txt(x+50,y+43,sub,8,(73,82,79))
txt(28,1000,'31 stories · 9 regions · Wed follow-ups labelled · Thursday scheduled items checked at build time',10,MUTED)
img.save('/home/hatch/workspace/makefun/news-image-20261126-01/entry.png',optimize=True)
