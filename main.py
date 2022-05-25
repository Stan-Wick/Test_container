# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as text:
        con = text.read()
        con_formatted = con.replace(',','').replace('?','').replace('.','').replace('\n','')
        #test: print(con_formatted.split().count('holding'), '\n', con_formatted)
    return con_formatted


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.split()
    word_count = {text[i]:text.count(text[i]) for i in range(0,len(text))}
    return word_count
