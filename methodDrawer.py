import sys
from PIL import Image, ImageDraw, ImageFont

def methodDrawer(printout):
	f = open(printout)
	stage = int(f.readline())
	fontSize = 36
	rows = f.readlines()
	w,h = (fontSize*stage+10,int(fontSize*len(rows)*1.2)+10)
	im = Image.new("RGB", (w,h), "white")
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("AppleGothic.ttf", fontSize)

	x = 10
	y = 10
	r = 0
	handstroke = True
	prevTrebX = x + fontSize*0.4
	prevTrebY = y + fontSize*0.6
	blueLine = "2"
	prevBlueX = x + fontSize*1.4
	prevBlueY = prevTrebY
	for curChange in rows:
		handstroke = handstroke==False
		curChange = curChange.split()
		if handstroke and curChange[1]=="1": # fix me!!
			draw.line((x,y-fontSize*.1,im.size[0]-x,y-fontSize*.1), fill='silver')
		x = 10
		for bell in curChange:
			if bell == "1":
				draw.line((prevTrebX,prevTrebY,x+fontSize*0.4,y+fontSize*0.6), fill='red', width=2)
				prevTrebX = x+fontSize*0.4
				prevTrebY = y+fontSize*0.6
			elif bell == blueLine:
				draw.line((prevBlueX,prevBlueY,x+fontSize*0.4,y+fontSize*0.6), fill='blue', width=2)
				prevBlueX = x+fontSize*0.4
				prevBlueY = y+fontSize*0.6
			if r % (len(rows)-1) == 0 or (bell != "1" and bell != blueLine):
				draw.text((x,y), bell, (0,0,0), font)
			x += fontSize
		y += fontSize*1.2
		r += 1

	im.save(printout[:-3]+"jpg")

if __name__ == "__main__":
	methodDrawer(str(sys.argv[1]))