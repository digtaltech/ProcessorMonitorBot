import os
import telebot
import socket

bot = telebot.TeleBot('')

bot.send_message(201743325, "Работаю")

@bot.message_handler(commands=['start'])
def start(message):
    returned_output = 1;
    returned_output = os.system('tasklist | find "notepad.exe"')
    if (returned_output == 0):
        print("Proc true")
        bot.send_message(message.from_user.id, f"Процесс Запущен")
    else:
        bot.send_message(message.from_user.id, f"Процесс выключен нахуй")

@bot.message_handler(commands=['reload'])
def reload(message):
    pc_02 = '192.168.1.2'
    pc_03 = '192.168.1.3'
    pc_04 = '192.168.1.206'
    pc_05 = '192.168.1.5'
    pc_07 = '192.168.1.7'
    pc_08 = '192.168.1.8'
    pc_09 = '192.168.1.240'
    pc_11 = '192.168.1.11'
    pc_12 = '192.168.1.171'
    pc_13 = '192.168.1.13'
    # pc_14 = '192.168.1.14'
    # pc_18 = '192.168.1.18'

    responsefull = ""
    for var in [value for key, value in locals().items() if key.startswith('pc_')]:
        try:
            client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client1.settimeout(5.0)
            client1.connect((var, 9090))
            client1.send(str(2).encode('utf-8'))
            response = client1.recv(4096).decode('utf-8')
            if (response == 'IDLE'):
                client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client2.settimeout(5.0)
                client2.connect((var, 9090))
                client2.send(str(3).encode('utf-8'))
                responsefull += '['+ var +']  '+client2.recv(4096).decode('utf-8')+' '+'\n'
        except BaseException as err:
            print(err)
            responsefull += '['+ var +']  '+ 'Неактивен' +' '+'\n'
    bot.send_message(message.from_user.id, responsefull)

@bot.message_handler(commands=['status'])
def status(message):
    pc_02 = '192.168.1.2'
    pc_03 = '192.168.1.3'
    pc_04 = '192.168.1.206'
    pc_05 = '192.168.1.5'
    pc_07 = '192.168.1.7'
    pc_08 = '192.168.1.8'
    pc_09 = '192.168.1.240'
    pc_11 = '192.168.1.11'
    pc_12 = '192.168.1.171'
    pc_13 = '192.168.1.13'
    # pc_14 = '192.168.1.14'
    # pc_18 = '192.168.1.18'

    response = ""
    for var in [value for key, value in locals().items() if key.startswith('pc_')]:
        try:
            client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client1.settimeout(10.0)
            client1.connect((var, 9090))
            client1.send(str(1).encode('utf-8'))
            response += '['+ var +']  '+client1.recv(4096).decode('utf-8')+'  -  '
            client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client2.settimeout(5.0)
            client2.connect((var, 9090))
            client2.send(str(2).encode('utf-8'))
            response += client2.recv(4096).decode('utf-8')+'\n'
        except BaseException as err:
            response += '['+ var +']  ' + 'Неактивен' + ' ' + '\n'
            print(err)
    bot.send_message(message.from_user.id, response)

@bot.message_handler(commands=['allstop'])
def AllStop(message):
    pc_02 = '192.168.1.2'
    pc_03 = '192.168.1.3'
    pc_04 = '192.168.1.206'
    pc_05 = '192.168.1.5'
    pc_07 = '192.168.1.7'
    pc_08 = '192.168.1.8'
    pc_09 = '192.168.1.240'
    pc_11 = '192.168.1.11'
    pc_12 = '192.168.1.171'
    pc_13 = '192.168.1.13'
    # pc_14 = '192.168.1.14'
    # pc_18 = '192.168.1.18'

    response = ""
    for var in [value for key, value in locals().items() if key.startswith('pc_')]:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(10.0)
            client.connect((var, 9090))
            client.send(str(4).encode('utf-8'))
            response += '['+ var +']  '+client.recv(4096).decode('utf-8')+' '+'\n'
        except BaseException:
            response += '['+ var +']  '+ 'Неактивен' +' '+'\n'
    bot.send_message(message.from_user.id, response)

# @bot.message_handler(commands=['pc'])
# def AllStop(message):

bot.polling(none_stop=True, interval=0)
