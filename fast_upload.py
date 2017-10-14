import tkinter as tk
import requests
import pyperclip


class Text:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def get_clipboard(self):
        """
        Get the current text from clipboard
        :return:
        """
        return self.root.clipboard_get()

    def clear_clipboard(self):
        """
        Clear the clipboard
        :return:
        """
        self.root.clipboard_clear()

    def put_clipboard(self, text):
        """
        Append to the clipboard the text variable
        :param text:
        :return:
        """
        pyperclip.copy(text)
        pyperclip.paste()


class Paste:
    def __init__(self, code, lexer, expiry):
        self.host = "https://bpaste.net"
        self.code = code
        self.lexer = lexer
        self.expiry = expiry
        self.length = len(self.code)
        self.r = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; "
                          "rv:52.0) Gecko/20100101 Firefox/52.0",
            "Host": "bpaste.net",
            "Accept": "text/html,application/xhtml+xml,"
                      "application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(self.length),
            "Upgrade-Insecure-Requests": "1"
        }
        self.params = dict(
            code=self.code,
            lexer=self.lexer,
            expiry=self.expiry
        )

    def send_post(self):
        """
        Do the post to bpaste.net and return the final url
        :return:
        """
        g = self.r.post(
            self.host,
            headers=self.headers,
            data=self.params,
            stream=True
        )
        return g.url


get_clip = Text()
bpaste = Paste(
    get_clip.get_clipboard(),
    "python3",
    "1day"
)
url = bpaste.send_post()
get_clip.clear_clipboard()
get_clip.put_clipboard(url)
