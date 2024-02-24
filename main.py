from flask import Flask

from GPT import ChatGPTBotAPI
app = Flask(__name__)

# Please Replace key variable with valid Paid Key of OpenAI to test this code. 
# I do have a Paid API, if you require for test purposes, i can provide.
bot = ChatGPTBotAPI(key="xyz")

@app.route("/")
def index():
    return "Welcome! I am Nadia!"

@app.route('/create_prompt/<prompt>',methods=["GET"])
def create(prompt):
    resp = bot.create_prompt(prompt)
    if resp["status"]:
        return {"status":True,"message":"Prompt Created"}
    else:
        return resp
@app.route('/get_response',methods=["GET"])
def response_func():
    resp = bot.get_response()


@app.route('/update_prompt/prompt_index=<index>&new_prompt=<new>',methods=["GET"])
def update_prompt(index,new):
    return bot.update_prompt(prompt_index=index,new_prompt=new)

@app.route('/delete_prompt/prompt_index=<index>',methods=["GET"])
def del_prompt(index):
    return bot.delete_prompt(prompt_index=index)
    
   

   

if __name__ == '__main__':
    app.run()
