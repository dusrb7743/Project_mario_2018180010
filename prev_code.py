from pico2d import *

background_Width, background_Height = 1200, 800

def handle_events():
    global running
    global dir, accl
    global jump, jump_y
    global gravity
    global mario_status
    global y, ground_y                     # y는 마리오가 커질때 땅속에 박히지 않게 하기위해 --> 이거 코드 다시 고칠 필요가 있어보임
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                if mario_status != -1:
                    mario_status = -1
                    y, ground_y = y - 50, ground_y - 50
            elif event.key == SDLK_2:
                if mario_status == -1:
                    mario_status = 0
                    y, ground_y = y + 50, ground_y + 50
                elif mario_status == 1:
                    mario_status = 0
            elif event.key == SDLK_3:
                if mario_status == -1:
                    mario_status = 1
                    y, ground_y = y + 50, ground_y + 50
                elif mario_status == 0:
                    mario_status = 1

            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

        if event.type == SDL_KEYDOWN and event.key == SDLK_x and jump == False:
            jump = True

    if jump == True:
        jump_y = 45
        gravity += 3


    if dir == 1 and accl < Max_accl and accl >= 0:                # 가만히 있다가 달릴때 서서히 빨라지게
        accl += 0.08
    elif dir == -1 and accl > (-Max_accl) and accl <= 0:
        accl -= 0.08
    elif dir == 1 and accl < 0:                     # 가속 있는데 갑자기 방향 바꿀때
        accl += 0.2
    elif dir == -1 and accl > 0:
        accl -= 0.2
    elif dir == 0 and accl > 0:                     # 달리는 도중 키를 때면 서서히 멈추게
        accl -= 0.15
        if accl < 0:
            accl = 0
    elif dir == 0 and accl < 0:
        accl += 0.15
        if accl > 0:
            accl = 0


open_canvas(background_Width, background_Height)
background = load_image('background3.png')
lmario_right = load_image('little_mario_sheet_right.png')           #lmario == little 마리오
lmario_left = load_image('little_mario_sheet_left.png')
lmario_stand_right = load_image('little_mario_stand_right.png')
lmario_stand_left = load_image('little_mario_stand_left.png')
lmario_jump_right = load_image('little_mario_jump_right.png')
lmario_jump_left = load_image('little_mario_jump_left.png')
mario_right = load_image('mario_sheet_right.png')
mario_left = load_image('mario_sheet_left.png')
mario_stand_right = load_image('mario_stand_right.png')
mario_stand_left = load_image('mario_stand_left.png')
mario_jump_right = load_image('mario_jump_right.png')
mario_jump_left = load_image('mario_jump_left.png')
smario_right = load_image('Smario_sheet_right.png')
smario_left = load_image('Smario_sheet_left.png')
smario_stand_right = load_image('Smario_stand_right.png')
smario_stand_left = load_image('Smario_stand_left.png')
smario_jump_right = load_image('Smario_jump_right.png')
smario_jump_left = load_image('Smario_jump_left.png')



running = True
jump = False

jump_y = 0      # 점프 량 값
x = 300
cx = x       # cx 는 바로 직전의 x를 표시 cx 와 x 를 비교하여 캐릭터의 방향과 움직임을 표기
y = 160         # 현대 땅위에
# cy = y
ground_y = 160  # 땅의 y값
gravity = 0    # 중력값
frame = 0       # 프레임
dir = 0         # 방향값
accl = 0        # 가속값
Max_accl = 1    # 최대 가속값
turn = 0        # 좌우 방향 도는 값
mario_status = -1       # 마리오 상태: -1 = 작은마리오, 0 = 일반 마리오, 1 = 플라워마리오

while running:

    clear_canvas()
    background.draw(600, 400)
    if mario_status == -1:
        if (x > cx and jump == False):
            lmario_right.clip_draw(frame * 120, 0, 102, 90, x, y)
            turn = 0
        elif (x < cx and jump == False):
            lmario_left.clip_draw(frame * 120, 0, 102, 90, x, y)
            turn = -1
        elif (turn == 0 and jump == False):
            lmario_stand_right.draw(x, y)
        elif (turn == -1 and jump == False):
            lmario_stand_left.draw(x, y)
        elif (x > cx and jump == True):
            lmario_jump_right.draw(x, y)
            turn = 0
        elif (x < cx and jump == True):
            lmario_jump_left.draw(x, y)
            turn = -1
        elif (x == cx and jump == True and turn == 0):
            lmario_jump_right.draw(x, y)
        elif (x == cx and jump == True and turn == -1):
            lmario_jump_left.draw(x, y)

    elif mario_status == 0:
        if (x > cx and jump == False):
            mario_right.clip_draw(frame * 120, 0, 120, 180, x, y)
            turn = 0
        elif (x < cx and jump == False):
            mario_left.clip_draw(frame * 120, 0, 120, 180, x, y)
            turn = -1
        elif (turn == 0 and jump == False):
            mario_stand_right.draw(x, y)
        elif (turn == -1 and jump == False):
            mario_stand_left.draw(x, y)
        elif (x > cx and jump == True):
            mario_jump_right.draw(x, y)
            turn = 0
        elif (x < cx and jump == True):
            mario_jump_left.draw(x, y)
            turn = -1
        elif (x == cx and jump == True and turn == 0):
            mario_jump_right.draw(x, y)
        elif (x == cx and jump == True and turn == -1):
            mario_jump_left.draw(x, y)

    elif mario_status == 1:
        if (x > cx and jump == False):
            smario_right.clip_draw(frame * 100, 0, 100, 180, x, y)
            turn = 0
        elif (x < cx and jump == False):
            smario_left.clip_draw(frame * 100, 0, 100, 180, x, y)
            turn = -1
        elif (turn == 0 and jump == False):
            smario_stand_right.draw(x, y)
        elif (turn == -1 and jump == False):
            smario_stand_left.draw(x, y)
        elif (x > cx and jump == True):
            smario_jump_right.draw(x, y)
            turn = 0
        elif (x < cx and jump == True):
            smario_jump_left.draw(x, y)
            turn = -1
        elif (x == cx and jump == True and turn == 0):
            smario_jump_right.draw(x, y)
        elif (x == cx and jump == True and turn == -1):
            smario_jump_left.draw(x, y)

    update_canvas()

    handle_events()
    cx = x
    cy = y
    frame = (frame + 1) % 3
    if dir == 1:                    # 오른쪽으로 가고있을때 가속 붙여서 x좌표 오른쪽으로
        x += dir * 25 * accl
    elif dir == -1:                 # 왼쪽으로 가고있을때 가속 붙여서 x좌표 왼쪽으로
        x += dir * 25 * (-accl)
    elif dir == 0 and turn == 0:    # 오른쪽으로 가다 멈출때
        x += 20 * accl
    elif dir == 0 and turn == -1:   # 왼쪽으로 가다 멈출때
        x += 20 * accl

    y += jump_y - gravity
    if y < ground_y:
        y = ground_y
        jump = False
        gravity = 0
        jump_y = 0

    delay(0.03)

close_canvas()