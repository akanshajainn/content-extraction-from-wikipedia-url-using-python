import wikipedia
import nltk
#wikipedia.set_lang('en')
#page = wikipedia.page('Wikipedia')
#print(page.content)

url='https://en.wikipedia.org/wiki/Sachin_Tendulkar'
title=url.split("/")[-1]
wiki_obj= wikipedia.page(title)
text=wiki_obj.content

#All text content from the page
print(text)

#To display all NER tags from the wikipedia's page content.
for sent in nltk.sent_tokenize(text):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(' '.join(c[0] for c in chunk),':',chunk.label())
