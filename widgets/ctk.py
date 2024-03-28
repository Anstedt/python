import customtkinter as ctk

window = ctk.CTk()
window.title('Howard is cool')
window.geometry('640x480')

label = ctk.CTkLabel(window,
                     text = 'A label',
                     fg_color = ('blue', 'red'),
                     text_color = 'white',
                     corner_radius = 10)
label.pack()

button = ctk.CTkButton(
  window,
  text = 'Button Press It',
  fg_color = '#FF0',
  text_color = '#000',
  hover_color = '#AA0',
  command = lambda: ctk.set_appearance_mode('dark'))
button.pack()

window.mainloop()
