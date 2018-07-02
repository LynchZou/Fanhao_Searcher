from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from spider import *
import random
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


"""
Process GUI window
"""
def ProcessGUI():

    url = ""

    # Evaluate Entry
    def evaluate(event):

        url = entry.get()

        try:
            data = getHTML(url)
        except ValueError:
            messagebox.showinfo("Failed", "请输入合法的url")
        else:
            try:
                print(getImage2(data))
            except urllib.error.HTTPError:
                messagebox.showinfo("Warning", "检测到Http Error")
            finally:
                messagebox.showinfo("Success", "图片已保存至当前文件夹")


    # random search
    def rand_search(event):

        # select url
        myurl = selectURL()
        # select regular expression
        regex = selectRegex(myurl)

        try:
            data = getHTML(myurl)
        except ValueError:
            messagebox.showerror("Failed", "获取url失败")
        else:
            try:
                print(getImage2(data, regex=regex))
            except urllib.error.HTTPError:
                messagebox.showwarning("Warning", "检测到Http Error")
            except UnicodeEncodeError:
                messagebox.showwarning("Warning", "ASCII codec cannot encode characters")
            finally:
                messagebox.showinfo("Success", "图片已保存至当前文件夹")


    # deep search
    def deep_search(event):

        # declare max images to download
        MAX_SEARCHED_PAGE = 5
        MAX_PASSED_PAGE = 100
        searched_page = 0
        passed_page = 0

        urlList = []
        imagelist = []

        # get and push root url
        url = entry.get()
        urlList.append(url)

        while len(urlList) != 0 and searched_page <= MAX_SEARCHED_PAGE and passed_page <= MAX_PASSED_PAGE:

            # randomly select url to parse
            last_item = random.choice(urlList)

            # if len(urlList) == 1:
            #     last_item = urlList.pop(0)
            # else:
            #     last_item = urlList.pop(1)

            # last_item = urlList.pop()
            print(last_item)

            print(passed_page)

            try:
                data = getHTML(last_item)
            except ValueError:
                answer = messagebox.askokcancel("Failed", "检测到不合法url，是否继续运行")
                if not answer:
                    break
            else:
                try:
                    # process obtained urls
                    hyperlink = getURL(data)
                    for item in hyperlink:
                        urlList.append(item)
                    # process data given by this iteration
                    imagelist = getImage2(data)
                except urllib.error.HTTPError:
                    messagebox.showwarning("Warning", "检测到Http Error")
                except UnicodeEncodeError:
                    pass
                finally:
                    if len(imagelist) != 0:
                        searched_page += 1
            finally:
                passed_page += 1
                pass

        messagebox.showinfo("Success", "图片已保存至当前文件夹")


    # initialize window
    root = Tk()
    root.title("番号搜索器")
    root.geometry("490x520")

    # frame
    frame = Frame(root)

    # greeting
    LabelGreeting = Label(frame, text="欢迎使用番号搜索器", fg="red")
    LabelGreeting.grid(row=0, column=1)

    # present image
    filex = resource_path("kato_megumi.gif")
    img_gif = PhotoImage(file=filex)
    img_gif = img_gif.subsample(x=4, y=4)
    label_img = Label(frame, image=img_gif)
    label_img.grid(row=1, column=1, padx=10)

    # entry
    Label(frame, text="请输入您想要搜索的网站:").grid(row=2, column=1, sticky=W, padx=60, pady=20)
    entry = Entry(frame)
    entry.grid(row=2, column=1, sticky=E, padx=60, pady=10)

    # search button
    ButSearch = Button(frame, text="网址搜索", width=15)
    ButSearch.bind("<Button-1>", evaluate)
    ButSearch.grid(row=3, column=1, sticky=W, padx=40)

    # deep search button
    DeepSearch = Button(frame, text="深度搜索", width=15)
    DeepSearch.bind("<Button-1>", deep_search)
    DeepSearch.grid(row=3, column=1, sticky=E, padx=40)

    # random search button
    RandomSearch = Button(frame, text="随机搜索", width=15)
    RandomSearch.bind("<Button-1>", rand_search)
    RandomSearch.grid(row=4, column=1, sticky=W, padx=40)

    # quit button
    ButQuit = Button(frame, text="退出", width=15, command=root.quit)
    ButQuit.grid(row=4, column=1, sticky=E, padx=40)


    # maker's info
    Label(frame, text="制作者：jk研究所所长\nQQ:1403892781", fg="blue").grid(row=5, column=1, pady=40)

    frame.grid()

    root.mainloop()



"""
main() function only for test
"""
def main():
    # current_path = os.path.dirname(__file__)
    # parent_path = os.path.dirname(current_path)
    # path = parent_path + "/ConvetedImages/"
    ProcessGUI()

if __name__ == "__main__":
    main()