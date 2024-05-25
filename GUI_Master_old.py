from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import warnings
import joblib
from joblib import dump
import pickle
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Comparison of Obesity Classification")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('B1.jpg')

image = image.resize((w, h))

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

image = Image.open('a5.png')

image = image.resize((1000,750))

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=30, y=80)






# function to change to next image
# function to change to next image
'''def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img3)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()'''




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Comparison of Obesity Classification", font=('times', 35,' bold '), height=1, width=62,bg="#560319",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv("C:/Users/user/Desktop/Obesity Classification 100%  code upd/Obesity Classification 100%  code upd/Obesity Classification 100%  code/Train.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as SVM_wt.joblib",width=45,height=2,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    X = data.drop('Class', axis=1)  # Adjust the column name according to your dataset
    y = data['Class']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the SVM model
    svm_model = SVC()
    svm_model.fit(X_train_scaled, y_train)
    from joblib import dump
    dump (svcclassifier,"SVM_wt.joblib")
    print("Model saved as SVM_wt.joblib")
    svm_model = joblib.load("SVM_wt.joblib")
    # Save the SVM model to a pickle file
    with open("SVM_wt.pkl", "wb") as file:
        pickle.dump(svm_model, file)
    with open("scaler.pkl", "wb") as file:
        pickle.dump(scaler, file)




def DT():
    data = pd.read_csv("C:/Users/user/Desktop/Obesity Classification 100%  code upd/Obesity Classification 100%  code upd/Obesity Classification 100%  code/Train.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=2)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier(criterion='entropy', random_state=0)  
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    # print("Confusion Matrix :")
    # cm = confusion_matrix(y_test,y_pred)
    # print(cm)
    # print("\n")
    # from mlxtend.plotting import plot_confusion_matrix

    # fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    # plt.xlabel('Predictions', fontsize=18)
    # plt.ylabel('Actuals', fontsize=18)
    # plt.title('Confusion Matrix', fontsize=18)
    # plt.show()


 
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as DT_wt.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (svcclassifier,"DT_wt.joblib")
    print("Model saved as DT_wt.joblib")

def RF():
    data = pd.read_csv("C:/Users/user/Desktop/Obesity Classification 100%  code upd/Obesity Classification 100%  code upd/Obesity Classification 100%  code/Train.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    # from sklearn.model_selection import train_test_split
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=12)

    # # from sklearn.svm import SVC
    # # svcclassifier = SVC(kernel='linear')
    # # svcclassifier.fit(x_train, y_train)
    
    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    
    from sklearn.ensemble import RandomForestClassifier  
    svcclassifier =RandomForestClassifier(n_estimators= 10, criterion="entropy") 
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
     
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as RF_wt.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (svcclassifier,"RF_wt.joblib")
    print("Model saved as RF_wt.joblib")
    
   


def NB():
    data = pd.read_csv("C:/Users/user/Desktop/Obesity Classification 100%  code upd/Obesity Classification 100%  code upd/Obesity Classification 100%  code/Train.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape


 
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    from sklearn.naive_bayes import GaussianNB
    naive_bayes_classifier = GaussianNB()
    naive_bayes_classifier.fit(x_train, y_train)

    y_pred = naive_bayes_classifier.predict(x_test)
    print(y_pred)

    print("Confusion Matrix :")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('Confusion Matrix.png', bbox_inches='tight')
    plt.show()
    

    print("=" * 40)
    print("==========")
    print("Classification Report : ", (classification_report(y_test, y_pred)))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as NB_wt.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (naive_bayes_classifier,"NB_wt.joblib")
    print("Model saved as NB_wt.joblib")
    
def call_file():
    from subprocess import call
    call(['python','Check.py'])
    #import Check.py
    #Check.py()


def window1():
    from subprocess import call
    call(['python','Graphs.py'])
    

def window():
    from subprocess import call
    call(['python','GUI_Master.py'])
def window1():
    from subprocess import call
    call(['python','Next.py'])

framed = tk.LabelFrame(root, text=" --Result-- ", width=300, height=580, bd=5, font=('times', 14, ' bold '),bg="gray",fg="white")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=1010, y=80)

framed1 = tk.LabelFrame(root, text=" -", width=300, height=100, bd=5, font=('times', 14, ' bold '),bg="black",fg="white")
framed1.grid(row=0, column=0, sticky='nw')
framed1.place(x=1010, y=650)

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root,foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="SVM", command=Model_Training, width=15, height=2)
button3.place(x=1050, y=130)

button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="DT", command=DT, width=15, height=2)
button4.place(x=1050, y=230)

button5 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="RF", command=RF, width=15, height=2)
button5.place(x=1050, y=330)
exit = tk.Button(root, text="NB", command=NB, width=15, height=2, font=('times', 15, ' bold '),bg="#560319",fg="white")
exit.place(x=1050, y=430)

# exit1 = tk.Button(root, text="Prediction", command=call_file, width=15, height=2, font=('times', 15, ' bold '),bg="gray",fg="black")
# exit1.place(x=500, y=630)

# exit2 = tk.Button(root, text="Visualization", command=window1, width=15, height=2, font=('times', 15, ' bold '),bg="gray",fg="black")
# exit2.place(x=700, y=630)

# exit2 = tk.Button(root, text="Detection", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="gray",fg="black")
# exit2.place(x=900, y=630)

exit3 = tk.Button(root, text="Next", command=window1, width=15, height=2, font=('times', 15, ' bold '),bg="Red",fg="black")
exit3.place(x=1070, y=580)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''