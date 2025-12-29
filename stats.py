def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def total_words(filepath):
    word_count = get_book_text(filepath).split()
    return len(word_count)

def total_characters(file_contents):
    words = file_contents.split()
    a_z = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'x':0, 'y':0, 'z':0}
    for i in range(len(words)):
        words[i] = words[i].lower()
        for k in range(0,len(words[i])):
            if words[i][k] in a_z:
                a_z[words[i][k]] += 1
    return a_z
