from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:

    def __init__(self):
        self.dbo = Database()
        self.apo = API()
        self.root = Tk()
        self.root.title("NLP Application")
        self.root.iconbitmap("/Users/aryansaxena/Desktop/Project/resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg= "#34495E")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white" )
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))
        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=60)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter your password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=60,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)
         
        login_but = Button(self.root,text="Log in",width=30,height=2,command=self.perform_login)
        login_but.pack(pady=(10,10))
         
        label3 = Label(self.root,text="Not a member?")
        label3.pack(pady=(10,10))
        register_but = Button(self.root,text="Register Now!",command=self.register_gui)
        register_but.pack(pady=(10,10))
    
    def register_gui(self):
        self.clear()
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white" )
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))
        label0 = Label(self.root,text="Enter Name")
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=60)
        self.name_input.pack(pady=(5,10),ipady=4)
        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=60)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter your password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=60,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)
         
        register_but = Button(self.root,text="Register",width=30,height=2,command=self.perform_registration)
        register_but.pack(pady=(10,10))
         
        label3 = Label(self.root,text="Already a member?")
        label3.pack(pady=(10,10))
        register_but = Button(self.root,text="Login Now!",command=self.login_gui)
        register_but.pack(pady=(10,10))
        
    def clear(self):
        for i in self.root.pack_slaves():
         i.destroy()
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response= self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success!","Registration is done. Welcome aboard")
        else:
            messagebox.showerror("Error!","This email already exists.")
    
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        
        if response:
            messagebox.showinfo("Welcome back!","You are now logged in")
            self.home_gui()
        else:
            messagebox.showerror("No email found","Please register yourself first")

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text="NLP App",bg="black",fg="white" )
        heading.pack(pady=(40,40))

        sentiment_but = Button(self.root,text="Sentiment Analysis",command=self.sentiment_gui)
        sentiment_but.pack(pady=(10,20))

        NER_but = Button(self.root,text="Named Entity Recognition")
        NER_but.pack(pady=(10,20))

        Emotion_but = Button(self.root,text="Emotion Recognisition")
        Emotion_but.pack(pady=(10,20))

        goback_but= Button(self.root, text = "Go Back",command=self.login_gui)
        goback_but.pack(pady=(10,20))
    
    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white" )
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))

        heading = Label(self.root,text="Sentiment Anaylysis",bg="#34495E",fg="white" )
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))

        label1 = Label(self.root,text="Enter Text")
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root,width=60)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        sentiment_but = Button(self.root,text="Analyize the text",command=self.do_sentiment_analysis)
        sentiment_but.pack(pady=(10,20))

        self.sentiment_result = Label(self.root,text="",fg="white",bg="#34495E")
        self.sentiment_result.pack(pady=(10,10), ipady=4)
        self.sentiment_result.configure(font=("verdana",15))

        meow_but = Button(self.root,text="Go Back",command=self.home_gui)
        meow_but.pack(pady=(10,10))
    
    def do_sentiment_analysis(self):
     text = self.sentiment_input.get()
     result = self.apo.sentiment_analysis(text)  # Call to your API
     
     # Assuming result format is [{'id': '1', 'predictions': [{'prediction': 'negative', 'probability': 0.99889}]}]
     if result and isinstance(result, list) and 'predictions' in result[0]:
         predictions = result[0]['predictions']
         txt = ''
         for pred in predictions:
             prediction = pred['prediction']
             probability = pred['probability']
             txt += f"{prediction} -> {probability:.5f}\n"
         self.sentiment_result['text'] = txt
     else:
         self.sentiment_result['text'] = "No valid predictions found."
     
     print(self.sentiment_result['text']) 
    


        

         
        
nlp = NLPApp()
