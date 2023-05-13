# 导入pygame模块
import pygame
# 导入random模块
import random
# 初始化pygame
pygame.init()
# 创建游戏窗口，大小为480*600
screen = pygame.display.set_mode((480, 600))
# 加载背景图片
bg = pygame.image.load("background.png")
# 绘制背景图片
screen.blit(bg, (0, 0))
# 设置游戏标题
pygame.display.set_caption("贪吃蛇")
# 创建时钟对象
clock = pygame.time.Clock()
# 定义方格的大小和颜色
SIZE = 20
COLOR = (255, 255, 255)
# 定义游戏区域的范围
AREA_X = (0, 480 // SIZE - 1)
AREA_Y = (0, 600 // SIZE - 1)
# 定义食物的颜色和分值
FOOD_COLOR = (255, 0, 0)
FOOD_SCORE = 10
# 定义字体对象和得分变量
font = pygame.font.SysFont("Arial", 32)
score = 0
# 定义蛇的初始位置和方向
snake = [(10, 10), (9, 10), (8, 10)]
direction = (1, 0)
# 定义食物的初始位置
food = (15, 15)
# 定义游戏状态变量
running = True
paused = False
game_over = False

# 定义一个函数，用于生成新的食物位置，避免与蛇重叠
def create_food(snake):
    while True:
        x = random.randint(AREA_X[0], AREA_X[1])
        y = random.randint(AREA_Y[0], AREA_Y[1])
        if (x, y) not in snake:
            return x, y

# 游戏主循环
while running:
    # 设置刷新帧率为10帧/秒
    clock.tick(10)
    # 监听事件
    for event in pygame.event.get():
        # 判断是否退出游戏
        if event.type == pygame.QUIT:
            running = False
        # 判断是否按下空格键，暂停或继续游戏
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = not paused
        # 判断是否按下方向键，改变蛇的方向（避免反向移动）
        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_UP, pygame.K_w):
            if direction[1] == 0:
                direction = (0, -1)
        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_DOWN, pygame.K_s):
            if direction[1] == 0:
                direction = (0, 1)
        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_LEFT, pygame.K_a):
            if direction[0] == 0:
                direction = (-1, 0)
        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_RIGHT, pygame.K_d):
            if direction[0] == 0:
                direction = (1, 0)
    # 如果没有暂停或结束，更新蛇的位置和状态
    if not paused and not game_over:
        # 计算蛇头的下一个位置（根据方向）
        next_x = snake[0][0] + direction[0]
        next_y = snake[0][1] + direction[1]
        # 判断是否吃到食物，如果是，增加分数和长度，生成新的食物位置；如果不是，删除蛇尾
        if (next_x, next_y) == food:
            score += FOOD_SCORE
            food = create_food(snake)
        else:
            snake.pop()
        # 判断是否撞到边界或自身，如果是，设置游戏结束标志；如果不是，将新的位置插入到蛇头
        if next_x < AREA_X[0] or next_x > AREA_X[1] or next_y < AREA_Y[0] or next_y > AREA_Y[1] or (next_x, next_y) in snake:
            game_over = True
        else:
            snake.insert(0, (next_x, next_y))
    # 绘制背景图片（覆盖之前绘制的内容）
    screen.blit(bg, (0, 0))
    # 绘制食物（覆盖之前绘制的内容）
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * SIZE + 1, food[1] * SIZE + 1, SIZE - 2 , SIZE -2))
    # 绘制蛇（覆盖之前绘制的内容）
    for s in snake:
        pygame.draw.rect(screen, COLOR, (s[0] * SIZE + 1 , s[1] * SIZE + 1 , SIZE -2 , SIZE -2))
    # 绘制得分（覆盖之前绘制的内容）
    text = font.render(f"Score: {score}", True, COLOR)
    screen.blit(text, (10 ,10))
    # 绘制游戏结束提示（覆盖之前绘制的内容）
    if game_over:
        text = font.render("Game Over!", True , COLOR)
        screen.blit(text , (180 ,280))
    # 更新屏幕显示（覆盖之前绘制的内容）
    pygame.display.update()
# 退出pygame模块    
pygame.quit()
