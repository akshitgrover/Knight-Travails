#Module to display chess board graphically:

import tkinter
root=tkinter.Tk()
root.geometry('1265x800')
frame=tkinter.Frame(bg="#CCCCFF")
frame.pack(fill="both",expand="true")


#Initializations:

board=[]
chess_board=[]


#Getting Position of the king:

l1=tkinter.Label(frame,text="Enter Position Of King: ",bg="#330033",fg="#FFFFFF",relief="groove",pady=5,font=16)
l1.place(relx=0.35,rely=0.35)
e=tkinter.Entry(frame)
e.place(relx=0.5,rely=0.359)
l1=tkinter.Label(frame,text="Enter Position Of Queen: ",bg="#330033",fg="#FFFFFF",relief="groove",pady=5,font=16)
l1.place(relx=0.35,rely=0.45)
e1=tkinter.Entry(frame)
e1.place(relx=0.5,rely=0.459)

def get():
    def reachqueen():
        
        def moves():
            
            #To calculate the number of moves required from destination node to other nodes on the board:
            i=0
            while(i<7):
                temp_board=[]
                for j in range(0,len(board[i])):
                    counter=0
                    if(board[i][j][0]-2>=0 and board[i][j][1]-1>=0 and ((board[i][j][0]-2,board[i][j][1]-1) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]-2,board[i][j][1]-1))
                        counter+=1
                    if(board[i][j][0]-1>=0 and board[i][j][1]-2>=0 and ((board[i][j][0]-1,board[i][j][1]-2) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]-1,board[i][j][1]-2))
                        counter+=1
                    if(board[i][j][0]+1<8 and board[i][j][1]-2>=0 and ((board[i][j][0]+1,board[i][j][1]-2) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]+1,board[i][j][1]-2))
                        counter+=1
                    if(board[i][j][0]+1<8 and board[i][j][1]+2<8 and ((board[i][j][0]+1,board[i][j][1]+2) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]+1,board[i][j][1]+2))
                        counter+=1
                    if(board[i][j][0]-2>=0 and board[i][j][1]+1<8 and ((board[i][j][0]-2,board[i][j][1]+1) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]-2,board[i][j][1]+1))
                        counter+=1
                    if(board[i][j][0]-1>=0 and board[i][j][1]+2<8 and ((board[i][j][0]-1,board[i][j][1]+2) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]-1,board[i][j][1]+2))
                        counter+=1
                    if(board[i][j][0]+2<8 and board[i][j][1]+1<8 and ((board[i][j][0]+2,board[i][j][1]+1) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]+2,board[i][j][1]+1))
                        counter+=1
                    if(board[i][j][0]+2<8 and board[i][j][1]-1>=0 and ((board[i][j][0]+2,board[i][j][1]-1) not in board[i-1]+reachq)):
                        temp_board.append((board[i][j][0]+2,board[i][j][1]-1))
                        counter+=1
                board.append(list((set(temp_board))))
                i+=1

            # To generate a 8X8 chessboard:
            for i in range(0,8):
                temp_board=[]
                for j in range(0,8):
                    temp_board.append(-1)
                chess_board.append(temp_board)

            # To fill the calculate distances of the nodes into a list of 8 as distances are stored in adjacency list:

            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    chess_board[board[i][j][0]][board[i][j][1]]=i
                    
            #Printing the minimum number of moves required to reach the destination nodes from source node:

            x,y=e3.get().split()
            x=int(x)-1
            y=int(y)-1

            path=[(x+1,y+1)] #List to store the nodes in the path of knight to reach the king.
            for i in range(0,len(board)):
                flag=0
                for j in range(0,len(board[i])):
                    if (x,y) in board[i]:
                        moves=i;
                        flag=1
                        break #Break if destination node is found.

        
                #To Find the path travelled by knight using greedy approach '-----Dikjstra's Algorithm-----'.
        
                if(flag==1): 
                    j=i
                    while(j<=i and j>0):
                        if(x-2>=0 and y-1>=0 and chess_board[x-2][y-1]==j-1 and j>0):
                            path.append((x-1,y))        
                            x-=2
                            y-=1
                            j-=1
                        if(x-2>=0 and y+1<8 and chess_board[x-2][y+1]==j-1 and j>0):
                            path.append((x-1,y+2))
                            x-=2
                            y+=1
                            j-=1
                
                        if(x+2<8 and y-1>=0 and chess_board[x+2][y-1]==j-1 and j>0):
                            path.append((x+3,y))
                            x+=2
                            y-=1
                            j-=1
                        if(x+2<8 and y+1<8 and chess_board[x+2][y+1]==j-1 and j>0):
                            path.append((x+3,y+2))
                            x+=2
                            y+=1
                            j-=1
                        if(x-1>=0 and y-2>=0 and chess_board[x-1][y-2]==j-1 and j>0):
                            path.append((x,y-1))
                            x-=1
                            y-=2
                            j-=1
                        if(x-1>=0 and y+2<8 and chess_board[x-1][y+2]==j-1 and j>0):
                            path.append((x,y+3))
                            x-=1
                            y+=2
                            j-=1
                        if(x+1<8 and y-2>=0 and chess_board[x+1][y-2]==j-1 and j>0):
                            path.append((x+2,y-1))
                            x+=1
                            y-=2
                            j-=1
                        if(x+1<8 and y+2<8 and chess_board[x+1][y+2]==j-1 and j>0):
                            path.append((x+2,y+3))
                            x+=1
                            y+=2
                            j-=1
                    break #Break if inner loop is broke ie. destination node is found.

            #Showing The Output:
                
            fr.destroy()
            frame=tkinter.Frame(bg="#CCCCFF")
            frame.pack(fill="both",expand="true")
            if(flag==0):
                l1=tkinter.Label(frame,text="Cannot Reach The King, The Queen Protects Her King !",bg="#330033",fg="#FFFFFF",relief="groove",pady=16,font=16)
                l1.place(relx=0.33,rely=0.15)
                for i in range(0,8):
                    for j in range(0,8):
                        if((i,j) in reachq and (i,j)!=(qx,qy) and (i+1,j+1)!=path[0] and (i,j)!=board[0][0]):
                            l=tkinter.Label(frame,text="     ",bg="#FF0000",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                            l.place(relx=(6+j)/20,rely=(5+i)/20)
                        elif((i,j)==(qx,qy)):
                            l=tkinter.Label(frame,text=" Q ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                            l.place(relx=(6+j)/20,rely=(5+i)/20)
                        elif((i,j)==board[0][0]):
                            l=tkinter.Label(frame,text=" K ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                            l.place(relx=(6+j)/20,rely=(5+i)/20)
                        elif((i+1,j+1)==path[0]):
                            l=tkinter.Label(frame,text=" O ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                            l.place(relx=(6+j)/20,rely=(5+i)/20)
                        else:
                            l=tkinter.Label(frame,text="     ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                            l.place(relx=(6+j)/20,rely=(5+i)/20)
                            
            else:
                l2=tkinter.Label(frame,text=str(moves)+" is/are required to reach the king !",bg="#330033",fg="#FFFFFF",relief="groove",pady=16,font=16,padx=7)
                l2.place(relx=0.38,rely=0.15)
                for i in range(0,8):
                    for j in range(0,8):
                        if((i+1,j+1)in path):
                            if((i+1,j+1)== path[moves]):
                                l=tkinter.Label(frame,text=" K ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                            elif((i+1,j+1)== path[0]):
                                l=tkinter.Label(frame,text=" O ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                            else:
                                l=tkinter.Label(frame,text="     ",bg="#000000",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                        else:
                            if((i,j)==(qx,qy)):
                                l=tkinter.Label(frame,text=" Q ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                            elif((i,j) in reachq):
                                l=tkinter.Label(frame,text="     ",bg="#FF0000",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                            else:
                                l=tkinter.Label(frame,text="     ",bg="#FFFFFF",fg="#000000",relief="groove",pady=7,font=16,padx=7)
                                l.place(relx=(6+j)/20,rely=(5+i)/20)
                        
            

        #To Caluculate the reach of queen:

        reachq=[]

        #To Store horizontal and vertical nodes:

        for i in range(0,qx):
            reachq.append((i,qy))
        for i in range(0,qy):
            reachq.append((qx,i))
        for i in range(qx,8):
            reachq.append((i,qy))
        for i in range(qy,8):
            reachq.append((qx,i))
        tempx=qx
        tempy=qy


        #To Store Diogonal nodes:

        while(tempx<7 and tempy<7):
            reachq.append((tempx+1,tempy+1))
            tempx+=1
            tempy+=1
        tempx=qx
        tempy=qy
        while(tempx>0 and tempy>0):
            reachq.append((tempx-1,tempy-1))
            tempx-=1
            tempy-=1
        tempx=qx
        tempy=qy
        while(tempx>0 and tempy<7):
            reachq.append((tempx-1,tempy+1))
            tempx-=1
            tempy+=1
        tempx=qx
        tempy=qy
        while(tempx<7 and tempy>0):
            reachq.append((tempx+1,tempy-1))
            tempx+=1
            tempy-=1
        moves()
        
    #To get the values in entry:
            
    temp=e.get()
    i,j=temp.split() # Address of destination node.
    i=int(i)-1
    j=int(j)-1
    board.append([(i,j)])
    
    #Position Of Queen
    qx,qy=e1.get().split()
    qx=int(qx)-1 #Initial abcissa of node of the queen.
    qy=int(qy)-1 #Initial ordinate of node of the queen.

    
    frame.destroy()
    fr=tkinter.Frame(bg="#CCCCFF")
    fr.pack(fill="both",expand="true")
    l1=tkinter.Label(fr,text="Enter Position Of Knight: ",bg="#330033",fg="#FFFFFF",relief="groove",pady=5,font=16)
    l1.place(relx=0.35,rely=0.35)
    e3=tkinter.Entry(fr)
    e3.place(relx=0.5,rely=0.359)
    b1=tkinter.Button(fr,text="Submit",bg="#FFFFFF",fg="blue",relief="groove",command=reachqueen)
    b1.place(relx=0.47,rely=0.55) 

b1=tkinter.Button(frame,text="Submit",bg="#FFFFFF",fg="blue",relief="groove",command=get)
b1.place(relx=0.47,rely=0.55)    
root.mainloop()
