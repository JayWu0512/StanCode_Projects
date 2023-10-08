"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

trigger = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self._window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset)
        self._paddle.filled = True
        self._paddle.fill_color = 'black'
        self._window.add(self._paddle)

        # Center a filled ball in the graphical window

        self._ball_r = ball_radius
        self._window_w = window_width
        self._window_h = window_height
        # self.set_a_ball()
        self._ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)/2,
                          y=(window_height-ball_radius*2)/2)
        self._ball.filled = True
        self._ball.fill_color = 'black'
        self._window.add(self._ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        # onmouseclicked(start)

        # Draw bricks
        for i in range(0, brick_rows):
            for j in range(0, brick_cols):
                self._brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*i,
                                    y=brick_offset+(brick_height+brick_spacing)*j)
                self._brick.filled = True
                if j < 2:
                    self._brick.fill_color = 'red'
                    self._brick.color = 'white'
                    self._window.add(self._brick)
                if 2 <= j < 4:
                    self._brick.fill_color = 'orange'
                    self._brick.color = 'white'
                    self._window.add(self._brick)
                if 4 <= j < 6:
                    self._brick.fill_color = 'yellow'
                    self._brick.color = 'white'
                    self._window.add(self._brick)
                if 6 <= j < 8:
                    self._brick.fill_color = 'green'
                    self._brick.color = 'white'
                    self._window.add(self._brick)
                if 8 <= j < 10:
                    self._brick.fill_color = 'blue'
                    self._brick.color = 'white'
                    self._window.add(self._brick)

    # let paddle moves
    def paddle_move(self, event):
        self._paddle.x = event.x - PADDLE_WIDTH/2
        if event.x - PADDLE_WIDTH/2 <= 0:
            self._paddle.x = 0
        elif event.x + PADDLE_WIDTH/2 >= self._window.width:
            self._paddle.x = self._window.width - PADDLE_WIDTH
        self._paddle.y = self._window.height - PADDLE_OFFSET

    # get dx and dy of the ball
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # get ball x and y while the ball moves
    def get_ball_x(self):
        return self._ball.x

    def get_ball_y(self):
        return self._ball.y

    def get_ball_r(self):
        return self._ball_r

    def get_ball(self):
        return self._ball

    # reset a ball
    def set_a_ball(self):
        self._ball = GOval(self._ball_r*2, self._ball_r*2, x=(self._window_w-self._ball_r*2)/2,
                          y=(self._window_h-self._ball_r*2)/2)
        self._ball.filled = True
        self._ball.fill_color = 'black'
        self._window.add(self._ball)

    # reset dx and dy
    def set_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    # get window for user
    def get_window(self):
        return self._window

    def get_window_width(self):
        return self._window_w

    def get_window_height(self):
        return self._window_h

    # get paddle for user
    def get_paddle(self):
        return self._paddle

