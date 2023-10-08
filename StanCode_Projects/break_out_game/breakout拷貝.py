"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLabel

# Constant
FRAME_RATE = 100        # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global Variables
trigger = True
graphics = BreakoutGraphics()
num_lives = GLabel('Num_lives: ' + str(NUM_LIVES))
num_lives.font = '-25'
graphics._window.add(num_lives, x=0, y=num_lives.height)


def main():
    # all animation of ball and paddle set inside
    animation()


def animation():
    global trigger
    global NUM_LIVES

    # set initial velocity
    graphics.set_velocity()

    # get ball and its vx and vy
    ball = graphics.get_ball()
    vx = graphics.get_vx()
    vy = graphics.get_vy()

    # get window and its weight and height
    window = graphics.get_window()
    window_w = graphics.get_window_width()
    window_h = graphics.get_window_height()

    # get paddle
    paddle = graphics.get_paddle()

    onmouseclicked(start)
    # Add the animation loop here!
    while True:
        # if trigger = False, it will move
        if not trigger:

            # start to move
            ball.move(vx, vy)

            # get ball's x and y everytime it moves
            x = graphics.get_ball_x()
            y = graphics.get_ball_y()
            r = graphics.get_ball_r()

            # get 4 top point of ball
            upper_left = window.get_object_at(x, y)
            upper_right = window.get_object_at(x + r * 2, y)
            lower_left = window.get_object_at(x, y + r * 2)
            lower_right = window.get_object_at(x + r * 2, y + r * 2)

            # the situation that ball moves out of window's bottom
            if y >= window_h-ball.width:
                # remove the ball if it is out of window
                window.remove(ball)
                # reset a ball
                graphics.set_a_ball()
                # reset its velocity
                graphics.set_velocity()
                # get the reset velocity value
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                # decrease its life and show on label
                NUM_LIVES -= 1
                num_lives.text = 'Num_lives: ' + str(NUM_LIVES)
                # open the trigger and it can be clicked
                trigger = True

                # if the lives is 0, you lose
                if NUM_LIVES == 0:
                    break

            # the situation that ball moves to window's top
            elif y < 0:
                vy = -vy
                ball.move(vx, 2 * vy)

            # the situation that ball moves to the left and right side of window
            elif x < 0 or x + r*2 > window_w:
                vx = -vx
                ball.move(2 * vx, vy)

            # the situation that ball's upper left side touch brick
            elif upper_left is not None and upper_left is not paddle and upper_left is not num_lives:
                vy = -vy
                remove(upper_left)

            # the situation that ball's upper right side touch brick
            elif upper_right is not None and upper_right is not paddle and upper_right is not num_lives:
                vy = -vy
                remove(upper_right)

            # the situation that ball's lower left side touch brick
            elif lower_left is not None:
                # when it touch to paddle
                if lower_left is paddle:
                    # avoid the ball stuck in paddle
                    if vy > 0:
                        vy = -vy
                # when it touch to brick
                else:
                    if lower_left is not paddle and lower_left is not num_lives:
                        vy = -vy
                        remove(lower_left)

            # the situation that ball's lower right side touch brick
            elif lower_right is not None:
                # when it touch to paddle
                if lower_right is paddle:
                    # avoid the ball stuck in paddle
                    if vy > 0:
                        vy = -vy
                # when it touch to brick
                else:
                    if lower_right is not paddle and lower_right is not num_lives:
                        vy = -vy
                        remove(lower_right)
        pause(FRAME_RATE)


# set the trigger
def start(event):
    global trigger
    trigger = False

# remove brick
def remove(obj):
    graphics._window.remove(obj)


if __name__ == '__main__':
    main()
