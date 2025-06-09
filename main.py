from stats import word_count
from stats import char_counts
from stats import sort_char_counts
import sys
def main():
 # if sys.argv[1] == None:
 try:
  path_to_file = sys.argv[1]
 except Exception as e:
  print ("Usage: python3 main.py <path_to_book>")
  raise Exception(sys.exit(1))
 
 num_words = word_count(path_to_file)
 character_counts = sort_char_counts(path_to_file)

 print ("============ BOOKBOT ============")
 print (f"Analyzing book found at {path_to_file}")
 print ("----------- Word Count ----------")
 print (f"Found {num_words} total words")
 print ("--------- Character Count -------")
 for c in character_counts:
  if c["char"].isalpha():
   print (f"{c['char']}: {c['num']}")
 print ("============= END ===============")

main()