message = 'welcome_to_python_class_!'

print(message)
print(message.replace('_', ' '))
words = message.split('_')
print(words)
print(f'there is a {len(words)} number of the words in sentences')

msg1 = input('Enter the sentence to count words :')
words = msg1.split()
print(f'There are {len(words)} number of the words in the sentences ')