from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 247, 242)
INK = (22, 24, 25)
RED = (177, 38, 39)
RED_DARK = (123, 30, 32)
GREY = (91, 94, 93)
RULE = (191, 188, 179)
PALE = (235, 232, 224)
SEA = (216, 229, 228)
LAND = (177, 192, 173)
GOLD = (197, 143, 43)
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(size, bold=False): return ImageFont.truetype(BOLD if bold else FONT, size)
def text(x, y, value, size, color=INK, bold=False, anchor=None): d.text((x, y), value, font=f(size, bold), fill=color, anchor=anchor)
def wrap(x, y, value, width, size, color=INK, bold=False, leading=2, max_lines=None):
    words=value.split(); lines=[]; line=""
    for word in words:
        trial=(line+" "+word).strip()
        if line and d.textlength(trial,font=f(size,bold))>width: lines.append(line); line=word
        else: line=trial
    if line: lines.append(line)
    if max_lines: lines=lines[:max_lines]
    for i,ln in enumerate(lines): text(x,y+i*(size+leading),ln,size,color,bold)
def rule(y,x1=28,x2=996,color=RULE,width=1): d.line((x1,y,x2,y),fill=color,width=width)

text(28,18,"THE WORLD / THURSDAY EDITION",14,RED,True)
text(28,39,"THURSDAY 26 NOVEMBER 2026",36,INK,True)
text(28,83,"Macy's 100th parade postponed  |  Mumbai remembers 26/11  |  Game 3 in Geneva",14,GREY)
text(996,25,"36",48,RED,True,"ra"); text(996,75,"STORIES",12,GREY,True,"ra"); rule(108,width=4,color=INK)

d.rectangle((28,123,996,247),fill=INK)
text(46,136,"LEAD / THU 26 NOV",12,(240,188,92),True)
wrap(46,160,"MACY'S 100TH THANKSGIVING PARADE POSTPONED",675,23,PAPER,True,leading=1,max_lines=2)
wrap(46,198,"First postponement in the parade's 100-year history: a powerful nor'easter brings 60–65 mph gusts, heavy rain and coastal flooding. It moves to Saturday 28 Nov, 8:30 am ET.",650,12,PAPER,leading=2,max_lines=3)
text(750,138,"NEW YORK",11,(240,188,92),True); text(750,161,"40.71N  74.01W",13,PAPER,True)
text(750,192,"STATE OF",10,(198,201,198),True); text(750,207,"EMERGENCY",19,RED,True)
text(46,232,"Balloons inflated Nov 25, then deflated. NBC re-airs the 2025 parade Thursday.",10,(205,207,203))

text(28,270,"THURSDAY CO-LEADS",12,RED,True); rule(289)
lead_panels=[(28,"MUMBAI / 26 NOV","18 YEARS SINCE 26/11","174 died in the 2008 attacks. India also marks Constitution Day: 77 years since adoption in 1949.","19.08N  72.88E"),(351,"GENEVA / GAME 3","GUKESH v SINDAROV","World Championship Game 3, 15:00 CET. Match tied 1–1 after two draws; Sindarov has White.","46.20N  6.14E"),(674,"BRUSSELS / 26–27 NOV","EU LEADERS MEET","Euro Summit and Special European Council discuss the long-term budget and Ukraine financing for 2027.","50.85N  4.35E")]
for x,kicker,headline,body,coords in lead_panels:
    d.rectangle((x,300,x+294,406),fill=PALE,outline=RULE,width=1); text(x+14,311,kicker,10,RED,True)
    wrap(x+14,331,headline,266,16,INK,True,leading=1,max_lines=2); wrap(x+14,366,body,266,10,GREY,leading=1,max_lines=3); text(x+14,393,coords,8,RED_DARK,True)

d.rectangle((28,430,996,621),fill=SEA,outline=INK,width=2); text(46,440,"CENTRE ATLAS / STORY DOTS",11,RED,True); text(978,440,"TRUE LAT/LON",9,GREY,True,"ra")
mx,my,mw,mh=46,463,930,140
for lon in range(-180,181,30):
    x=mx+(lon+180)/360*mw; d.line((x,my,x,my+mh),fill=(183,202,201),width=1)
for lat in range(-60,91,30):
    y=my+(90-lat)/150*mh; d.line((mx,y,mx+mw,y),fill=(183,202,201),width=1)
def proj(lon,lat): return mx+(lon+180)/360*mw,my+(90-lat)/150*mh
continents=[[(-168,72),(-140,70),(-125,55),(-105,50),(-70,40),(-68,18),(-79,-5),(-105,8),(-145,45)],[(-82,12),(-58,12),(-45,-5),(-40,-35),(-52,-55),(-72,-45),(-78,-15)],[(-10,72),(40,70),(80,60),(145,45),(160,30),(140,8),(100,10),(55,20),(25,-10),(10,-35),(-5,-30),(-18,-5)],[(112,-10),(153,-12),(153,-38),(125,-42),(112,-28)]]
for polygon in continents: d.polygon([proj(*point) for point in polygon],fill=LAND,outline=(115,139,126))
points=[("NYC",-74.01,40.71),("GIZA",31.21,30.06),("MUM",72.88,19.08),("GEN",6.14,46.20),("BRU",4.35,50.85),("JQ",100.30,41.00),("JLM",35.21,31.77),("CIK",106.10,-6.10),("BENG",20.07,32.12),("HRM",56.30,26.50),("PYG",125.75,39.02),("MIN",6.55,9.61),("DHK",90.41,23.81),("BOG",-74.07,4.71),("CCS",-66.88,10.48),("RIO",-43.17,-22.91)]
for i,(label,lon,lat) in enumerate(points,1):
    x,y=proj(lon,lat); d.ellipse((x-4,y-4,x+4,y+4),fill=RED,outline=PAPER,width=1); text(x+6,y-10,str(i),8,RED_DARK,True)
labels=[("NYC",-74.01,40.71,8,-17),("Giza",31.21,30.06,8,10),("Mumbai",72.88,19.08,8,-18),("Geneva",6.14,46.20,-44,-19),("Brussels",4.35,50.85,-49,9),("Jiuquan",100.3,41,8,-17),("Jerusalem",35.21,31.77,8,-17),("Cikande",106.1,-6.1,8,8),("Benghazi",20.07,32.12,-45,-17),("Hormuz",56.3,26.5,8,8),("Pyongyang",125.75,39.02,8,-17),("Minna",6.55,9.61,8,8),("Dhaka",90.41,23.81,8,8),("Bogota",-74.07,4.71,-45,8),("Caracas",-66.88,10.48,8,-17),("Rio",-43.17,-22.91,8,8)]
for label,lon,lat,dx,dy in labels: x,y=proj(lon,lat); text(x+dx,y+dy,label,8,INK,True)

d.rectangle((28,635,996,676),fill=RED); text(46,646,"DATE CHECK",11,PAPER,True); text(145,646,"THU 26 NOV: lead + co-leads + NFL + India terminal + Wolbachia",9,PAPER); text(145,660,"WED 25 NOV: Giza, Shenzhou, Netanyahu and most briefs  |  TUE 24 NOV: Cikande update",8,(255,218,205))

stories=[("GIZA / TOP CARD","31 killed, 21 injured","WED 25 NOV / preliminary"),("SHENZHOU-24","First Pakistani in orbit","WED / Tiangong"),("NETANYAHU","Judges seek Case 4000 reset","WED / recommendation"),("CIKANDE","26 dead in factory fire","TUE / update"),("RUSSIA OIL","20+ year refining low","WED / attacks"),("HORMUZ","Mine claims in strait","WED / Iran says"),("N. KOREA","Swiss diplomat expelled","WED / sanctions"),("NIGERIA","30+ killed in Niger State","WED / attacks"),("BANGLADESH","100+ bank branches burned","WED / unrest"),("BTC","About $60,300","WED / rebound"),("COLOMBIA","10 years after peace deal","WED / UN warning"),("VENEZUELA","$237.5bn debt revealed","WED / reset"),("PETROBRAS","$122bn investment plan","WED / Brazil"),("BEPICOLOMBO","Mercury reached","WED / 8-year mission"),("DART","Stadium-sized crater","WED / asteroid test"),("RUSSIA","Nearly 500,000 lost","WED / own figures"),("CHINA","Xi graft probe in Shanghai","WED / party chief"),("CONGO","Ebola workers evacuated","WED / fighting"),("YEMEN","Houthis claim refinery attack","WED / Saudi Arabia"),("EU SANCTIONS","22nd package proposed","WED / Russia"),("NATO","Space defence vow","WED / satellite report"),("COLOMBIA","20 supermarket hostages freed","WED / 17 hours"),("ECOWAS","Security force roadmap","WED / 2027"),("ABREGO","Leaving US for Spain","WED / deportation case"),("NIGERIA","$200m meth seized","WED / five arrested"),("US ARMY","10,000-lb detonation","WED / Iowa"),("MELANIA","Nine children reunited","WED / families"),("SANDRINGHAM","Two charged in break-in","WED / England"),("NFL","Thanksgiving triple-header","THU / Detroit, Dallas, Buffalo"),("KAMARAJAR","4,288-crore terminal","WED / India cabinet"),("WOLBACHIA","68% fewer viral infections","WED / Brazil")]
for i,(head,body,date) in enumerate(stories):
    col=i%4; row=i//4; x=28+col*242; y=689+row*38; d.rectangle((x,y,x+226,y+33),fill=(242,240,234),outline=RULE,width=1); d.rectangle((x,y,x+5,y+33),fill=RED if i%3==0 else GOLD); text(x+12,y+4,head,8,RED_DARK if i%3==0 else INK,True); text(x+12,y+15,body,8,INK); text(x+12,y+25,date,7,GREY)
assert len(stories) == 31
text(28,1004,"COUNT: 36 DISTINCT STORIES (1 lead + 4 co-lead stories + 31 lower-grid/top-card items)  |  9 regions  |  UTC day rail",9,GREY,True)
img.save("/home/hatch/workspace/makefun/news-image-20261126-01/entry.png",optimize=True)
