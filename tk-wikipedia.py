import customtkinter as ctk
from tkinter import messagebox
import wikipedia
import threading

# Ana pencereyi oluştur
window = ctk.CTk()
window.title('Wikipedia API')
window.geometry("800x600")  # Pencere boyutunu ayarla
ctk.set_appearance_mode("dark")


# Fonksiyonlar
def clear():
    my_entry.delete(0, 'end')
    my_text.delete(1.0, 'end')
    loading_label.pack_forget()  # Yükleniyor animasyonunu gizle

def search():
    loading_label.pack(pady=20)  # Yükleniyor animasyonunu göster
    window.update_idletasks()  # GUI'yi güncelle

    def search_thread():
        try:
            wikipedia.set_lang("tr")
            result = wikipedia.page(my_entry.get())
            content = result.content
        except wikipedia.exceptions.PageError:
            content = "Aradığınız sayfa bulunamadı."
        finally:
            window.after(0, lambda: display_result(content))

    threading.Thread(target=search_thread).start()

def display_result(content):
    clear()
    my_text.insert(1.0, content)
    loading_label.pack_forget()  # Yükleniyor animasyonunu gizle

# Arama çerçevesi
search_frame = ctk.CTkFrame(window)
search_frame.pack(padx=20, pady=20, fill='x')

# Arama kutusu
my_entry = ctk.CTkEntry(search_frame, placeholder_text="Wikipedia'da ara")
my_entry.pack(padx=20, pady=20, fill='x')

# Sonuç çerçevesi
text_frame = ctk.CTkFrame(window)
text_frame.pack(padx=20, pady=(0, 20), fill='both', expand=True)

# Scrollbar'lar
vertical_scroll = ctk.CTkScrollbar(text_frame, orientation='vertical')
vertical_scroll.pack(side='right', fill='y')

horizontal_scroll = ctk.CTkScrollbar(text_frame, orientation='horizontal')
horizontal_scroll.pack(side='bottom', fill='x')

# Metin alanı
my_text = ctk.CTkTextbox(text_frame, wrap='none', yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)
my_text.pack(fill='both', expand=True)

vertical_scroll.configure(command=my_text.yview)
horizontal_scroll.configure(command=my_text.xview)

# Düğme çerçevesi
button_frame = ctk.CTkFrame(window)
button_frame.pack(pady=10)

search_button = ctk.CTkButton(button_frame, text='Ara', font=("Arial", 16), command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = ctk.CTkButton(button_frame, text='Temizle', font=("Arial", 16), command=clear)
clear_button.grid(row=0, column=1, padx=20)

# Yükleniyor animasyonu
loading_label = ctk.CTkLabel(window, text="Yükleniyor...", font=("Arial", 16))

# Ana döngü
window.mainloop()
