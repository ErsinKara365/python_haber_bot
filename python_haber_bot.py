import tkinter as tk
import feedparser as fd
import webview as web

en_son_haber = [
    "https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml",
    "https://www.cnnturk.com/feed/rss/all/news",
    "https://www.ensonhaber.com/rss/ensonhaber.xml"
    ]

dunya_haber = [
    "https://www.cnnturk.com/feed/rss/dunya/news",
    "https://www.ensonhaber.com/rss/dunya.xml",
    "https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml"
    ]

saglik_haber = [
    "https://www.ensonhaber.com/rss/saglik.xml",
    "https://www.milliyet.com.tr/rss/rssnew/saglikrss.xml",
    "https://www.cnnturk.com/feed/rss/saglik/news"
    ]

ekonomi_haber = [
    "https://www.cnnturk.com/feed/rss/ekonomi/news",
    "https://www.milliyet.com.tr/rss/rssnew/ekonomirss.xml",
    "https://www.ensonhaber.com/rss/ekonomi.xml"
    ]

def buton_mavi ():
    btn_son_dakika.configure(bg="blue")
    btn_dunya.configure(bg="blue")
    btn_saglik.configure(bg="blue")
    btn_ekonomi.configure(bg="blue")

def silme_islemi ():
    for label in fr_haberler.winfo_children():
        label.destroy()
        

def open_url(event):
    web.create_window(event.widget.cget("text"),event.widget.cget("text")  )
    web.start()

def add_haberler (haberler):
    haber_sayi = 0
    for haber in haberler.entries:
        haber_sayi += 1
        if haber_sayi > 2 :
            break
        tk.Label(fr_haberler, text=haber.title, anchor="w", font=("Helveticabold", 14)).pack(side=tk.TOP, fill="x")
        lb_link=tk.Label(fr_haberler, text=haber.link, anchor="w", cursor="hand2",fg="blue", font=("Helveticabold", 14))
        lb_link.pack(side=tk.TOP, fill="x")
        lb_link.bind("<Button-1>",open_url)
        tk.Label(fr_haberler, text="-", anchor="c", bg="pink", font=("Helveticabold", 14)).pack(side=tk.TOP, fill="x")
    

def son_dakika_command ():
    buton_mavi ()
    silme_islemi()
    btn_son_dakika.configure(bg="red")
    for haber in en_son_haber :
        haberler = fd.parse(haber)
        add_haberler(haberler)

def dunya_command ():
    buton_mavi ()
    silme_islemi()
    btn_dunya.configure(bg="red")
    for haber in dunya_haber :
        haberler = fd.parse(haber)
        add_haberler(haberler)


def ekonomi_command ():
    buton_mavi ()
    silme_islemi()
    btn_ekonomi.configure(bg="red")
    for haber in ekonomi_haber :
        haberler = fd.parse(haber)
        add_haberler(haberler)

def saglik_command ():
    buton_mavi ()
    silme_islemi()
    btn_saglik.configure(bg="red")
    for haber in saglik_haber :
        haberler = fd.parse(haber)
        add_haberler(haberler)




window = tk.Tk()
window.geometry("1500x500+0+550")
window.title("Haber Basliklari")


fr_haberler = tk.Frame(window, height=500)
fr_haberler.grid(row=0, column=1, sticky="nsew")

fr_buttons = tk.Frame(window, relief=tk.RAISED, bg="pink", bd=2)
fr_buttons.grid(row=0, column=0, sticky="ns")

btn_son_dakika = tk.Button(fr_buttons, text="Son Dakika" ,font=("Helveticabold", 14), bg="blue", command= son_dakika_command)
btn_son_dakika.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_dunya = tk.Button(fr_buttons, text="Dünya", font=("Helveticabold", 14), bg="blue", command= dunya_command)
btn_dunya.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

btn_ekonomi = tk.Button(fr_buttons, text="Ekonomi", font=("Helveticabold", 14), bg="blue", command= ekonomi_command)
btn_ekonomi.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

btn_saglik = tk.Button(fr_buttons, text="Saglik", font=("Helveticabold", 14), bg="blue", command= saglik_command)
btn_saglik.grid(row=3, column=0, sticky="ew", padx=5, pady=5)





window.mainloop()
