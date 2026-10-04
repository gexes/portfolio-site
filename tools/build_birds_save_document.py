"""Build the Birds save diagram and PDF from the reviewed Markdown source.

Requires reportlab, pypdf, pypdfium2. Run from any working directory.
"""
from pathlib import Path
import html
import re
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from pypdf import PdfReader, PdfWriter
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'assets/documents'
TEMP = ROOT / 'tmp/pdfs'
TEMP.mkdir(parents=True, exist_ok=True)
(ROOT / 'assets/svg').mkdir(parents=True, exist_ok=True)
FONTS = ROOT / 'assets/fonts'
pdfmetrics.registerFont(TTFont('Oxanium', str(FONTS/'Oxanium-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Oxanium-Bold', str(FONTS/'Oxanium-Bold.ttf')))
pdfmetrics.registerFontFamily('Oxanium',normal='Oxanium',bold='Oxanium-Bold',italic='Oxanium',boldItalic='Oxanium-Bold')
W, H = 1600, 1330
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
       '<title id="title">Birds of Impalitism: save flow and connected systems</title>',
       '<desc id="desc">Runtime owners feed SaveGameController and SaveData, which SaveSystem writes to save.json. Explicit or queued loading restores the player, pickup and reveal IDs, and area tear UI. World flags are an unsupported dictionary; batteryCharge is unused.</desc>',
       '<style>@font-face{font-family:Oxanium;src:url("../fonts/Oxanium-Regular.ttf")}@font-face{font-family:Oxanium;src:url("../fonts/Oxanium-Bold.ttf");font-weight:700}text{font-family:Oxanium,Arial,sans-serif}</style>']
c = canvas.Canvas(str(TEMP / 'diagram.pdf'), pagesize=(W, H))
BG, INK, MUTED, BLUE, AMBER = '#ffffff', '#202831', '#364653', '#103a57', '#704600'

def rect(x, y, w, h, fill, stroke=None, radius=14):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke or fill}"/>')
    c.setFillColor(colors.HexColor(fill)); c.setStrokeColor(colors.HexColor(stroke or fill))
    c.roundRect(x, H-y-h, w, h, radius, fill=1, stroke=1)

def text(x, y, value, size=23, color=INK, bold=False, mono=False):
    family = 'Oxanium, sans-serif'
    svg.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{700 if bold else 400}">{html.escape(value)}</text>')
    c.setFillColor(colors.HexColor(color)); c.setFont('Oxanium-Bold' if bold or mono else 'Oxanium', size)
    c.drawString(x,H-y,value)

def line(x1,y1,x2,y2):
    svg.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#687681" stroke-width="3" fill="none"/>')
    c.setStrokeColor(colors.HexColor('#687681')); c.setLineWidth(3); c.line(x1,H-y1,x2,H-y2)

def centered(x,y,value,size=30,color=BLUE,bold=True):
    font='Oxanium-Bold' if bold else 'Oxanium'
    from reportlab.pdfbase.pdfmetrics import stringWidth
    text(x-stringWidth(value,font,size)/2,y,value,size,color,bold)

def uml(x,y,w,h,title,lines,highlight=False,title_size=30,body_size=27):
    rect(x,y,w,h,'#ffffff','#969ba0',radius=5)
    if highlight:
        rect(x+1,y+1,w-2,58,'#b9dfec',radius=4)
    line(x,y+60,x+w,y+60)
    centered(x+w/2,y+41,title,title_size)
    for i,value in enumerate(lines): text(x+22,y+99+i*37,value,body_size)

rect(0,0,W,H,BG,radius=0)
uml(470,40,660,177,'SaveGameController',[
    'SaveGame() / LoadGame()',
    'Persistent controller; queued scene load'
],highlight=True,title_size=38,body_size=29)
line(800,217,800,255)
line(224,255,1376,255)
for x in (224,608,992,1376): line(x,255,x,290)

uml(48,290,352,226,'Player Transform',[
    'Position + yaw',
    'Found at save/load time',
    'Controller disabled',
    'while applying transform'
],body_size=25)
uml(432,290,352,263,'BatteryPickupManager',[
    'Collected pickup IDs',
    'Completed reveal IDs',
    'BatteryPickup +',
    'DialogueReveal',
    'Restore object visibility'
],title_size=28,body_size=25)
uml(816,290,352,263,'TimePeriodChanger',[
    'Area tear counts + UI',
    'Registry:',
    'TimePeriodChangerManager',
    'Last area set by trigger',
    'Restore counts and UI'
],title_size=29,body_size=24)
uml(1200,290,352,226,'WorldStateManager',[
    'Boolean flags API',
    'SaveFlags / LoadFlags',
    'Dictionary unsupported',
    'by JsonUtility'
],title_size=29,body_size=25)

line(470,128,26,128); line(26,128,26,746); line(26,746,400,746)
text(48,624,'Save: gather state',26,MUTED)
text(48,661,'Load: restore state',26,MUTED)
text(48,698,'through the controller',26,MUTED)

uml(400,610,800,270,'SaveData',[],title_size=36)
for i,value in enumerate(['playerX, playerY, playerZ','playerRotY','collectedBatteryIDs','revealedDialogueIDs']):
    text(424,713+i*36,value,25,mono=True)
for i,value in enumerate(['tearCountEnterance','tearCountBeach','tearCountFoodCourt','lastTimePeriodArea']):
    text(839,713+i*36,value,25,mono=True)
text(424,862,'batteryCharge: unused   |   worldFlags: not serialized',26,AMBER)

line(800,880,800,930)
uml(400,930,800,170,'SaveSystem',[
    'JsonUtility: ToJson / FromJson<SaveData>',
    'File: WriteAllText / ReadAllText'
],title_size=36,body_size=29)
text(1226,968,'Save triggers',26,BLUE,True)
text(1226,1005,'F5 / pause save',25)
text(1226,1042,'InteractableLevelTear',25)
text(48,967,'Load triggers',26,BLUE,True)
text(48,1004,'F9 / pause load',25)
text(48,1041,'Queued -> sceneLoaded',25)
line(800,1100,800,1145)
uml(400,1145,800,125,'save.json',[
    'Application.persistentDataPath + "/save.json"'
],title_size=34,body_size=28)
centered(800,1310,'Scene destination / returnScene is not stored in SaveData.',25,MUTED,False)
svg.append('</svg>')
(ROOT/'assets/svg/birds-of-impalitism-save-flow.svg').write_text('\n'.join(svg),encoding='utf-8')
c.save()
diagram = pdfium.PdfDocument(str(TEMP/'diagram.pdf'))
diagram[0].render(scale=1.5).to_pil().save(ROOT/'assets/png/birds-of-impalitism-save-flow.png')
diagram.close()

styles = {
    'title': ParagraphStyle('title',fontName='Oxanium-Bold',fontSize=25,leading=32,textColor=colors.HexColor(BLUE),spaceAfter=19),
    'sub': ParagraphStyle('sub',fontName='Oxanium-Bold',fontSize=16,leading=23,textColor=colors.HexColor(BLUE),spaceBefore=11,spaceAfter=9),
    'body': ParagraphStyle('body',fontName='Oxanium',fontSize=12.5,leading=18.5,textColor=colors.HexColor(INK),spaceAfter=11),
    'list': ParagraphStyle('list',fontName='Oxanium',fontSize=12,leading=17.5,leftIndent=13,firstLineIndent=-13,textColor=colors.HexColor(INK),spaceAfter=7),
}

def inline(value):
    value=html.escape(value)
    value=re.sub(r'`([^`]+)`',r'<font name="Oxanium-Bold" color="#103a57" size="10">\1</font>',value)
    value=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',value)
    url='https://docs.unity3d.com/2022.3/Documentation/Manual/JSONSerialization.html'
    value=value.replace(url,f'<link href="{url}" color="{BLUE}">Unity 2022.3 JSON Serialization manual</link>')
    return value

def footer(canv,doc):
    canv.setStrokeColor(colors.HexColor('#82909a')); canv.line(48,43,564,43)
    canv.setFont('Oxanium-Bold',9); canv.setFillColor(colors.HexColor(MUTED))
    canv.drawString(48,29,'Birds of Impalitism | Unity Save System Documentation')
    canv.drawRightString(564,29,str(doc.page+(2 if doc.page>=12 else 1)))

parts=(DOCS/'birds-of-impalitism-design.md').read_text(encoding='utf-8').split('<!-- page -->')[1:]
story=[]
for i,part in enumerate(parts):
    if i: story.append(PageBreak())
    for block in re.split(r'\n\s*\n',part.strip()):
        lines=block.splitlines()
        if block.startswith('# '): story.append(Paragraph(inline(block[2:]),styles['title']))
        elif block.startswith('## '): story.append(Paragraph(inline(block[3:]),styles['sub']))
        elif block.startswith('!['):
            # The architecture diagram gets a dedicated, near-full-page landscape sheet.
            continue
        elif all(re.match(r'^(- |\d+\. )',line) for line in lines):
            for line in lines:
                if line.startswith('- '): line='- '+line[2:]
                story.append(Paragraph(inline(line),styles['list']))
        else: story.append(Paragraph(inline(' '.join(lines)),styles['body']))

doc=SimpleDocTemplate(str(TEMP/'body.pdf'),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=54)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
cover_art=PdfReader(str(DOCS/'archive/birds-of-impalitism-design-original.pdf')).pages[0].images[0].image
cover_art_path=TEMP/'cover-art.png'
cover_art.save(cover_art_path)
cover=canvas.Canvas(str(TEMP/'cover.pdf'),pagesize=(612,792))
cover.setFillColor(colors.HexColor('#142839'));cover.rect(0,0,612,792,stroke=0,fill=1)
cover.setFillColor(colors.HexColor('#61d1e8'));cover.rect(48,726,516,3,stroke=0,fill=1)
cover.setFont('Oxanium-Bold',12);cover.setFillColor(colors.HexColor('#f1d56f'));cover.drawCentredString(306,687,'TECHNICAL DESIGN  /  SAVE SYSTEM')
cover.setFont('Oxanium-Bold',31);cover.setFillColor(colors.white);cover.drawCentredString(306,632,'Birds of Impalitism')
cover.setFont('Oxanium',15);cover.setFillColor(colors.HexColor('#e4edf2'));cover.drawCentredString(306,599,'Unity save and progression design')
cover.drawImage(ImageReader(cover_art_path),196,310,width=220,height=212,mask='auto')
cover.setFont('Oxanium',12);cover.setFillColor(colors.HexColor('#e4edf2'));cover.drawCentredString(306,271,'Data ownership  /  Scene transitions  /  World restoration')
cover.setFont('Oxanium-Bold',11);cover.setFillColor(colors.HexColor('#61d1e8'));cover.drawCentredString(306,70,'PROJECT SOURCE REVIEW  /  OCTOBER 3, 2026')
cover.save()

diagram_page=canvas.Canvas(str(TEMP/'diagram-page.pdf'),pagesize=(792,690))
diagram_page.setFillColor(colors.HexColor('#ffffff'));diagram_page.rect(0,0,792,690,fill=1,stroke=0)
diagram_page.setFont('Oxanium-Bold',16);diagram_page.setFillColor(colors.HexColor(BLUE));diagram_page.drawString(18,668,'SCENE FLOW  /  SAVE DATA AND CONNECTED SYSTEMS')
diagram_page.drawImage(str(ROOT/'assets/png/birds-of-impalitism-save-flow.png'),10,9,width=772,height=772*H/W,preserveAspectRatio=True,anchor='c')
diagram_page.setFont('Oxanium-Bold',9);diagram_page.setFillColor(colors.HexColor(MUTED));diagram_page.drawRightString(778,13,'13')
diagram_page.save()
writer=PdfWriter()
writer.append(PdfReader(str(TEMP/'cover.pdf')))
body_pages=PdfReader(str(TEMP/'body.pdf')).pages
diagram_inserted=False
for body_page in body_pages:
    writer.add_page(body_page)
    if not diagram_inserted and 'Scene Flow' in (body_page.extract_text() or ''):
        writer.append(PdfReader(str(TEMP/'diagram-page.pdf')))
        diagram_inserted=True
writer.add_metadata({'/Title':'Birds of Impalitism - Unity Save System Documentation','/Author':'Brandon Smith','/Subject':'Current save data ownership, scene flow, and restoration; source reviewed October 3, 2026'})
with (DOCS/'birds-of-impalitism-design.pdf').open('wb') as stream: writer.write(stream)
print('Generated SVG, PNG, and revised PDF:',len(writer.pages),'pages')
