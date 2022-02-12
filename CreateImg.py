from PIL import Image, ImageDraw, ImageFont
from pykakasi import kakasi
HIRA = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ"
HIRA += "まみむめもやゆよらりるれろわをん"

OTHER = "ぁぃぅぇぉゃゅょっー"

kakasiObj = kakasi()


def createHiraImg(Hira):
    img = Image.new("L", (16, 16), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font/SourceHanSansJP-Medium.otf", 16)
    draw.text((0, -5), Hira, font=font)
    return img


for value in HIRA:
    img = createHiraImg(value)
    img.save("img/general/" + "".join(i["hepburn"] for i in kakasiObj.convert(value)) + ".png")

for value in OTHER:
    img = createHiraImg(value)
    img.save("img/other/" + "x" + "".join(i["hepburn"] for i in kakasiObj.convert(value)) + ".png")

exit()
