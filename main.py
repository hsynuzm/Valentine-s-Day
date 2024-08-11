import turtle
import time


def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-112, 200)
    turtle.left(120)
    turtle.circle(-112, 200)
    turtle.forward(224)
    turtle.end_fill()


def create_heart_with_text(text):
    turtle.speed(1)
    turtle.bgcolor("black")
    turtle.title("Kalp Çizimi")

    turtle.penup()
    turtle.goto(0, -112)
    turtle.setheading(0)
    turtle.pendown()

    draw_heart()

    turtle.penup()
    turtle.goto(0, 70)
    turtle.color("white")
    turtle.write(text, align="center", font=("Arial", 18, "bold"))
    turtle.hideturtle()


def main():
    user_input = input("Enter your cutom text (Your Love!!): ")

    while True:
        turtle.clear()
        create_heart_with_text(user_input)
        time.sleep(1)


if __name__ == "__main__":
    main()
    turtle.done()
