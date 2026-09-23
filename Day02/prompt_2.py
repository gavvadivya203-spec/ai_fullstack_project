import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"define Ai and Name only 3 types of Ai only"
        }
    ]
)
print(response["message"]["content"])