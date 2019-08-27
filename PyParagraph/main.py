import re

nsentences = 0
totnwords = 0
nletters = 0

with open('raw_data/paragraph_2.txt', 'r',encoding='utf-8') as file:
    for line in file:
        line = line.replace('“','')
        line = line.replace('”','')
#        line = line.replace('\'s',' ')
        sentences = re.split('[.\n?]', line)
        for sentence in sentences:
            words = re.split('[-–\',()<>1234567890\" ]', sentence)
            nword = 0
            for word in words:
                if len(word) > 0:
                    nword += 1
                    nletters += len(word)
#                    print (f"{word} {len(word)}")
            if nword > 0:
                totnwords += nword
                nsentences += 1

results = []
results.append("Paragraph Analysis\n-----------------")
results.append(f"Approximate Word Count: {totnwords}")
results.append(f"Approximate Sentence Count: {nsentences}")
results.append(f"Average Letter Count: {round(nletters/totnwords,1)}")
results.append(f"Average Sentence Length: {round(totnwords/nsentences,1)}")

filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
