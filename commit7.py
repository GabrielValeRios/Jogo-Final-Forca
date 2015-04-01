# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:29:24 2015

@author: Usuario
"""

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")


tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-50,40)
tartaruga.pendown()
tartaruga.color("orange")
#tartaruga.forward()
#tartaruga.backward()
    
dist = 200
angulo = -90
for i in range(2):
    tartaruga.right(angulo)  # Vira o angulo pedido
    tartaruga.forward(dist) # Avança a distancia pedida
dist=400
angulo=90
for i in range(1):
    tartaruga.left(angulo)
    tartaruga.forward(dist)


import random
import turtle
from unicodedata import normalize
def formatar(txt):
    return normalize("NFKD",txt).encode('ASCII','ignore').decode('ASCII')
if __name__ =='__main__':
    from doctest import testmod
    testmod()


palavras=open("entrada.txt",encoding="UTF-8")
ler=palavras.readlines()
List=[]
print(ler)
for r in range(len(ler)):
    List.append(ler[r].strip())
    print(List)
    s=random.choice(List)
    print(s)
    z=formatar(s).lower()
    print(z)
y=-280
x=-620
for i in range(len(z)):
        if s[i] == " ":
            tartaruga=turtle.Turtle()        
            tartaruga.penup()
            tartaruga.setpos(x,y)
            tartaruga.left(0)
            tartaruga.forward(90)
            x+=40
        else:
            tartaruga=turtle.Turtle()
            tartaruga.speed(5)
            tartaruga.penup()
            tartaruga.setpos(x,y)
            tartaruga.pendown()
            tartaruga.forward(30)
            tartaruga.color("orange")
            tartaruga.left(0)
            #tartaruga.write("_",font=("Arial",12))
            x+=40
            tartaruga.hideturtle()
acertos=0
erros=0
chutes=0
palpites = []

palpite = ""


tartaruga.write("jogador")

while (erros < 6 ):
    
    
    palpite=window.textinput("chute uma letra","letra")
    if palpite in z:
    
        while palpite in palpites:
            palpite=window.textinput("chute uma letra diferente","letra")
            
        
        palpites.append(palpite)
    
    
    if palpite in z:
        for i in range(len(z)):
            
            if palpite==z[i]:
                
                
                tartaruga.penup()
                tartaruga.setpos(-610+i*40,-280)
                tartaruga.pendown()
                tartaruga.color("black")
                tartaruga.write(palpite,font=("Arial",18))
                acertos+=1
                
                

            

    else:
        erros+=1
        
      
      
           
    
    if erros==1:
        