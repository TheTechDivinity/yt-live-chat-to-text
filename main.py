# Creating the Generator
from chat_downloader import ChatDownloader
from random import randint
from datetime import datetime

# Title and Intro
print('''
    YouTube Live Chat to Text File
    by: Divinity
    
    This project reads YouTube live stream messages and stores them in 2
    .txt files inside "outputs/name-message/" or "outputs/message-only/"
    The first contains all the messages, and the latter contains all the
    messages and the author's names.
    FORMAT: <author>:   <message> or <message> (Oldest to Latest)
    
    -Credits to:
    Chat Downloader: https://github.com/xenova/chat-downloader
    Codeium: https://www.codeium.com/
    
    
''')

# Getting the livestream URL
url = input('   Enter the YouTube URL: ')
print('')  # Blank line for readability

chat = ChatDownloader().get_chat(url)  # Create a generator

# Creating the text file named with the URL and a random number of 6 digits
# to avoid overwriting other files

# Removes the start of the url (https://www.youtube.com/watch?v=)
url = url.replace('https://www.youtube.com/watch?v=', '')

# Makes the file name the url (without illegal characters) with a '+' and a random number of 6 digits
output_name = url + '+' + str(randint(-999999, 999999)) + '.txt'

# Output file with the author's name, and the message
name_message_output = 'outputs/name-message/name-message+' + output_name
# Output file with only the message
message_only_output = 'outputs/message-only/message-only+' + output_name

print(' Messages: \n')  # For readability

# Prints the locations of the output files
print(' Name & Message Output File: ' + name_message_output)
print(' Message Only Output File: ' + message_only_output)


# Converts the timestamp from an int to a formatted string (d/m/Y, H:M:S)
def convert_timestamp(timestamp):
    date_time = datetime.fromtimestamp(float(timestamp))
    return date_time


# Turns an unformatted message dictionary to a formatted string
# Format:  Author's name: Message or just Message
def format_message(message_dictionary, add_name):
    formatted_message_string = message_dictionary['message']  # Message

# If we want to add the author's name to the message add it
    if add_name:
        author = message_dictionary['author']  # Get the author of the message
        formatted_message_string = author['name'] + ':   ' + formatted_message_string  # Author's Name

    # Returns the formatted message as a string
    return formatted_message_string


# Writing the messages into the text file
for message in chat:  # Iterate over messages
    chat.print_formatted(message)  # Prints the formatted message

    # Writes the message in the text files of each format type and adds a new line for each
    with open(message_only_output, 'a', encoding="utf-8") as output:
        output.write(format_message(message, False) + '\n')

    with open(name_message_output, 'a', encoding="utf-8") as output:
        output.write(format_message(message, True) + '\n')
