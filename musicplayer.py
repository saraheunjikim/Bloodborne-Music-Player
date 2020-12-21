"""
This is a music player that plays the soundtracks from Bloodborne.
"""
from tkinter import *
import time, sys
from pygame import mixer

mixer.init()

track_names = ['lady maria', 'cleric beast']
current_track = (0, '')


def press(word):
    global track_names
    global current_track
    word = button_text.get()
    if word == 'PLAY':
        update_button_text('PLAY')
        track_index, track_name = current_track
        if track_index >= len(track_names):
            track_index = 0

        # Play the current track
        name = track_names[track_index]
        current_track = (track_index, name)
        mixer.music.set_volume(100)
        mixer.music.load(f'C:/Users/Muffin/Desktop/python/projects/etc/{name}.mp3')
        mixer.music.play()

        window_2.delete(0, 'end')
        window_2.configure(state='normal')
        window_2.insert('end', name)

    if word == 'PAUSE':
        update_button_text('PAUSE')
        mixer.music.pause()

        time.sleep(5)

    if word == 'STOP':
        mixer.music.stop()
        time.sleep(5)

    if word == 'NEXT':
        pass

    if word == 'PREVIOUS':
        pass


def checkPlaying(main_window):
    global track_names
    global current_track

    result = False

    if mixer.music.get_busy() == True:
        result = True
    else:
        # Playing has finished
        # TODO: Change button states, whatever
        print("Sound finished, playing next")
        track_index, track_name = current_track
        current_track = (track_index + 1, '')
        press('PLAY')
        result = False

    main_window.after(250, checkPlaying, main_window)

    return result

def update_button_text(word):
    if word == 'PLAY':
        button_text.set('PAUSE')
    elif word == 'PAUSE':
        button_text.set('PLAY')


if __name__ == '__main__':
    # create application window
    app = Tk()

    # title
    app.title("Music Players")

    # geometry
    app.geometry('383x121')

    # background color
    app.configure(bg='orange')

    equation = StringVar()
    window_1 = Label(app, textvariable=equation)
    window_1.grid(columnspan=4, ipadx=100, ipady=10)
    equation.set('Bloodborne Music Player')

    window_2 = Entry(app, width=30)
    window_2.grid(columnspan=4, ipadx=100, ipady=10)
    window_2.configure(state='disabled')

    window_2.grid_columnconfigure((0, 1, 2), uniform="equal", weight=1)

    # Create buttons
    button_text = StringVar()
    button_text.set("PLAY")
    button1 = Button(app, textvariable=button_text, fg='yellow', bg='purple',
                     command=lambda: press(button_text), height=2, width=1)
    button1.grid(row=2, column=0, sticky="NSEW")

    button2 = Button(app, text='STOP', fg='yellow', bg='purple',
                     command=lambda: press('STOP'), height=2, width=1)
    button2.grid(row=2, column=1, sticky="NSEW")

    button3 = Button(app, text='NEXT', fg='yellow', bg='purple',
                     command=lambda: press('NEXT'), height=2, width=1)
    button3.grid(row=2, column=2, sticky="NSEW")

    button4 = Button(app, text='PREVIOUS', fg='yellow', bg='purple',
                     command=lambda: press('PREVIOUS'), height=2, width=1)
    button4.grid(row=2, column=3, sticky="NSEW")

    # Start the Music Playing Check
    app.after(1000, checkPlaying, app)

# start the GUI
app.mainloop()
