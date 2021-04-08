from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time

# ----------------------- START OF CLASS/METHOD DECLARATIONS -----------------------

# GamePlay class: methods for displaying/removing the values from tiles, tallying up the score, and ending the game


class GamePlay:

    def display_value(tile, x, y):
        global hit, game_over_var, tile_dict, temp_level
        num = IntVar()
        num.set(x)
        tile.configure(text=x)  # prints the value to the tile
        capture_values.append(x)  # this appends the shuffled list value to 'capture_values' list
        tile_store.append(tile_dict[y])  # this appends the previous 2 clicked tiles into 'tile_store' list
        hit += 1  # increments the hit variable to track how many times the user clicks

        if hit == 2:  # we need to wait for 2 clicks before we choose any action

            message_success = "Success!"
            message_fail = "Try again!"

            #   in case the user presses the same tile twice:
            if tile_store[0] == tile_store[1]:
                messagebox.showinfo("Memory Game", "You can't press the same tile twice!")
                GamePlay.remove_value(tile_store[0])
                GamePlay.remove_value(tile_store[1])
                hit = 0
                tile_store.clear()
                capture_values.clear()

            #   in case the user gets the values correct
            elif capture_values[0] == capture_values[1]:
                messagebox.showinfo("Memory Game", message_success)
                tile_store[0].configure(state = DISABLED)
                tile_store[1].configure(state = DISABLED)
                game_over_var += 1
                hit = 0
                tile_store.clear()
                capture_values.clear()
                # following checks for the game end scenario:
                if(temp_level=='Level 1'):
                    if game_over_var == 2:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                elif(temp_level=='Level 2'):
                    if game_over_var == 4:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                elif(temp_level=='Level 3'):
                    if game_over_var == 6:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                elif(temp_level=='Level 4'):
                    if game_over_var == 8:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                elif(temp_level=='Level 5'):
                    if game_over_var == 10:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                elif(temp_level=='Level 6'):
                    if game_over_var == 12:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        messagebox.showinfo("Memory Game", "Game Over! Total time taken: " + "{:.2f}".format(elapsed_time) + " seconds")
                        mainWindow.destroy()
                else:
                    pass

            #   in case the user gets the values wrong:
            else:
                messagebox.showinfo("Memory Game", message_fail)
                GamePlay.remove_value(tile_store[0])
                GamePlay.remove_value(tile_store[1])
                hit = 0
                tile_store.clear()
                capture_values.clear()
        else:
            pass


    def remove_value(tile):
        tile.configure(text='')

# Lvl_One to Lvl_Six classes: used to set up the grid and list of values

class Lvl_One():

    value_list = [1,1,2,2]
    random.shuffle(value_list)
    # grid size is 1X4
    def lvl_1(self):
        global tile_dict

        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)


        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)


        # dictionary containing tile key and values:
        # the Button fxn passes the tile key as one of the parameters in order to allow access to the tiles
        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3
        }

class Lvl_Two():

    value_list = [1, 1, 2, 2, 3, 3, 4, 4]
    random.shuffle(value_list)
    # grid size is 2X4
    def lvl_2(self):
        global tile_dict
        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)
        tile_4 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_4, self.value_list[4], 4), height=5, width=15)
        tile_5 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_5, self.value_list[5], 5), height=5, width=15)
        tile_6 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_6, self.value_list[6], 6), height=5, width=15)
        tile_7 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_7, self.value_list[7], 7), height=5, width=15)

        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)

        tile_4.grid(row=1, column=0)
        tile_5.grid(row=1, column=1)
        tile_6.grid(row=1, column=2)
        tile_7.grid(row=1, column=3)

        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3,
            4: tile_4,
            5: tile_5,
            6: tile_6,
            7: tile_7
        }

class Lvl_Three():
    value_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(value_list)
    # grid size is 3X4
    def lvl_3(self):
        global tile_dict
        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)
        tile_4 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_4, self.value_list[4], 4), height=5, width=15)
        tile_5 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_5, self.value_list[5], 5), height=5, width=15)
        tile_6 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_6, self.value_list[6], 6), height=5, width=15)
        tile_7 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_7, self.value_list[7], 7), height=5, width=15)
        tile_8 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_8, self.value_list[8], 8), height=5, width=15)
        tile_9 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_9, self.value_list[9], 9), height=5, width=15)
        tile_10 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_10, self.value_list[10], 10), height=5, width=15)
        tile_11 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_11, self.value_list[11], 11), height=5, width=15)

        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)

        tile_4.grid(row=1, column=0)
        tile_5.grid(row=1, column=1)
        tile_6.grid(row=1, column=2)
        tile_7.grid(row=1, column=3)

        tile_8.grid(row=2, column=0)
        tile_9.grid(row=2, column=1)
        tile_10.grid(row=2, column=2)
        tile_11.grid(row=2, column=3)

        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3,
            4: tile_4,
            5: tile_5,
            6: tile_6,
            7: tile_7,
            8: tile_8,
            9: tile_9,
            10: tile_10,
            11: tile_11
        }

class Lvl_Four():

    value_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    random.shuffle(value_list)
    # grid size is 4X4
    def lvl_4(self):
        global tile_dict
        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)
        tile_4 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_4, self.value_list[4], 4), height=5, width=15)
        tile_5 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_5, self.value_list[5], 5), height=5, width=15)
        tile_6 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_6, self.value_list[6], 6), height=5, width=15)
        tile_7 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_7, self.value_list[7], 7), height=5, width=15)
        tile_8 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_8, self.value_list[8], 8), height=5, width=15)
        tile_9 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_9, self.value_list[9], 9), height=5, width=15)
        tile_10 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_10, self.value_list[10], 10), height=5, width=15)
        tile_11 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_11, self.value_list[11], 11), height=5, width=15)
        tile_12 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_12, self.value_list[12], 12), height=5, width=15)
        tile_13 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_13, self.value_list[13], 13), height=5, width=15)
        tile_14 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_14, self.value_list[14], 14), height=5, width=15)
        tile_15 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_15, self.value_list[15], 15), height=5, width=15)

        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)

        tile_4.grid(row=1, column=0)
        tile_5.grid(row=1, column=1)
        tile_6.grid(row=1, column=2)
        tile_7.grid(row=1, column=3)

        tile_8.grid(row=2, column=0)
        tile_9.grid(row=2, column=1)
        tile_10.grid(row=2, column=2)
        tile_11.grid(row=2, column=3)

        tile_12.grid(row=3, column=0)
        tile_13.grid(row=3, column=1)
        tile_14.grid(row=3, column=2)
        tile_15.grid(row=3, column=3)

        # dictionary containing tile key and values:
        # the Button fxn passes the tile key as one of the parameters in order to allow access to the tiles
        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3,
            4: tile_4,
            5: tile_5,
            6: tile_6,
            7: tile_7,
            8: tile_8,
            9: tile_9,
            10: tile_10,
            11: tile_11,
            12: tile_12,
            13: tile_13,
            14: tile_14,
            15: tile_15,
        }

class Lvl_Five():
    value_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    random.shuffle(value_list)
    # grid size is 5X4
    def lvl_5(self):
        global tile_dict
        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)
        tile_4 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_4, self.value_list[4], 4), height=5, width=15)
        tile_5 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_5, self.value_list[5], 5), height=5, width=15)
        tile_6 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_6, self.value_list[6], 6), height=5, width=15)
        tile_7 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_7, self.value_list[7], 7), height=5, width=15)
        tile_8 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_8, self.value_list[8], 8), height=5, width=15)
        tile_9 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_9, self.value_list[9], 9), height=5, width=15)
        tile_10 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_10, self.value_list[10], 10), height=5, width=15)
        tile_11 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_11, self.value_list[11], 11), height=5, width=15)
        tile_12 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_12, self.value_list[12], 12), height=5, width=15)
        tile_13 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_13, self.value_list[13], 13), height=5, width=15)
        tile_14 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_14, self.value_list[14], 14), height=5, width=15)
        tile_15 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_15, self.value_list[15], 15), height=5, width=15)
        tile_16 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_16, self.value_list[16], 16), height=5, width=15)
        tile_17 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_17, self.value_list[17], 17), height=5, width=15)
        tile_18 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_18, self.value_list[18], 18), height=5, width=15)
        tile_19 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_19, self.value_list[19], 19), height=5, width=15)

        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)

        tile_4.grid(row=1, column=0)
        tile_5.grid(row=1, column=1)
        tile_6.grid(row=1, column=2)
        tile_7.grid(row=1, column=3)

        tile_8.grid(row=2, column=0)
        tile_9.grid(row=2, column=1)
        tile_10.grid(row=2, column=2)
        tile_11.grid(row=2, column=3)

        tile_12.grid(row=3, column=0)
        tile_13.grid(row=3, column=1)
        tile_14.grid(row=3, column=2)
        tile_15.grid(row=3, column=3)

        tile_16.grid(row=4, column=0)
        tile_17.grid(row=4, column=1)
        tile_18.grid(row=4, column=2)
        tile_19.grid(row=4, column=3)

        # dictionary containing tile key and values:
        # the Button fxn passes the tile key as one of the parameters in order to allow access to the tiles
        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3,
            4: tile_4,
            5: tile_5,
            6: tile_6,
            7: tile_7,
            8: tile_8,
            9: tile_9,
            10: tile_10,
            11: tile_11,
            12: tile_12,
            13: tile_13,
            14: tile_14,
            15: tile_15,
            16: tile_16,
            17: tile_17,
            18: tile_18,
            19: tile_19
        }

class Lvl_Six():
    value_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
    random.shuffle(value_list)
    def lvl_6(self):
        global tile_dict
        tile_0 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_0, self.value_list[0], 0), height=5, width=15)
        tile_1 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_1, self.value_list[1], 1), height=5, width=15)
        tile_2 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_2, self.value_list[2], 2), height=5, width=15)
        tile_3 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_3, self.value_list[3], 3), height=5, width=15)
        tile_4 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_4, self.value_list[4], 4), height=5, width=15)
        tile_5 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_5, self.value_list[5], 5), height=5, width=15)
        tile_6 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_6, self.value_list[6], 6), height=5, width=15)
        tile_7 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_7, self.value_list[7], 7), height=5, width=15)
        tile_8 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_8, self.value_list[8], 8), height=5, width=15)
        tile_9 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_9, self.value_list[9], 9), height=5, width=15)
        tile_10 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_10, self.value_list[10], 10), height=5, width=15)
        tile_11 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_11, self.value_list[11], 11), height=5, width=15)
        tile_12 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_12, self.value_list[12], 12), height=5, width=15)
        tile_13 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_13, self.value_list[13], 13), height=5, width=15)
        tile_14 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_14, self.value_list[14], 14), height=5, width=15)
        tile_15 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_15, self.value_list[15], 15), height=5, width=15)
        tile_16 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_16, self.value_list[16], 16), height=5, width=15)
        tile_17 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_17, self.value_list[17], 17), height=5, width=15)
        tile_18 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_18, self.value_list[18], 18), height=5, width=15)
        tile_19 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_19, self.value_list[19], 19), height=5, width=15)
        tile_20 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_20, self.value_list[20], 20), height=5, width=15)
        tile_21 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_21, self.value_list[21], 21), height=5, width=15)
        tile_22 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_22, self.value_list[22], 22), height=5, width=15)
        tile_23 = Button(outer_frame, command=lambda: GamePlay.display_value(tile_23, self.value_list[23], 23), height=5, width=15)


        tile_0.grid(row=0, column=0)
        tile_1.grid(row=0, column=1)
        tile_2.grid(row=0, column=2)
        tile_3.grid(row=0, column=3)

        tile_4.grid(row=1, column=0)
        tile_5.grid(row=1, column=1)
        tile_6.grid(row=1, column=2)
        tile_7.grid(row=1, column=3)

        tile_8.grid(row=2, column=0)
        tile_9.grid(row=2, column=1)
        tile_10.grid(row=2, column=2)
        tile_11.grid(row=2, column=3)

        tile_12.grid(row=3, column=0)
        tile_13.grid(row=3, column=1)
        tile_14.grid(row=3, column=2)
        tile_15.grid(row=3, column=3)

        tile_16.grid(row=4, column=0)
        tile_17.grid(row=4, column=1)
        tile_18.grid(row=4, column=2)
        tile_19.grid(row=4, column=3)

        # making a new column, instead of a new row
        tile_20.grid(row=5, column=0)
        tile_21.grid(row=5, column=1)
        tile_22.grid(row=5, column=2)
        tile_23.grid(row=5, column=3)

        # dictionary containing tile key and values:
        # the Button fxn passes the tile key as one of the parameters in order to allow access to the tiles
        tile_dict = {
            0: tile_0,
            1: tile_1,
            2: tile_2,
            3: tile_3,
            4: tile_4,
            5: tile_5,
            6: tile_6,
            7: tile_7,
            8: tile_8,
            9: tile_9,
            10: tile_10,
            11: tile_11,
            12: tile_12,
            13: tile_13,
            14: tile_14,
            15: tile_15,
            16: tile_16,
            17: tile_17,
            18: tile_18,
            19: tile_19,
            20: tile_20,
            21: tile_21,
            22: tile_22,
            23: tile_23
        }


# start_game method receives command from the main script to start the game, depending on level selected

def start_game(event):
    global temp_level, start_time
    temp_level = levels.get()
    if(levels.get()=='Level 1'):
        start_time = time.time()
        game = Lvl_One()
        game.lvl_1()
        levels.destroy()
    elif(levels.get()=='Level 2'):
        start_time = time.time()
        game = Lvl_Two()
        game.lvl_2()
        levels.destroy()
    elif(levels.get()=='Level 3'):
        start_time = time.time()
        game = Lvl_Three()
        game.lvl_3()
        levels.destroy()
    elif(levels.get()=='Level 4'):
        start_time = time.time()
        game = Lvl_Four()
        game.lvl_4()
        levels.destroy()
    elif(levels.get()=='Level 5'):
        start_time = time.time()
        game = Lvl_Five()
        game.lvl_5()
        levels.destroy()
    elif(levels.get()=='Level 6'):
        start_time = time.time()
        game = Lvl_Six()
        game.lvl_6()
        levels.destroy()
    else:
        pass

# ----------------------- END OF CLASS/METHOD DECLARATIONS -----------------------


mainWindow = Tk()

mainWindow.title("Memory Game")
mainWindow.geometry("900x700")

# creates the green outer frame of the game window:
outer_frame = Label(mainWindow, relief="sunken", borderwidth=10, bg='green')
outer_frame.place(x=0, y=0, width=900, height=700)
messagebox.showinfo("Memory Game", "Welcome! Match tiles to earn points! Please select your level")
# sets up level selection menu:
levels = ttk.Combobox(outer_frame, value=['Level 1',
                                          'Level 2',
                                          'Level 3',
                                          'Level 4',
                                          'Level 5',
                                          'Level 6'])

levels.current(0)
levels.bind("<<ComboboxSelected>>", start_game)
levels.grid(row=0, column=0)

# Following variables are used by GamePlay.display_value - these are the variables used for the game logic

hit = 0     # this variable tracks how many times the user has selected a tile
capture_values = []     # empty list that stores the values selected by the user. Used for comparison
tile_store = []     # empty list that stores the tiles selected by the user. Resets after 2 tiles have been selected
game_over_var = 0       # if this variable reaches (2,4,6,8,10 - depending on the level), the game ends


mainWindow.mainloop()



