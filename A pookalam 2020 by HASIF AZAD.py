#A pookalam 2020 by HASIF AZAD

import turtle

a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()

a.speed(11)
b.speed(11)
c.speed(11)

a.hideturtle()
b.hideturtle()
c.hideturtle()


#   function to draw circle
#-----------------------------
def circ(arclen,color):
    a.fillcolor(color)
    a.color(color)
    a.up()
    a.goto(0,-arclen)
    a.down()
    a.begin_fill()
    a.circle(arclen)
    a.end_fill()
#-----------------------------    
circ(290,'green')
circ(282,'lightgreen')
circ(250,'purple')
circ(242,'violet')


#  function for inner design
#-----------------------------
def design(dimension,color):
    b.fillcolor(color)
    b.color(color)
    for i in range(8):
        b.begin_fill()
        b.circle(dimension,90)
        b.end_fill()
        b.up()
        b.home()
        b.down()
        b.left((i+1)*45)
    
    for i in range(8):
        b.begin_fill()
        b.circle(-dimension,90)
        b.end_fill()
        b.up()
        b.home()
        b.down()
        b.right((i+1)*45)
#------------------------------
design(200,'yellow')
design(180,'gold')
design(150,'orange')

circ(135,'red')
circ(127,'yellow')



#        boat design
#------------------------------
c.fillcolor('black')

for i in range(8):    
    c.begin_fill()

    c.fd(100)
    c.circle(17,90)
    c.fd(33)
    c.left(120)
    c.fd(27)
    c.left(45)
    c.circle(8,180)
    c.right(180)
    c.fd(10)
    c.circle(-17,45)
    c.home()

    c.end_fill()
    c.home()
    c.left((i+1)*45)
#-----------------------------

circ(25,'chocolate')


#-----------------------------
a.up()
a.back(340)
a.down()
a.left(90)
for i in range(9):
    color=['green','yellow','blue','red','violet','green','yellow','blue','red','violet']
    happyonam=['h','a','p','p','y','o','n','a','m']
    a.color(color[i])
    a.write(happyonam[i],font=('',50,''))
    a.up()
    a.circle(-320,22.5)
    a.down()
