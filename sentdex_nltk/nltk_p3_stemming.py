#stemming
#we are going to stemming = finding the root of the woords, especially paragramg
# verbs especially, like riding has a root of rid. we dont need the -ing. 
# i was taking a ride in the car
# iwas riding in a car.
#meaning exact same

#nltk has stemming algoth
##for w in example_words:
##     print (ps.stem(w))

# the print goes "python", but there words "pythonli" probably because change meaning . bust ok

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]



new_text = "it is very important to be pythonly while you are pythoning with python. all pythoners have pythoned poorly at least once." 
words = word_tokenize(new_text)

for w in words:
     print (ps.stem(w))
