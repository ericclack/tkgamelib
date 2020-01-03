# 1, Import the library
from packages import *

# 2, numbers for the game
GRAVITY=1
FLAP_POWER=10
FLOOR_SIZE=50
GAP_SHRINK=5
SPEED_INC=1
world=Struct(gap=150,speed=20,score=0)

# 3, canvas and the player
create_canvas()

player = ImageSprite('images/face.gif')
player.move_to(350,200)
# set the players speed
# speed_y=0 is not moving, if +ve is down, -ve is up
player.speed_y=0

# 4, create walls
wall_top = ImageSprite('images/wall_top.gif')
wall_bottom = ImageSprite('images/wall_bottom.gif')
# position them on the right & put them moving left
# remember the position is the TOP LEFT corner of the image
# so we use the sprites height to set the TOP image
mid=CANVAS_HEIGHT/2
wall_top.move_to(CANVAS_WIDTH-50,mid - world.gap - wall_top.height)
wall_bottom.move_to(CANVAS_WIDTH-50,mid + world.gap)
wall_top.speed_x=-world.speed
wall_bottom.speed_x=-world.speed

# 5, create floor
# we will need CANVAS_WIDTH/sprite.width +1 sprites
world.floor=[]
for r in range(int(CANVAS_WIDTH/FLOOR_SIZE) +1):
    f=ImageSprite('images/floor.gif')
    f.move_to(FLOOR_SIZE*r, CANVAS_HEIGHT-FLOOR_SIZE+2)
    f.speed_x=-world.speed
    world.floor.append(f)

# 6, player flap and gravity
def flap():
    # flap sends the player moving upwards, so we set its speed upwards
    player.speed_y=-FLAP_POWER

def update_player():
    # add gravity:
    player.speed_y+=GRAVITY
    # move velocity
    player.move_with_speed()

# 7, move the walls
def update_walls():
    wall_top.move_with_speed()
    wall_bottom.move_with_speed()
    # if off screen move back on:
    if wall_top.x<-50:
        increase_difficulty()
        # give score
        world.score+=1
        show_variable('Score',world.score)
        # reset the walls
        mid=random.randint(300,500)
        wall_top.move_to(CANVAS_WIDTH-50,mid - world.gap - wall_top.height)
        wall_bottom.move_to(CANVAS_WIDTH-50,mid + world.gap)

# 8, increasing the difficulty in the game
def increase_difficulty():
    # make the game harder
    world.speed+=SPEED_INC
    wall_top.speed_x=-world.speed
    wall_bottom.speed_x=-world.speed
    world.gap-=GAP_SHRINK
    # speed up the floor too
    for f in world.floor:    
        f.speed_x=-world.speed
    
# 9, check for player hitting the walls
def check_for_game_over():
    if player.touching(wall_top) or player.touching(wall_bottom):
        end_game("Game Over\nScore:"+str(world.score))
    if player.y < 0 or player.y+player.height>CANVAS_HEIGHT:
        end_game("Game Over\nScore:"+str(world.score))


# 10, move the floors
def update_floor():
    for f in world.floor:
        f.move_with_speed()
        if f.x<-FLOOR_SIZE:
            f.move(CANVAS_WIDTH+FLOOR_SIZE,0)

# 11, the main loop
def update():
    update_player()
    update_walls()
    check_for_game_over()
    update_floor()
    

# 12, setup all the functions and the main program loop
show_variable('Score',world.score)

when_key_pressed('<space>', flap)
forever(update, 25)

mainloop()
