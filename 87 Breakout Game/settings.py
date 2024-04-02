# BRICKS
BRICK_GAP = 4
BRICK_WIDTH = BRICK_GAP * 8
BRICK_HEIGHT = BRICK_WIDTH // 2
BRICKS_PER_ROW = 14
# BALLS
BALL_SIZE = BRICK_GAP * 2
BALL_SPEED = .007
NUMBER_OF_BALLS = 3
SPEED_MULTIPLIER = .5
# WINDOW
SCREEN_WIDTH = (BRICK_WIDTH + BRICK_GAP) * BRICKS_PER_ROW + BRICK_GAP
SCREEN_HEIGHT = SCREEN_WIDTH * (1 + 5 ** 0.5) / 2 // BRICK_GAP * BRICK_GAP
# SCOREBOARD
SCOREBOARD_HEIGHT = (BRICK_HEIGHT + BRICK_GAP) * 8
SCOREBOARD_TOP = SCREEN_HEIGHT // 2
FONT_NAME = 'Courier'
# PLAY AREA
SCREEN_TOP = SCREEN_HEIGHT // 2 - SCOREBOARD_HEIGHT
SCREEN_BOTTOM = SCREEN_HEIGHT // -2
SCREEN_LEFT = SCREEN_WIDTH // -2
SCREEN_RIGHT = SCREEN_WIDTH // 2
# PADDLE
PADDLE_WIDTH = 20 * 5
PADDLE_HEIGHT = BALL_SIZE
PADDLE_Y = SCREEN_BOTTOM + PADDLE_HEIGHT * 5
# OTHER
GRAVEYARD = (1000, 1000)
