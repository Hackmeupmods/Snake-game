import turtle
import random

# Constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0),
}

# Setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Kaila Snake Game")
screen.bgcolor("black")
screen.tracer(0)

pen = turtle.Turtle("circle")
pen.penup()
pen.color("green")

food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.speed(0)

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-WIDTH // 2 + 10, HEIGHT // 2 - 30)
score_writer.color("white")

# Game state
snake = []
snake_direction = "right"
score = 0

def get_random_food_pos():
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x // 20 * 20, y // 20 * 20)

def reset():
    global snake, snake_direction, food_pos, score
    snake.clear()
    snake.extend([[-40, 0], [-20, 0], [0, 0]])
    snake_direction = "right"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 14, "normal"))

def move_snake():
    global food_pos, score

    new_head = snake[-1].copy()
    offset = offsets[snake_direction]
    new_head[0] += offset[0]
    new_head[1] += offset[1]

    # Wrap around screen
    if new_head[0] >= WIDTH // 2:
        new_head[0] = -WIDTH // 2
    elif new_head[0] < -WIDTH // 2:
        new_head[0] = WIDTH // 2 - 20
    if new_head[1] >= HEIGHT // 2:
        new_head[1] = -HEIGHT // 2
    elif new_head[1] < -HEIGHT // 2:
        new_head[1] = HEIGHT // 2 - 20

    if new_head in snake[:-1]:
        reset()
        screen.ontimer(move_snake, DELAY)
        return

    snake.append(new_head)

    pen.clear()
    for segment in snake:
        pen.goto(segment)
        pen.stamp()

    if pen.distance(food) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        score += 10
        score_writer.clear()
        score_writer.write(f"Score: {score}", font=("Arial", 14, "normal"))
    else:
        snake.pop(0)

    screen.update()
    screen.ontimer(move_snake, DELAY)

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

# Key bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start game
reset()
move_snake()
screen.mainloop()


Added snake game code manually
