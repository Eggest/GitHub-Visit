
from tkinter import *
from tkinter.messagebox import *
from webbrowser import open as open_tap


def gitopen():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts","a") as file:
        file.write("""\n\n\n\n#Github Hosts Start
#Update Time: 2024-01-27
#Project Address: https://github.com/maxiaof/github-hosts
#Update URL: https://raw.githubusercontent.com/maxiaof/github-hosts/master/hosts
140.82.113.26 alive.github.com
140.82.114.26 live.github.com
185.199.108.154 github.githubassets.com
140.82.113.22 central.github.com
185.199.108.133 desktop.githubusercontent.com
185.199.108.153 assets-cdn.github.com
185.199.111.133 camo.githubusercontent.com
185.199.110.133 github.map.fastly.net
146.75.121.194 github.global.ssl.fastly.net
140.82.121.3 gist.github.com
185.199.110.153 github.io
140.82.121.3 github.com
192.0.66.2 github.blog
140.82.121.6 api.github.com
185.199.110.133 raw.githubusercontent.com
185.199.109.133 user-images.githubusercontent.com
185.199.110.133 favicons.githubusercontent.com
185.199.108.133 avatars5.githubusercontent.com
185.199.108.133 avatars4.githubusercontent.com
185.199.111.133 avatars3.githubusercontent.com
185.199.109.133 avatars2.githubusercontent.com
185.199.109.133 avatars1.githubusercontent.com
185.199.110.133 avatars0.githubusercontent.com
185.199.108.133 avatars.githubusercontent.com
140.82.121.9 codeload.github.com
52.217.198.209 github-cloud.s3.amazonaws.com
3.5.28.182 github-com.s3.amazonaws.com
52.217.169.129 github-production-release-asset-2e65be.s3.amazonaws.com
3.5.7.164 github-production-user-asset-6210df.s3.amazonaws.com
52.216.162.123 github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.108.153 githubstatus.com
140.82.114.18 github.community
51.137.3.17 github.dev
140.82.112.21 collector.github.com
13.107.42.16 pipelines.actions.githubusercontent.com
185.199.110.133 media.githubusercontent.com
185.199.111.133 cloud.githubusercontent.com
185.199.108.133 objects.githubusercontent.com
#Github Hosts End""")
        file.close()
def commandd(*args):
    gitopen()
    if askyesno("完成","您的GitHub加速已完成，是否打开GitHub"):
        open_tap("https://github.com")
    quit()
tk = Tk()
tk.title("GitHub连接助手")
tk.geometry("500x500")
start = Button(tk,text="启动",command=commandd)
start.place(x = 0,y = 0,width = 500,height = 500)
mainloop()