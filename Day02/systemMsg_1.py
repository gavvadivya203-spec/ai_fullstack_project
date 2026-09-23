import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Exlain cyber security in 2 lines"
        },
        {
            "role":"user",
            "content":"Explain ai"
        }
    ]
)
print(response["message"]["content"])