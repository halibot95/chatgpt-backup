from playwright.sync_api import sync_playwright

class ChatGPTBrowser:
    def __init__(self, headless=True):
        self.url = "https://chat.openai.com/chat"
        self.headless = headless

    def fetch_chat_html(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            context = browser.new_context(storage_state="auth.json")  # 自动登录保存
            page = context.new_page()
            page.goto(self.url)

            print("🔒 如果首次运行，请登录 ChatGPT 后按回车继续抓取：")
            input()

            page.wait_for_selector('div[class*="text-token"]', timeout=60000)
            html = page.content()

            context.storage_state(path="auth.json")  # 保存登录状态
            browser.close()
            return html
