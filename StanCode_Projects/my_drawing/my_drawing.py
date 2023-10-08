"""
File: Scared Cat
Name: Scared Cat
----------------------
TODO: draw a grey cat, put jerry's face beside it.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage


def main():
    """
    Title : Scared Cat
    Once you step into StanCode, the first you see is Karel.
    It's astonished that the basic code function can be taught by this little item.
    Just like the cat see something unreal and be stunned.(especially jerry's head on Karel)
    """
    window = GWindow(width=600, height=600, title='scared_cat')

    img = GImage('jerry2.png')
    window.add(img, x=50, y=10)

    left_ear = GPolygon()
    left_ear.add_vertex((355, 170))
    left_ear.add_vertex((335, 205))
    left_ear.add_vertex((410, 185))
    left_ear.filled = True
    left_ear.fill_color = 'grey'
    left_ear.fill = 'white'
    window.add(left_ear)

    right_ear = GPolygon()
    right_ear.add_vertex((485, 180))
    right_ear.add_vertex((435, 185))
    right_ear.add_vertex((500, 215))
    right_ear.filled = True
    right_ear.fill_color = 'grey'
    right_ear.fill = 'white'
    window.add(right_ear)

    face = GOval(220, 160, x=300, y=180)
    face.filled = True
    face.fill_color = 'grey'
    face.color = 'black'
    window.add(face)

    left_feet = GOval(50, 80, x=350, y=400)
    left_feet.filled = True
    left_feet.fill_color = 'white'
    left_feet.color = 'black'
    window.add(left_feet)

    right_feet = GOval(50, 80, x=425, y=400)
    right_feet.filled = True
    right_feet.fill_color = 'white'
    right_feet.color = 'black'
    window.add(right_feet)

    tail = GOval(50, 80, x=425, y=400)
    tail.filled = True
    tail.fill_color = 'white'
    tail.color = 'black'
    window.add(tail)

    tail = GRect(80, 25, x=460, y=370)
    tail.filled = True
    tail.fill_color = 'grey'
    tail.color = 'white'
    window.add(tail)

    tail_top = GRect(20, 24, x=535, y=370)
    tail_top.filled = True
    tail_top.fill_color = 'darkgrey'
    tail_top.color = 'grey'
    window.add(tail_top)

    tail_end = GRect(16, 24, x=510, y=370)
    tail_end.filled = True
    tail_end.fill_color = 'darkgrey'
    tail_end.color = 'grey'
    window.add(tail_end)

    body = GOval(180, 150, x=322, y=300)
    body.filled = True
    body.fill_color = 'grey'
    body.color = 'grey'
    window.add(body)

    abdomen = GOval(80, 74, x=373, y=340)
    abdomen.filled = True
    abdomen.fill_color = 'white'
    abdomen.color = 'white'
    window.add(abdomen)

    left_body1 = GOval(32, 20, x=323, y=350)
    left_body1.filled = True
    left_body1.fill_color = 'darkgrey'
    left_body1.color = 'grey'
    window.add(left_body1)

    left_body2 = GOval(32, 20, x=323, y=380)
    left_body2.filled = True
    left_body2.fill_color = 'darkgrey'
    left_body2.color = 'grey'
    window.add(left_body2)

    right_body1 = GOval(32, 20, x=468, y=350)
    right_body1.filled = True
    right_body1.fill_color = 'darkgrey'
    right_body1.color = 'grey'
    window.add(right_body1)

    right_body2 = GOval(32, 20, x=468, y=380)
    right_body2.filled = True
    right_body2.fill_color = 'darkgrey'
    right_body2.color = 'grey'
    window.add(right_body2)

    right_hand = GOval(70, 30, x=420, y=320)
    right_hand.filled = True
    right_hand.fill_color = 'white'
    right_hand.color = 'grey'
    window.add(right_hand)

    left_hand = GOval(70, 30, x=335, y=320)
    left_hand.filled = True
    left_hand.fill_color = 'white'
    left_hand.color = 'grey'
    window.add(left_hand)

    inside_face = GOval(65, 50, x=380, y=240)
    inside_face.filled = True
    inside_face.fill_color = 'white'
    inside_face.color = 'white'
    window.add(inside_face)

    nose = GOval(30, 20, x=398, y=245)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'white'
    window.add(nose)

    mouth = GRect(30, 20, x=398, y=265)
    mouth.filled = True
    mouth.fill_color = 'pink'
    mouth.color = 'white'
    window.add(mouth)

    mouth1 = GLine(420, 255, 390, 270)
    mouth1.filled = True
    window.add(mouth1)

    mouth2 = GLine(410, 255, 435, 270)
    mouth2.filled = True
    window.add(mouth2)

    right_eyebrow = GOval(30, 5, x=438, y=225)
    right_eyebrow.filled = True
    right_eyebrow.fill_color = 'black'
    right_eyebrow.color = 'grey'
    window.add(right_eyebrow)

    left_eyebrow = GOval(30, 5, x=356, y=225)
    left_eyebrow.filled = True
    left_eyebrow.fill_color = 'black'
    left_eyebrow.color = 'grey'
    window.add(left_eyebrow)

    left_eye = GOval(15, 15, x=365, y=235)
    left_eye.filled = True
    left_eye.fill_color = 'white'
    left_eye.color = 'black'
    window.add(left_eye)

    right_eye = GOval(15, 15, x=445, y=235)
    right_eye.filled = True
    right_eye.fill_color = 'white'
    right_eye.color = 'black'
    window.add(right_eye)

    top_hair1 = GOval(5, 15, x=403, y=222)
    top_hair1.filled = True
    top_hair1.fill_color = 'black'
    top_hair1.color = 'grey'
    window.add(top_hair1)

    top_hair2 = GOval(5, 15, x=415, y=222)
    top_hair2.filled = True
    top_hair2.fill_color = 'black'
    top_hair2.color = 'grey'
    window.add(top_hair2)

    left_hair1 = GOval(32, 5, x=313, y=260)
    left_hair1.filled = True
    left_hair1.fill_color = 'black'
    left_hair1.color = 'grey'
    window.add(left_hair1)

    left_hair2 = GOval(30, 5, x=315, y=275)
    left_hair2.filled = True
    left_hair2.fill_color = 'black'
    left_hair2.color = 'grey'
    window.add(left_hair2)

    right_hair1 = GOval(32, 5, x=476, y=260)
    right_hair1.filled = True
    right_hair1.fill_color = 'black'
    right_hair1.color = 'grey'
    window.add(right_hair1)

    right_hair2 = GOval(30, 5, x=478, y=275)
    right_hair2.filled = True
    right_hair2.fill_color = 'black'
    right_hair2.color = 'grey'
    window.add(right_hair2)

    top_face1 = GOval(10, 18, x=423, y=183)
    top_face1.filled = True
    top_face1.fill_color = 'darkgrey'
    top_face1.color = 'grey'
    window.add(top_face1)

    top_face2 = GOval(11, 20, x=408, y=181)
    top_face2.filled = True
    top_face2.fill_color = 'darkgrey'
    top_face2.color = 'grey'
    window.add(top_face2)

    top_face3 = GOval(10, 18, x=393, y=183)
    top_face3.filled = True
    top_face3.fill_color = 'darkgrey'
    top_face3.color = 'grey'
    window.add(top_face3)

    line1 = GLine(463, 165, 463, 210)
    line2 = GLine(464, 165, 464, 210)
    line3 = GLine(465, 165, 465, 210)
    window.add(line1)
    window.add(line2)
    window.add(line3)

    line4 = GLine(470, 167, 470, 205)
    line5 = GLine(471, 167, 471, 205)
    line6 = GLine(472, 167, 472, 205)
    window.add(line4)
    window.add(line5)
    window.add(line6)

    line7 = GLine(477, 170, 477, 201)
    line8 = GLine(478, 170, 478, 201)
    line9 = GLine(479, 170, 479, 201)
    window.add(line7)
    window.add(line8)
    window.add(line9)

    swear1 = GOval(5, 10, x=343, y=203)
    swear1.filled = True
    swear1.fill_color = 'lightblue'
    swear1.color = 'grey'
    window.add(swear1)

    swear2 = GOval(5, 10, x=483, y=235)
    swear2.filled = True
    swear2.fill_color = 'lightblue'
    swear2.color = 'grey'
    window.add(swear2)

    swear3 = GOval(5, 10, x=493, y=215)
    swear3.filled = True
    swear3.fill_color = 'lightblue'
    swear3.color = 'grey'
    window.add(swear3)


if __name__ == '__main__':
    main()
