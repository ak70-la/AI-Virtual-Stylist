from ast import Import
from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo
import openai # type: ignore




openai.api_key ="your openai api key" # type: ignore


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://arafatlala786:OmIzJdpvli0a0qbn@cluster0.vbhan.mongodb.net/chatgpt"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({}) 
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("main.html",myChats = myChats)

@app.route("/api", methods=["GET","POST"])    
def qa():
    if request.method=="POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question":question,"answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create( # type: ignore
                    model ="gpt-4o",
                    prompt=question,
                    temprature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
            print(response)
            data = {"question":question, "answer": response ["choices"] [0] ["text"]}
            mongo.db.chats.insert_one({"question": question, "answer": response ["choices"] [0] ["text"]})
            return jsonify(data)
                  
        
        

app.run(debug=True,port=5001)   