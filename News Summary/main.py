import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

#nltk.download('punkt')

def summarize():

            url = utext.get('1.0', "end").strip()
            article = Article(url)

            article.download()
            article.parse()

            article.nlp()

            # print(f'Title: {article.title}')
            # print(f'Authors: {article.authors}')
            # print(f'Publication Date: {article.publish_date}')
            # print(f'Summary: {article.summary}')

            title.config(state='normal')
            author.config(state='normal')
            publications.config(state='normal')
            summary.config(state='normal')
            sentiment.config(state='normal')

            title.delete('1.0', 'end')
            title.insert('1.0', article.title)

            author.delete('1.0', 'end')
            author.insert('1.0', article.authors)

            publications.delete('1.0', 'end')
            publications.insert('1.0', article.publish_date)

            summary.delete('1.0', 'end')
            summary.insert('1.0', article.summary)

            analysis = TextBlob(article.text)
            sentiment.delete('1.0', "end")
            sentiment.insert('1.0', f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "netural"}')

            title.config(state='disabled')
            author.config(state='disabled')
            publications.config(state='disabled')
            summary.config(state='disabled')
            sentiment.config(state='disabled')



root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publications")
plabel.pack()

publications = tk.Text(root, height=1, width=140)
publications.config(state='disabled', bg='#dddddd')
publications.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()

