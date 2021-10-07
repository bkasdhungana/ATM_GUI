import tkinter as tk
from tkinter import font as tkfont
from tkmacosx import Button

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.attributes('-fullscreen', True)

        label = tk.Label(self, text="Dhungana ATM", font=('Arial', 45), bg="#3d3d5c", fg="white")
        label.pack(pady=25)

        space_label = tk.Label(self, height=4,bg="#3d3d5c")
        space_label.pack()

        password_label = tk.Label(self, text='Enter your password', font=('Arial', 20), bg="#3d3d5c",fg="white")
        password_label.pack()

        password_entry_box = tk.Entry(self, text="", textvariable="pass_var", font=('Arial', 15), width=22)
        password_entry_box.pack(ipady=7)

        def check_password():
            pass

        enter_button = Button(self, text="Enter",relief='groove', borderwidth=3, width=180, height=50)
        enter_button.pack(pady=10)

        incorrect_password = tk.Label(self, text="", font=('Arial', 15, 'italic'), fg='white', bg='#33334d', anchor='n')
        incorrect_password.pack(fill='both',expand=True)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
