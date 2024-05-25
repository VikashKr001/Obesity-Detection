from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd
#import requests
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

def Train():
    """GUI"""
    

    root = tk.Tk()

    root.geometry("1700x1550")
    root.title("Comparison of Clustering Methods for Obesity Classification")
    root.configure(background="#152238")
    ID = tk.IntVar()
    Age = tk.IntVar()
    Gender= tk.IntVar()
    Height= tk.IntVar()
    Weight= tk.IntVar()
    BMI = tk.IntVar()
    
   
   
    
    #===================================================================================================================
    
    
    def Detect():
        
        
        e1=ID.get()
        print(e1)
        e2=Age.get()
        print(e2)
        e3= Gender.get()
        print(e3)
        e4= Height.get()
        print(e4)
        e5=Weight.get()
        print(e5)
        e6=BMI.get()
        print(e6)
        
        #########################################################################################
        
        from joblib import dump ,load
        a1=load(r'SVM_wt.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5,e6]])
        print(v)
        
        # try:
        #     if v[0] == 0:
        #         print("PCOS Not Detected")
        #         yes = tk.Label(root, text="PCOS Not Detected", background="green", foreground="white",
        #                        font=('times', 20, 'bold'), width=20)
        #         yes.place(x=630, y=650)
        #     elif v[0] == 1:
        #         print("PCOS Detected")
        #         no = tk.Label(root, text="PCOS Detected", background="brown", foreground="white",
        #                       font=('times', 20, 'bold'), width=20)
        #         no.place(x=630, y=650)
        # except:
        #     print("Invalid input values")
        #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white",
        #                        font=('times', 20, 'bold'), width=20)
        #     invalid.place(x=630, y=650)
    
        
        if v[0]==0:
            print("Low_Under_weight Detected \n Combine a balanced diet with regular physical activity")
            yes = tk.Label(root,text="Low_Underweight Detected \n Combine a balanced diet with regular physical activity",background="green",foreground="white",font=('times', 20, ' bold '),width=70)
            yes.place(x=100,y=520)
                     
        elif v[0]==1:
            print("Medium_Normal_weight Detected \n Focus on a diet rich meal,\n Don't skip meals, Minimize processed foods and sugary drinks,")
            no = tk.Label(root, text="Medium_Normal_weight Detected \n Focus on a diet rich meal,\n Don't skip meals, Minimize processed foods and sugary drinks,", background="brown", foreground="white",font=('times', 20, ' bold '),width=70)
            no.place(x=10,y=520)
            
        elif v[0]==2:
            print("High_Over_weight Detected,\n Emphasize whole, nutrient-dense foods such as fruits, vegetables, lean proteins, whole grains, and healthy fats.\n Plan meals and snacks to avoid impulsive eating,  Emphasize whole, nutrient-dense foods such as fruits, vegetables, lean proteins, whole grains, and healthy fats.\n Combine a balanced diet with regular physical activity, Stay hydrated by drinking plenty of water")
            no = tk.Label(root, text="High_Over_weight Detected \n Nutrient-dense foods such as fruits, vegetables, lean proteins, whole grains, and healthy fats,\n Plan meals and snacks to avoid impulsive eating, \n Combine a balanced diet with regular physical activity, Stay hydrated by drinking plenty of water", background="brown", foreground="white",font=('times', 20, ' bold '),width=90)
            no.place(x=10,y=520)
        
        elif v[0]==3:
            print("Very_High_Obese_weight Detected, \n Minimize processed and fast foods, \n Try to eat regular, balanced meals to avoid extreme hunger, \n Drink plenty of water throughout the day, \n Combine a healthy diet with regular physical activity")
            no = tk.Label(root, text="Very_High_Obese_weight Detected, \n Minimize processed and fast foods, \n Try to eat regular, balanced meals to avoid extreme hunger, \n Drink plenty of water throughout the day, \n Combine a healthy diet with regular physical activity", background="brown", foreground="white",font=('times', 20, ' bold '),width=70)
            no.place(x=100,y=520)
            
    
            
        # except:
        #     print("Invalid input values")
        #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white", font=('times', 20, 'bold'), width=20)
        #     invalid.place(x=630, y=650)    
              
    
       
            
        
            
            
    l1=tk.Label(root,text="ID",background="olive",font=('times', 20, ' bold '),width=20)
    l1.place(x=400,y=50)
    ID=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=ID)
    ID.place(x=800,y=50)

    l2=tk.Label(root,text="Age",background="olive",font=('times', 20, ' bold '),width=20)
    l2.place(x=400,y=100)
    Age=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar= Age)
    Age.place(x=800,y=100)
    
    l3=tk.Label(root,text="Gender",background="olive",font=('times', 20, ' bold '),width=20)
    l3.place(x=400,y=150)
    Gender=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Gender)
    Gender.place(x=800,y=160)
    
    l4=tk.Label(root,text="Height",background="olive",font=('times', 20, ' bold '),width=20)
    l4.place(x=400,y=200)
    Height=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Height)
    Height.place(x=800,y=200)
    
    l5=tk.Label(root,text="Weight",background="olive",font=('times', 20, ' bold '),width=20)
    l5.place(x=400,y=250)
    Weight=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Weight)
    Weight.place(x=800,y=250)
  
    l6=tk.Label(root,text="BMI",background="olive",font=('times', 20, ' bold '),width=20)
    l6.place(x=400,y=300)
    BMI=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=BMI)
    BMI.place(x=800,y=300)
    
    
    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=660,y=400)


    root.mainloop()

Train()