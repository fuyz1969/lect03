"""
    作者：
    功能
    版本
    日期


"""
import turtle

def draw_pentagrm(size):
    i = 1
    while i <= 5:
        turtle.forward(size)
        turtle.right(144)
        i += 1

def draw_recursive_pentagram(size):
    """


    :param size:
    :return:
    """
    i = 1
    while i <= 5:
        turtle.forward(size)
        turtle.right(144)
        i += 1
    size +=10
    if size <= 100:
        draw_recursive_pentagram(size)

def main():
    """


    :return:
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor('blue')

    size = 50
    # while size<=500:
    #
    #     draw_pentagrm(size)
    #     # size = size +100
    #     size +=10
    draw_recursive_pentagram(size)

    turtle.exitonclick()
    # turtle.forward(300)
    # trutle.right(144)
    # turtle.forward(300)
    # trutle.right(144)
    # turtle.forward(300)
    # trutle.right(144)
    # turtle.forward(300)
    # trutle.right(144)




if __name__ == '__main__':
    main()