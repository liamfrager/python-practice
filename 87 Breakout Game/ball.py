from settings import *
from turtle import Turtle
from bricks import Brick
from paddle import Paddle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.remaining_balls = []
        self.load_balls()
        self.has_hit_top_wall = False
        self.collision_buffer = 1
        self.get_new_ball()

    def load_balls(self):
        self.shapesize(BALL_SIZE / 5, BALL_SIZE / 5, 1)
        for i in range(NUMBER_OF_BALLS):
            self.home()
            self.goto(
                x=SCREEN_RIGHT - (BALL_SIZE * 5) * (i + 1),
                y=SCOREBOARD_TOP - (BRICK_HEIGHT * 4)
            )
            self.remaining_balls.append(self.stamp())
        self.shapesize(BALL_SIZE / 20, BALL_SIZE / 20, 1)

    def get_new_ball(self):
        if len(self.remaining_balls) > 0:
            self.clearstamp(self.remaining_balls[-1])
            self.remaining_balls = self.remaining_balls[:-1]
            self.goto(0, PADDLE_Y + (PADDLE_HEIGHT + BALL_SIZE) / 2)
            self.move_speed = BALL_SPEED
            self.hit_four, self.hit_twelve, self.hit_orange, self.hit_red = (
                False, False, False, False)
            self.x_move = random.choice([-2, 2])
            self.y_move = 8
            return True
        return False

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)
        # print(f'x: {self.xcor()}, y:{self.ycor()}')

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def get_object_sides(self, object: Brick):
        object_width = BRICK_WIDTH
        object_height = BRICK_HEIGHT
        object_l = object.xcor() - (object_width + BALL_SIZE) / 2
        object_r = object.xcor() + (object_width + BALL_SIZE) / 2
        object_t = object.ycor() + (object_height + BALL_SIZE) / 2
        object_b = object.ycor() - (object_height + BALL_SIZE) / 2
        return (object_l, object_r, object_t, object_b)

    def collides_x(self, object: Brick):
        object_l, object_r, object_t, object_b = self.get_object_sides(object)
        if self.xcor() == object_l or self.xcor() == object_r:
            if self.ycor() >= object_b - self.collision_buffer and self.ycor() <= object_t + self.collision_buffer:
                return True
        return False

    def collides_y(self, object: Brick):
        object_l, object_r, object_t, object_b = self.get_object_sides(object)
        if self.ycor() == object_t or self.ycor() == object_b:
            if self.xcor() >= object_l - self.collision_buffer and self.xcor() <= object_r + self.collision_buffer:
                return True
        return False

    @property
    def speed_multiplier(self):
        multiplier = SPEED_MULTIPLIER ** (self.hit_four + self.hit_twelve +
                                          self.hit_orange + self.hit_red)
        return multiplier

    def set_move_speed(self, speed):
        self.move_speed = BALL_SPEED * self.speed_multiplier * speed
        print(f'mult: {self.speed_multiplier}\nspeed: {self.move_speed}\n')
