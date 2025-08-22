import os
import eel
import requests

from engine.features import *
# from engine.command import *
# from engine.auth import recoganize


import ollama

# Load your cybersecurity dataset
with open("data/cybersecurity.txt", "r", encoding="utf-8") as f:
    cybersecurity_data = f.read()

def start():

    eel.init("www")
    print("")

    playAssistantSound()
    # @eel.expose
    # def init():
        # subprocess.call([r'device.bat'])
        # eel.hideLoader()
        # speak("Ready for Face Authentication")
        # flag = recoganize.AuthenticateFace()
        # if flag == 1:
            # eel.hideFaceAuth()
            # speak("Face Authentication Successful")
            # eel.hideFaceAuthSuccess()
            # speak("Hello, Welcome Sir, How can i Help You")
            # eel.hideStart()
            # playAssistantSound()
        # else:
            # speak("Face Authentication Fail")
    # os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    # eel.init("www")

    @eel.expose
    def ask_bot(user_query):
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": f"You are a cybersecurity assistant. Use this knowledge:\n{cybersecurity_data}"},
                {"role": "user", "content": user_query}
            ]
        )
        return response["message"]["content"]

    eel.start('index.html', mode=None)

if __name__ == "__main__":
    start()


# from langchain.chains import RetrievalQA
# from langchain_community.llms import Ollama

# def get_rag_chain(vectorstore):
    # llm = Ollama(model="llama3")  # Replaceable with llama3.1, llama3.2, etc.
    # retriever = vectorstore.as_retriever()
    # chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    # return chain

    