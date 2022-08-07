# UNIcompiler
# MP3 music Player
# Task-3

from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
photo = PhotoImage(file=r"dic.png")
photo1 = PhotoImage(file=r"dic1.png")
photo2 = PhotoImage(file=r"dic2.png")
photo3 = PhotoImage(file=r"dic3.png")


class MusicPlayer:

    def __init__(self, window):
        window.geometry('465x412')
        window.title('UNICompiler mp3 music player')
        window.configure(bg="plum")
        window.resizable(0, 0)

        p1 = PhotoImage(file='download.png')
        window.iconphoto(False, p1)

        frame = LabelFrame(window, text='MP3 Music Player', bg='#00e6e6', font=('Ubuntu', 40, 'bold', 'underline'))
        frame.pack(expand=True, fill=BOTH)

        Load = Button(window, text='Load', image=photo, command=self.load, bg='#00ace6')
        Load.place(x=180, y=300)

        Play = Button(window, text='Play', image=photo1, command=self.play, bg='#00ace6')
        Play.place(x=180, y=150)

        Pause = Button(window, text='Pause', image=photo3, command=self.pause, bg='#00ace6')
        Pause.place(x=50, y=150)

        Stop = Button(window, text='Stop', image=photo2, command=self.stop, bg='#00ace6')
        Stop.place(x=310, y=150)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


app = MusicPlayer(root)
root.mainloop()
