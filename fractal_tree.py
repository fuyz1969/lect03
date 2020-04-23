"""
    作者：
    功能
    版本
    日期


"""
import turtle

def draw_branch(branch_length):

    if branch_length >5 :
        if branch_length<=15:
            color = 'green'
        else:
            color = 'brown'

        turtle.color(color)

        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length-15)

        turtle.left(40)
        draw_branch(branch_length-15)

        turtle.right(20)

        turtle.color(color)
        turtle.backward(branch_length)



def main():

    color = 'brown'

    turtle.left(90)
    turtle.pensize(4)

    turtle.penup()
    turtle.backward(150)
    turtle.pendown()

    turtle.color(color)
    draw_branch(100)

    turtle.exitonclick()





if __name__ == '__main__':
    main()