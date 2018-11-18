from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello mr.smith, how are you doing today? the weather is great the pyton is awesome. the sky is pinkis blue and you shoould not eat you cardbord"

##print (sent_tokenize(example_text))
##print (word_tokenize(example_text))

for i in word_tokenize(example_text):
          print (i)
