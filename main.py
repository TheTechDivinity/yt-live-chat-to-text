from chat_downloader import ChatDownloader
from random import randint
from datetime import datetime

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

url = input('   Enter the YouTube URL: ')
print('')
chat = ChatDownloader().get_chat(url)

output_file_name = input('   Enter the name of the output file: ')

if output_file_name == '':
    output_file_name = url.replace('https://www.youtube.com/watch?v=', '') + '+' + str(randint(-999999, 999999))

names_and_messages_path = input('   Enter the path to the names and messages file: ')
if names_and_messages_path == '':
    names_and_messages_output_file = 'outputs/name-message/name-message+' + output_file_name + '.txt'
else:
    names_and_messages_output_file = names_and_messages_path + '/name-message+' + output_file_name + '.txt'

message_only_path = input('   Enter the path to the message only file: ')
if message_only_path == '':
    message_only_output_file = 'outputs/message-only/message-only+' + output_file_name + '.txt'
else:
    message_only_output_file = message_only_path + '/message-only+' + output_file_name + '.txt'

print('')
print(' Name & Message Output File: ' + names_and_messages_output_file)
print(' Message Only Output File: ' + message_only_output_file)


def format_message(message_dictionary, add_name):  # FORMAT: <author>:   <message> or <message>
    formatted_message_string = message_dictionary['message']

    if add_name:
        author = message_dictionary['author']
        formatted_message_string = author['name'] + ':   ' + formatted_message_string
    return formatted_message_string


# Note CMD only supports ASCII characters, so it'll display non-ASCII characters as "?"
print('\n Messages:')
for message in chat:
    chat.print_formatted(message)

    with open(message_only_output_file, 'a', encoding="utf-8") as messages_only_file:
        messages_only_file.write(format_message(message, False) + '\n')

    with open(names_and_messages_output_file, 'a', encoding="utf-8") as names_and_messages_file:
        names_and_messages_file.write(format_message(message, True) + '\n')
