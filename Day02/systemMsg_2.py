import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Give the answer in 2 lines. I m teaching python to a 7 years old boy"
        },
        {
            "role":"user",
            "content":"Explain python"
        }
    ]
)
print(response["message"]["content"])