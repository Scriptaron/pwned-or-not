from customtkinter import (
    CTk,
    CTkButton,
    CTkCheckBox,
    CTkEntry,
    CTkFrame,
    CTkImage,
    CTkLabel,
    CTkToplevel,
    set_appearance_mode,
)
from PIL import Image
from pwned import Pwned

img = CTkImage(Image.open('.\\docs\\icon\\cmd.png'), size=(50, 50))

root = CTk()
root.geometry('450x200')
root.title('Pwned or not?')
set_appearance_mode('dark')
root.resizable(width=False, height=False)


def click_submit():
    pw = Pwned(entry.get())
    if pw.isPwned():
        create_popup(
            'Password found '
            + str(pw.get_leaked_password())
            + ' times in the dataset.\n Recommended to change it ASAP!', '#FD0000'
        )
    else:
        create_popup(
            'Your password was not found in the dataset. \nYou have a safe password!', '#3ce800'
        )


def create_popup(warning, color):
    popup = CTkToplevel()
    popup.geometry('400x125')
    popup.title('Status')
    popup.resizable(width=False, height=False)

    popup_label = CTkLabel(popup, font=('Roboto', 18), text=warning, text_color=color)
    popup_label.pack(pady=10)

    popup_button = CTkButton(
        popup,
        text='Ok',
        fg_color='#303134',
        hover_color='#207c01',
        font=('System', 20),
        command=popup.destroy,
    )
    popup_button.pack(pady=10)


def show_password():
    if entry.cget('show') == '*':
        entry.configure(show='')
    else:
        entry.configure(show='*')


label = CTkLabel(root, text='Enter your password:', font=('System', 30))
label.pack(pady=10)

top_frame = CTkFrame(root, fg_color='transparent')
top_frame.pack(side='top', fill='x')

mid_frame = CTkFrame(root, fg_color='transparent')
mid_frame.pack(side='top', fill='x')

frame1 = CTkFrame(top_frame, fg_color='transparent')
frame1.pack()

frame2 = CTkFrame(mid_frame, fg_color='transparent')
frame2.pack(side='right')

img_label = CTkLabel(frame1, image=img, text='')
img_label.pack(side='left')

entry = CTkEntry(
    frame1,
    font=('System', 25),
    width=260,
    show='*',
    fg_color='transparent',
    border_color='#3ce800',
)
entry.pack(side='right')

checkbox = CTkCheckBox(
    frame2,
    text='',
    command=show_password,
    hover_color='#800000',
    fg_color='#207c01',
)
checkbox.pack(side='right')

label_check = CTkLabel(frame2, text='Show', font=('System', 10))
label_check.pack(side='left', padx=10)

button = CTkButton(
    root,
    text='Submit',
    font=('System', 20),
    fg_color='#303134',
    hover_color='#207c01',
    command=click_submit,
)
button.pack(pady=20)

root.mainloop()
