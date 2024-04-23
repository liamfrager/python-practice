SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_BOT = -SCREEN_HEIGHT // 2
SCREEN_TOP = SCREEN_HEIGHT // 2
SCREEN_L = -SCREEN_WIDTH // 2
SCREEN_R = SCREEN_WIDTH // 2

GRAVEYARD = (1000, 1000)

SHIP_MOVE_DISTANCE = 8
LASER_MOVE_DISTANCE = 12
ALIEN_MOVE_DISTANCE = 12
ALIEN_X_GAP = 48
ALIEN_Y_GAP = 40


SHIP_COLOR = 'white'
SHIP_COORDS = ((-7.5, -4), (-7.5, 0), (-6.5, 0), (-6.5, 1), (-1.5, 1), (-1.5, 3), (-0.5, 3),
               (-0.5, 4), (0.5, 4), (0.5, 3), (1.5, 3), (1.5, 1), (6.5, 1), (6.5, 0), (7.5, 0), (7.5, -4))
ALIEN_1_COLOR = 'lime'
ALIEN_1_COORDS = ((-4, 1), (-3, 1), (-3, 2), (-2, 2), (-2, 3), (-1, 3), (-1, 4), (1, 4), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (4, -1), (2, -1), (2, -2), (3, -2), (3, -3), (4, -3), (4, -4), (3, -4), (3, -3), (2, -3), (2, -2), (1, -2), (1, 0), (2, 0), (2, 1), (1, 1), (1, -1), (-1, -1),
                  (-1, 0), (-2, 0), (-2, 1), (-1, 1), (-1, -1), (-1, -2), (1, -2), (1, -3), (2, -3), (2, -4), (1, -4), (1, -3), (-1, -3), (-1, -2), (-2, -2), (-2, -3), (-1, -3), (-1, -4), (-2, -4), (-2, -3), (-3, -3), (-3, -4), (-4, -4), (-4, -3), (-3, -3), (-3, -2), (-2, -2), (-2, -1), (-4, -1))
ALIEN_2_COLOR = 'cyan'
ALIEN_2_COORDS = ((-5.5, -3), (-5.5, 0), (-4.5, 0), (-4.5, 1), (-3.5, 1), (-3.5, 2), (-2.5, 2), (-2.5, 0), (-1.5, 0), (-1.5, 1), (-2.5, 1), (-2.5, 3), (-3.5, 3), (-3.5, 4), (-2.5, 4), (-2.5, 3), (-1.5, 3), (-1.5, 2), (1.5, 2), (1.5, 3), (2.5, 3), (2.5, 4), (3.5, 4), (3.5, 3), (2.5, 3), (2.5, 0), (1.5, 0), (1.5, 1),
                  (2.5, 1), (2.5, 2), (3.5, 2), (3.5, 1), (4.5, 1), (4.5, 0), (5.5, 0), (5.5, -3), (4.5, -3), (4.5, -1), (3.5, -1), (3.5, -3), (2.5, -3), (2.5, -4), (0.5, -4), (0.5, -3), (2.5, -3), (2.5, -2), (-2.5, -2), (-2.5, -3), (-0.5, -3), (-0.5, -4), (-2.5, -4), (-2.5, -3), (-3.5, -3), (-3.5, -1), (-4.5, -1), (-4.5, -3))
ALIEN_3_COLOR = 'orangered'
ALIEN_3_COORDS = ((-6, -1), (-6, 2), (-5, 2), (-5, 3), (-2, 3), (-2, 4), (2, 4), (2, 3), (5, 3), (5, 2), (6, 2), (6, -1), (4, -1), (4, -2), (5, -2), (5, -3), (4, -3), (4, -4), (2, -4), (2, -3), (3, -3), (3, -2), (1, -2), (1, 0),
                  (3, 0), (3, 1), (1, 1), (1, -1), (-1, -1), (-1, 1), (-3, 1), (-3, 0), (-1, 0), (-1, -2), (1, -2), (1, -3), (-1, -3), (-1, -2), (-3, -2), (-3, -3), (-2, -3), (-2, -4), (-4, -4), (-4, -3), (-5, -3), (-5, -2), (-4, -2), (-4, -1))
UFO_COLOR = 'magenta'
UFO_COORDS = ((-4, 1), (-3, 1), (-3, 2), (-2, 2), (-2, 3), (-1, 3), (-1, 4), (1, 4), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (4, -1), (2, -1), (2, -2), (3, -2), (3, -3), (4, -3), (4, -4), (3, -4), (3, -3), (2, -3), (2, -2), (1, -2), (1, 0), (2, 0), (2, 1), (1, 1), (1, -1), (-1, -1),
              (-1, 0), (-2, 0), (-2, 1), (-1, 1), (-1, -1), (-1, -2), (1, -2), (1, -3), (2, -3), (2, -4), (1, -4), (1, -3), (-1, -3), (-1, -2), (-2, -2), (-2, -3), (-1, -3), (-1, -4), (-2, -4), (-2, -3), (-3, -3), (-3, -4), (-4, -4), (-4, -3), (-3, -3), (-3, -2), (-2, -2), (-2, -1), (-4, -1))

EXPLOSION_COORDS = ((0, 0), (-1, 1), (0, 1), (1, 1), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),    (-3, 3), (-2, 3), (-1, 3), (0, 3),
                    (1, 3), (2, 3), (3, 3), (-3, 4), (-2, 4),    (-1, 4), (0, 4), (1, 4), (2, 4), (3, 4), (-2, 5), (-1, 5), (0, 5), (1, 5), (2, 5))
