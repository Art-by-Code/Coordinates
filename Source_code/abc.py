import turtle as tu   
import re   
import docx   # make sure you have there libraries installed on your system   
   
source = "ganesh"  # source = name of the coordinates file (available in github  https://github.com/Art-by-Code/Coordinates )   
# source file should present in same folder as of code file  
   
data = docx.Document("{}.docx".format(source))   
coordinates = []   
colour = []   
   
for i in data.paragraphs:   
    try :   
        coord_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)   
        coord_num_tup = []   
        color_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)   
        color_val = re.findall(r'[-+]?\d*\.\d*',color_stg_tup[0])   
        color_val_lst = [float(k) for k in color_val]   
        colour.append(tuple(color_val_lst))   
   
        for j in coord_stg_tup:   
            coord_pos = re.findall(r'[-+]?\d*\.\d*',j)   
            coord_num_lst = [float(k) for k in coord_pos]   
            coord_num_tup.append(tuple(coord_num_lst))   
   
        coordinates.append(coord_num_tup)   
    except:   
        pass   
 
pen = tu.Turtle()   
screen = tu.Screen()   
   
tu.tracer(2)   
tu.hideturtle()   
pen.speed(0)   
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)   
   
for i in range(len(coordinates)):   
    draw = 1   
    path = coordinates[i]   
    col = colour[i]   
    pen.color(col)   
    pen.begin_fill()   
    for order_pair in path:   
        x,y = order_pair   
        y = -1*y   
        if draw:   
            pen.up()   
            pen.goto(x,y)   
            pen.down()   
            draw = 0   
        else:   
            pen.goto(x,y)   
    pen.end_fill()   
    pen.hideturtle()  
screen.mainloop() 
