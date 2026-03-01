#word frequency counter
import string
choice=input('Type 1 to paste text OR 2 to use a file: ')
if choice=='1':
    text=input('Enter your paragraph: ')
elif choice=='2':
    filename=input('Enter your filename(example-sample.txt): ')
#to open and read the file as a file and close after reading    
    with open(filename,'r')as file:
        text=file.read()
else:
    print('Invalid input')
#remove punctuation
text=text.translate(str.maketrans('','',string.punctuation))
#convert to lowercase and split into words
words=text.lower().split()
#create empty dictionary
word_count={}
#count words
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
#print result
print('\nWord Frequency:\n')
for word, count in word_count.items():
    print(word,':',count)
 
