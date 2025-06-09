def get_book_text(path_to_file):
 with open(path_to_file) as f:
  bookfile = f.read()
  return bookfile

def word_count(path_to_file):
 file_contents = get_book_text(path_to_file)
 num_words = len(file_contents.split())
 return(num_words)

def char_counts(path_to_file):
 chars = {}
 bookfile = get_book_text(path_to_file).lower()
 char_list = list(bookfile)
 for c in char_list:
  if c in chars:
   chars[c] += 1
  else:
   chars[c] = 1
 return chars

def sort_char_counts(path_to_file):
 def sort_on(e):
  return e["num"]
 chars = char_counts(path_to_file)
 char_list = []
 for c in chars:
  count = chars[c]
  char_list.append({"char": c, "num": count})
 char_list.sort(reverse=True, key=sort_on)
 return char_list
