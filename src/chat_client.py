from openai import OpenAI

# 跟你的 .job 裡 PORT 一致
BASE_URL = "http://localhost:8000/v1"
MODEL = "Qwen/Qwen2.5-7B-Instruct"  # 跟 .job 裡 MODEL_CHECKPOINT 一致

client = OpenAI(
    base_url=BASE_URL,
    api_key="no-key-needed",  # vLLM 會忽略，但參數必填
)

def chat():
    history = []
    print("開啟與 Qwen 的對話，輸入空行或 Ctrl+C 結束。\n")
    while True:
        try:
            user = input("You: ").strip()
            if not user:
                break
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        history.append({"role": "user", "content": user})

        resp = client.chat.completions.create(
            model=MODEL,
            messages=history,
            max_tokens=512,
            temperature=0.7,
        )
        answer = resp.choices[0].message.content
        history.append({"role": "assistant", "content": answer})
        print(f"Qwen: {answer}\n")

if __name__ == "__main__":
    chat()
