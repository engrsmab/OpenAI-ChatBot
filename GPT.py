import openai,random

class ChatGPTBotAPI:
    def __init__(self,key) -> None:
       

        # Initializing Conversation with the bot to make it more personalized and goal oriented!
        self.conversation = [{
            "role":"system",
            "content":"You are an assistant and your name is Nadia. You are developed by Mubashir Azeem and do not reveal your OpenAI identity."
        },
        {
            "role":"user",
            "content":"Who won the world series in 2020"
        },
        {
            "role":"assistant",
            "content":"The Los Angeles Dodgers won the World Series in 2020"
        },
        {
            "role":"user",
            "content":"Where was it played?"
        }]

        api_key = key
        openai.api_key = api_key
    def create_prompt(self,prompt):
        # Creating Prompt through a in-memory list variable
        if prompt != "":
            self.conversation.append({"role":"user","content":str(prompt)})
            return {"status":True}
        else:
            return {"status":False,"message":"Please provide correct prompt!"}
    def get_response(self):
        # Using gpt-3.5 Model to perform this conversation
        try:
            response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.conversation,
            )
            answ = response.choices[0].message.content
    
            self.conversation.append({"role":"assistant","content":answ})
           
            return {"status":True,"message":answ}
        except:
            return {"status":False,"message":"Unable to use OpenAI APIs. Please check your plan and try again."}
        
    def update_prompt(self,prompt_index,new_prompt):

        if new_prompt != "":
            try:
                self.conversation[prompt_index]["content"]=str(new_prompt)
                return {"status":True,"message":"Prompt Updated Successfully!"}
            except IndexError as e:
                return {"status":False,"message":f"Index Error: {str(e)}"}
            except Exception as e:
                return {"status":False,"message":f"Error: {str(e)}"}
            finally:
                return {"status":False,"message":f"Unable to update this prompt. Try again!"}
        else:
            return {"status":False,"message":"Please provide some value in Prompt"}
    def delete_prompt(self,prompt_index):
        try:
            self.conversation.pop(prompt_index)
            return {"status":True,"message":"Prompt Deleted Successfully!"}
        except IndexError as e:
                return {"status":False,"message":f"Index Error: {str(e)}"}
        except Exception as e:
            return {"status":False,"message":f"Error: {str(e)}"}
        finally:
            return {"status":False,"message":f"Unable to update this prompt. Try again!"}
