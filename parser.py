from bs4 import BeautifulSoup

def parse_chat_dialogues(html):
    soup = BeautifulSoup(html, 'html.parser')
    conversations = []

    # ChatGPT 采用 role-based 内容块，注意需根据实际页面结构调整
    messages = soup.find_all("div", class_="text-token")
    
    current_pair = {"user": "", "gpt": ""}
    is_user_turn = True

    for msg in messages:
        text = msg.get_text(strip=True)
        if not text:
            continue
        if is_user_turn:
            current_pair["user"] = text
        else:
            current_pair["gpt"] = text
            conversations.append(current_pair.copy())
            current_pair = {"user": "", "gpt": ""}
        is_user_turn = not is_user_turn

    return conversations
