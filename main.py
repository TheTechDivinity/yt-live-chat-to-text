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

output_file_name = url.replace('https://www.youtube.com/watch?v=', '') + '+' + str(randint(-999999, 999999)) + '.txt'

name_message_output_file = 'outputs/name-message/name-message+' + output_file_name
message_only_output_file = 'outputs/message-only/message-only+' + output_file_name

print(' Name & Message Output File: ' + name_message_output_file)
print(' Message Only Output File: ' + message_only_output_file)


def format_message(message_dictionary, add_name):  # FORMAT: <author>:   <message>
    formatted_message_string = message_dictionary['message']

    if add_name:
        author = message_dictionary['author']
        formatted_message_string = author['name'] + ':   ' + formatted_message_string
    return formatted_message_string


print(' Messages: \n')
for message in chat:
    chat.print_formatted(message)

    with open(message_only_output, 'a', encoding="utf-8") as messages_only_file:
        messages_only_file.write(format_message(message, False) + '\n')

    with open(name_message_output, 'a', encoding="utf-8") as names_and_messages_file:
        names_and_messages_file.write(format_message(message, True) + '\n')
