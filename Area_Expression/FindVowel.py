#Write a program to find a vowel letter

letter = input('Enter a letter here: ')
to_lower_letter = letter.lower()

if to_lower_letter == 'a' or to_lower_letter == 'e' or to_lower_letter == 'i' or to_lower_letter == 'o' or to_lower_letter == 'u':
    print('Entered letter is Vowel')
else:
    print('Entered letter is Consonant')

