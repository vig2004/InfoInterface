import tkinter as tk
from PIL import Image,ImageTk
from random import randint
import time

MOVE_INCREMENT = 20
moves_per_second = 12
GAME_SPEED = 1000 // moves_per_second


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background='black', highlightthickness=0)

        self.snake_positions = [(100, 100),(80, 100),(60, 100)]
        self.food_positions = self.set_new_food_position()
        self.score=0
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)

        self.load_assests()
        self.create_object()

        self.after(50, self.perform_action )


    def load_assests(self):
        try:                   #try because if this fails it wont work
            self.snake_body_image=Image.open('C:/Users/INTEL/PycharmProjects/pythonProject1/iig security/img_buttons/snake.png')
            self.snake_body=ImageTk.PhotoImage(self.snake_body_image )

            self.food_body_image = Image.open('C:/Users/INTEL/PycharmProjects/pythonProject1/iig security/img_buttons/food111.png ')
            self.food_body = ImageTk.PhotoImage(self.food_body_image)
        except IOError as error:
            print(error)
            root.destroy()

    def create_object(self):
        self.create_text(
            100 , 12, text=f"score: {self.score} (speed: {moves_per_second })", tag="score", fill='white',font=('TkDefaultFont',15)
        )
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body,tag="snake")

        self.create_image(*self.food_positions,image=self.food_body, tag="food")
        self.create_rectangle(7,27,595,613,outline='white')

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions [0]
        new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)

        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position  )
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position  )
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (head_x_position,head_y_position - MOVE_INCREMENT )



        #new_head_position = (head_x_position + MOVE_INCREMENT,head_y_position)

        self.snake_positions = [new_head_position ] + self.snake_positions [:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    def perform_action(self):
        if self.check_collisions() :
            self.end_game()
            return

        self.check_food_collision()
        self.move_snake()
        self.after(GAME_SPEED,self.perform_action)

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        if head_x_position in (0, 600) or head_y_position in (20, 620):
            return True
        elif (head_x_position, head_y_position) in self.snake_positions[1:]:
            return True

    def on_key_press(self,e):
        new_direction = e.keysym
        all_directions=("Up","Down","Left","Right")
        opposites = ({"Up","Down"},{"Left","Right"})

        if (
            new_direction in all_directions
            and{new_direction, self.direction  } not in opposites
        ):
            self.direction = new_direction

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_positions:
            self.score += 5
            self.snake_positions.append(self.snake_positions[-1])

            if self.score % 5 == 0:
                global moves_per_second
                moves_per_second += 1




            self.create_image(
                *self.snake_positions[-1],image=self.snake_body,tag="snake"
            )

            self.food_positions = self.set_new_food_position()
            self.coords(self.find_withtag("food"),*self.food_positions)

            score = self.find_withtag("score")
            self.itemconfigure(score,text=f"Score: {self.score} (speed: {moves_per_second })",tag="score")

    def set_new_food_position(self):
        while True :
            x_position = randint(1,29)  * MOVE_INCREMENT
            y_position = randint(3,30)  * MOVE_INCREMENT
            food_position = (x_position,y_position  )

            if food_position not in self.snake_positions:
                return food_position

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over ! You Scored {self.score} !",
            fill='white',
            font=('TkDefaultFont',25)
        )




root=tk.Tk()
root.title('image')
root.iconbitmap('C:/Users/INTEL/PycharmProjects/pythonProject1/pics/tk1.3.ico')

board=Snake()
board.pack()



root.mainloop()