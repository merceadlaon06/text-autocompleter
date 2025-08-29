'''Step 1 is putting everything in words and Basic Readme

Step 2 Add architecture (Drawings of how it should work)

Step 3 Add initial functions and Comments or Pseudocode of every function needed

Step 4 Write every code

Step 4.1 Test every function doing calls (Unit testing)

Step 5 Finish the Readme

---

'''

# Code with comments
import tkinter as tk
from english_words import get_english_words_set

web2lowerset = get_english_words_set(['web2'], lower=True)


class Node:  # Defines a small object that represents one place (one letter) in the trie
    def __init__(self):  # this function runs when we make a new Node.
        self.children = {}  # each node has a dictionary called children.
        self.is_end_of_word = False  # it becomes true when the path from the root to this node spells a complete word that we restored or path is completed.


class Trie_builder:  # defines the trie container (the whole structure)
    def __init__(self):  # runs when we make the trie
        self.root = Node()  # creates the root node. The root is the starting point. It has no letter in it.

    def insert_letter(self,
                      word):  # inserting a word creates nodes in the order: root -> first, second, third, ... and marks the ending letter as end_of_word
        current_node = self.root  # start from root

        for letter in word:  # go through each letter in the word from left to right
            if letter not in current_node.children:  # if there is no child node for this letter yet,
                current_node.children[letter] = Node()  # make a new node for that letter
            current_node = current_node.children[
                letter]  # mark the final node to show that the path contains all the letters of a word
        current_node.is_end_of_word = True  # a path for a word is completed

    def search_word(self, word):  # searches if there exists a complete path for a word
        current_node = self.root  # searching starts from the root

        for letter in word:  # checks the letters one by one
            if letter not in current_node.children:  # for each letter: if the letter's child doesn't exist, the word is not in the trie then,
                return False  # return false
            current_node = current_node.children[letter]  # if letter is found, continue checking the next letters
        return current_node.is_end_of_word  # this checks that the path existed and it was marked a complete word. For example: "hello" is a full word so it will return True. However, "hell" is in the path but not a complete word so it will return False

    def is_prefix_found(self,
                        prefix):  # tries to follow if there exist a path for a prefix. Example: 'he' will return True but 'ma' will return False because there is no word that starts with 'ma' in the list of words
        current_node = self.root  # starts checking from the root

        for letter in prefix:  # checks all letters in the prefix one by one
            if letter not in current_node.children:  # if letter is not found as a child to a parent then,
                return False  # print False
            current_node = current_node.children[letter]  # continue

        return True  # if all letters are found, print True

    def autocomplete(self, prefix):  # Will print all the words in the list that contains the prefix
        words = []  # start the list with an empty list. if the prefix can't be followed by letters all the way to the end of a word , return the empty list
        current_node = self.root  # start from the root

        for letter in prefix:  # go through all letters in the prefix form left to right
            if letter not in current_node.children:  # looks if the prefix can be followed. if not then,
                return words  # print empty list

            current_node = current_node.children[letter]  # node is now the prefix node

        def dfs(current_node, path):  # function to gather all words that start with the prefix
            if current_node.is_end_of_word:  # if current node is the end of the word, join the path (list of letters) into a string then,
                words.append(''.join(path))  # append each of the words to the list of words.
            for letter, child_node in current_node.children.items():  # for every child_node,
                dfs(child_node, path + [
                    letter])  # call _dfs to build the updated list of words. 'path' plus the next letters make up the complete word

        dfs(current_node,
            list(prefix))  # path equals to the prefix as a list of letters, so every result includes the prefix

        return words  # returns all the words that contain the prefix in a list. Example: autocomplete('he')--> ['hello', 'henry']

    def list_words(self):  # this function collects all the word in the trie
        words = []  # starting from empty list

        def dfs(current_node, path):  # same _dfs function in autocomplete function
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for letter, child_node in current_node.children.items():
                dfs(child_node, path + [letter])

        dfs(self.root, [])  # however, we start from the root with an empty path
        return words  # returns the list of all words in the trie


trie = Trie_builder()
for word in web2lowerset:
    trie.insert_letter(word)

def update_dynamic(event=None):
    text = entry.get().strip().lower()
    output_box.delete("1.0", tk.END)

    if not text:
        return

    results = trie.autocomplete(text)
    if results:
        output_box.insert(tk.END, "Autocomplete:\n" + "\n".join(results[:20]))
        if len(results) > 20:
            output_box.insert(tk.END, f"\n...and {len(results) - 20} more")
    else:
        output_box.insert(tk.END, "No matches.\n")

    if trie.search_word(text):
        output_box.insert(tk.END, f"\n\n✔ '{text}' is a valid word.")
    else:
        output_box.insert(tk.END, f"\n\n✘ '{text}' is NOT a valid word.")


def search_words():
    update_dynamic()


def validate_word():
    update_dynamic()


def clear_text():
    entry.delete(0, tk.END)
    output_box.delete("1.0", tk.END)


root = tk.Tk()
root.title("Dynamic Trie Text Autocompleter")
root.geometry("550x450")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_dynamic)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_search = tk.Button(btn_frame, text="Search", command=search_words,
                       bg="lightblue", width=12)
btn_search.grid(row=0, column=0, padx=5)

btn_validate = tk.Button(btn_frame, text="Validate Word", command=validate_word,
                         bg="lightgreen", width=12)
btn_validate.grid(row=0, column=1, padx=5)

btn_clear = tk.Button(btn_frame, text="Clear", command=clear_text,
                      bg="lightcoral", width=12)
btn_clear.grid(row=0, column=2, padx=5)

output_box = tk.Text(root, height=15, width=60, wrap="word", font=("Arial", 12))
output_box.pack(pady=10)

root.mainloop()

'''

trie.insert_letter('mike')
trie.insert_letter('henry')
trie.insert_letter('minimal')
trie.insert_letter('minimum')
trie.insert_letter('mini')

print(trie.list_words())
print(trie.is_prefix_found('ma'))
print(trie.is_prefix_found('he'))
print(trie.autocomplete('mi'))

print(trie.autocomplete('mi'))

print(trie.search_word('minimum'))
print(trie.search_word('minimal'))
print(trie.search_word('mini'))
print(trie.search_word('minim'))
'''




