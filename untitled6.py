from tkinter import *
import requests
import json

root = Tk()
root.title("Very Fancy Code Thiny")
root.geometry("500x500")
root.config(bg="lavender")

capcitallabel = Label(root, text="Capital City Name", font=("times new roman", 25, "bold"), bg="lavender")
capcitallabel.place(relx=0.5,rely=0.03, anchor=CENTER)

enter = Entry(root)
enter.place(relx=0.5,rely=0.1,anchor=CENTER)

countryname = Label(root,text="Country Name:",font=("times new roman", 17),bg="lavender",wraplength=500,justify=CENTER,fg="indigo")
countryname.place(relx=0.5,rely=0.3,anchor=CENTER)

regionname = Label(root,text="Region:",font=("times new roman", 17),bg="lavender",wraplength=500,justify=CENTER,fg="indigo")
regionname.place(relx=0.5,rely=0.35,anchor=CENTER)

lanname = Label(root,text="Language:",font=("times new roman", 17),bg="lavender",wraplength=500,justify=CENTER,fg="indigo")
lanname.place(relx=0.5,rely=0.4,anchor=CENTER)

pop = Label(root,text="Population:",font=("times new roman", 17),bg="lavender",wraplength=500,justify=CENTER,fg="indigo")
pop.place(relx=0.5,rely=0.45,anchor=CENTER)

area = Label(root,text="Area:",font=("times new roman", 17),bg="lavender",wraplength=500,justify=CENTER,fg="indigo")
area.place(relx=0.5,rely=0.5,anchor=CENTER)

def city_details():
    api_output_json=""
    api_request = requests.get("https://restcountries.com/v2/capital/" + enter.get())
    api_output_json = json.loads(api_request.content)
    
    name=api_output_json[0]['name']
    region=api_output_json[0]['region']
    language=api_output_json[0]['languages'][0]['name']
    population=api_output_json[0]['population']
    areaa=api_output_json[0]['area']
    
    countryname['text']="Country Name: "+name
    regionname['text']="Region: "+region
    lanname['text']="Language: "+language
    pop['text']="Population: "+str(population)
    area['text']="Area: "+str(areaa)

btn = Button(root, text="City Details", height=2, command=city_details)
btn.place(relx=0.5,rely=0.2,anchor=CENTER)

root.mainloop()