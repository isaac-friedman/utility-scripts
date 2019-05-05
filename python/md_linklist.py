print("Welcome to the Markdown link list generator!")
filename = raw_input("What will your file be called? ")
count = int(raw_input("How many links will be in your list? "))

links = []
urls = []

for i in range(count): #Placeholders for link texts
    links.append('[]' + '[' + str(i+1) + ']  ')
    urls.append('[' + str(i+1) + ']' + ': <url here>  ')  #Placeholders for link URLS

with open('./'+ filename, 'wt') as outfile:
    outfile.write('\n'.join(str(link) for link in links))
    outfile.write('\n\n') #spacer
    outfile.write('\n'.join(str(url) for url in urls))
