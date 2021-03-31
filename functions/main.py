import tkinter as tk
import pygubu
from functions import displayData, getData, getGameMode, gameModeStatsDict


class Application():
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('../gui/group4.ui')
        self.toplevel2 = builder.get_object('toplevel2', master)

        builder.connect_callbacks(self)

        callbacks = {
            'button1_clicked': self.button1_clicked,
            'button2_clicked': self.button2_clicked
        }

        builder.connect_callbacks(callbacks)

        guivars = ('enteredPlayer', 'button1', 'textEntry1',
                   'button2', 'textBox1')

        builder.import_variables(self, guivars)

        self.textBox1 = builder.get_object('statsDisplay')

    def button1_clicked(self):
        allPlayerData = getData.getData(self.enteredPlayer.get())
        selectedGame = getGameMode.getGameMode()

        displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

    def button2_clicked(self):
        self.enteredPlayer.set('')
        self.textBox1.delete('1.0', tk.END)
        self.textBox1.insert(tk.END, "Kills:\nDeaths:\nWins:\nKD Ratio:")

    def on_quit_button_click(self):
        self.master.quit()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.withdraw()
    root.mainloop()
