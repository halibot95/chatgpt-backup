import os
import datetime
import yaml
from browser import ChatGPTBrowser
from parser import parse_chat_dialogues
from markdown_writer import write_markdown

def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    output_path = config.get("output_path", "./output")
    os.makedirs(output_path, exist_ok=True)

    browser = ChatGPTBrowser(headless=config.get("headless", False))
    html_content = browser.fetch_chat_html()

    dialogues = parse_chat_dialogues(html_content)

    today = datetime.date.today().strftime("%Y-%m-%d")
    filepath = os.path.join(output_path, f"{today}.md")

    write_markdown(dialogues, filepath, tags=config.get("tags", []))
    print(f"\n✅ 已写入 Markdown 文件：{filepath}")

if __name__ == "__main__":
    main()
