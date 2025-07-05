import datetime

def write_markdown(dialogues, filepath, tags=None):
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tags_str = "、".join(tags) if tags else ""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# ChatGPT 对话归档｜{today}\n")
        if tags:
            f.write(f"\n**标签**：{tags_str}\n\n")

        for i, d in enumerate(dialogues, 1):
            f.write(f"## 🗂️ 对话 {i}\n\n")
            f.write(f"**🧑 你：**\n{d['user']}\n\n")
            f.write(f"**🤖 GPT：**\n{d['gpt']}\n\n")
            f.write("---\n\n")
