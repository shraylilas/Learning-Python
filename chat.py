from ollama import chat
from prompts import SOCRATIC, ARYABHATA, ROUTER

MODEL = "llama3.2:3b"

messages = []
    
while True:
    user_input = input(f"USER: ")

    if user_input.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_input})
    
    routing = chat(
        model=MODEL,
        messages = [{"role": "system", "content": ROUTER},
                    {"role": "user", "content": user_input}
                     ]
    )
    mode_used = routing.message.content.strip()
    print(mode_used)
    if mode_used == "SOCRATIC":
         response = chat(
             model=MODEL,
             messages = [{"role": "system", "content": SOCRATIC},
                        {"role": "user", "content": user_input}
                     ]
         )

    elif mode_used == "ARYABHATA":
         response = chat(
             model=MODEL,
             messages = [{"role": "system", "content": ARYABHATA},
                        {"role": "user", "content": user_input}
                     ]                        
         )

    print(f"\nKAUTILYA: {response.message.content}")
    