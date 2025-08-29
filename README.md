# 🔠 Python Trie Implementation

A **Python implementation of a Trie (prefix tree)** data structure.  
This project demonstrates how to efficiently store and search words with operations such as **insert_letter, search_word, prefix checking, autocomplete, and listing all words**.

---

## 📖 What is a Trie?
A **Trie** (pronounced *"try"*) is a tree-like data structure used to efficiently store and retrieve strings, especially when dealing with prefixes.  
Common use cases include:
- Autocomplete (e.g., typing "go" suggests "good", "google")  
- Spell checking  
- Dictionary word lookups  
- IP routing (longest prefix matching)  

---

## ✨ Features
- ✅ Insert words into the Trie  
- 🔎 Search for complete words  
- 🔤 Check if a prefix exists  
- 💡 Autocomplete suggestions based on a prefix  
- 📃 List all stored words in the Trie  

---

## 🛠️ Requirements
This project does not require external dependencies.  
You only need:

```
Python >= 3.7
```

---

## 📂 Project Structure
```
python-trie/
│── README.md          # Project documentation + code
```

---

## ▶️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-trie.git
   cd python-trie
   ```

2. **Run the script**
   ```bash
   python README.md
   ```

---
## 🧪 List of Words inserted in the Trie
```
    ['hello','henry', 'mike', 'minimal', 'minimum', 'mini']
```

---
## 🧪 Example Output
```
['hello', 'mike', 'henry', 'minimal', 'minimum', 'mini']            → Result of trie.list_words(). Shows all words stored in the trie after inserting them.
False                                                               → Result of trie.is_prefix_found('ma'). No word starts with "ma".
True                                                                → Result of trie.is_prefix_found('he'). There are words starting with "he" (hello, henry).
['mike', 'minimal', 'minimum', 'mini']                              → Result of trie.autocomplete('mi'). All words that start with "mi".
True                                                                → Result of trie.search_word('minimum'). "minimum" exists in the trie.
True                                                                → Result of trie.search_word('mini'). "mini" still exists as a complete word.
False                                                               → Result of trie.search_word('minim'). "minim" is only a prefix, not a full word.
```

---

## 📌 Notes
- This implementation is designed to be **educational and beginner-friendly**, with detailed inline comments explaining every method.  
- It can be extended to handle:
  - Large dictionaries
  - Predictive text input
  - Autocomplete search engines
  - Spell checkers  