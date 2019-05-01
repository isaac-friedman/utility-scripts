print("Welcome to the Markdown link list generator!")
filename = raw_input("What will your file be called? ")
count = int(raw_input("How many links will be in your list? "))

with open('./'+ filename, 'wt') as outfile:
    for i in range(count): #Placeholders for link texts
        outfile.write('[]' + '[' + str(i+1) + ']\n')
    outfile.write('\n\n') #spacer
    for i in range(count):
        outfile.write('[' + str(i+1) + ']' + ':[]\n')  #Placeholders for link URLS
