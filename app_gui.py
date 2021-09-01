import tkinter as tk
from tkinter import *
from chatbot_main import start_chat, bot_name

BG_COLOR = "white"
FONT = "calibri"
TEXT_COLOR = "#303331"

class ChatApp:

    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chappie AI bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=400, height=480, bg=BG_COLOR)

        self.text_widget =Text(self.window, width=20, height=2, fg=TEXT_COLOR, bg=BG_COLOR, font=FONT,
                                padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Putting scrollbar in the chat area.
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=1)
        scrollbar.configure(command=self.text_widget.yview, bg="#B2AFAE")

        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.79)

        # message_text_box.
        self.msg_entry =Entry(bottom_label, bg="#B2AFAE", fg=TEXT_COLOR, font=FONT, borderwidth=0)
        self.msg_entry.place(relwidth=0.80, relheight=0.06, relx=0.008, rely=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # enter_button.
        button = Button(bottom_label, text="Send", font=FONT, bg=BG_COLOR, fg="#323DC7", borderwidth=0,
                        command= lambda: self._on_enter_pressed(None))
        button.place(relx= 0.80, rely= 0.011, relheight= 0.06, relwidth=0.20)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "YOU")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        
        msg1 = f"{msg}:{sender}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.tag_configure("right", justify='right')
        self.text_widget.insert(END, msg1, "right")
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}:{start_chat(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.tag_configure("left", justify='left')
        self.text_widget.insert(END, msg2, "left")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__=="__main__":
    app = ChatApp()
    app.run()

