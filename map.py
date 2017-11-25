import base64
import Tkinter

import urllib


def getaddress(location, width, height, zoom):   # Create a web address
    locationnospaces = urllib.quote_plus(location)
    address = "http://maps.googleapis.com/maps/api/staticmap?\
center=Roma,&zoom=13&size=400x400&key=&format=gif&sensor=false"\
.format(locationnospaces, zoom, width, height)
    return address


def getmap(location, witdh, height, zoom):   # download the map image from this address
    address = getaddress(location, witdh, height, zoom)
    urlreader = urllib.urlopen(address)
    data = urlreader.read()
    urlreader.close()
    base64data = base64.encodestring(data)
    image = Tkinter.PhotoImage(data=base64data)
    return image


def getlabelname():   # Give a marker on the map
    popup = Tkinter.Toplevel()
    popup.title("New Marker")
    label = Tkinter.Label(popup, text="Please enter a label for your marker")
    label.grid(columnspan=2)

    labelname = Tkinter.StringVar()
    textbox = Tkinter.Entry(popup, textvariable=labelname)
    textbox.pack()
    textbox.grid(column=0, row=1)

    button = Tkinter.Button(popup, text="Done", command=popup.destroy)
    button.grid(column=1, row=1)

    popup.wait_window()

    text = labelname.get()
    return text


def canvasclick(event):  # Reacting to mouse click
    x, y = event.x, event.y
    widget = event.widget
    size = 10
    widget.create_oval(x - size, y - size, x + size, y + size, width=2)
    label = getlabelname()
    widget.create_text(x, y + 2 * size, text=label)


def main():
    location = "Rome, IT"
    width = 400
    height = 400
    zoom = 13

    window = Tkinter.Tk()
    window.title("Welcome to my GitHub profile")
    window.minsize(width, height)

    mapimage = getmap(location, width, height, zoom)
    canvas = Tkinter.Canvas(window, width=width, height=height)
    canvas.create_image(0, 0, image=mapimage, anchor=Tkinter.NW)
    canvas.bind("<Button-1>, canvasclick")  # Reacting to mouse click
    canvas.pack()

    label = Tkinter.Label(window, text="hello!")
    label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
