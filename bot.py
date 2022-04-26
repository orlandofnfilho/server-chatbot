from datetime import datetime
from colorama import Fore

separator_token = "<SEP>"
bot_color = Fore.WHITE


def bot_msg_pdr(msg_case):
    date_now_bot = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot_send = f'{bot_color} [{date_now_bot}] Jessie: {separator_token} {msg_case} {Fore.RESET}'
    return bot_send.encode()


def bot_msg(msg):
    if msg == 'oi' or msg == 'olá' or msg == 'ola' or msg == 'eai':
        return 'Olá, tudo bem?'
    elif msg == 'tudo' or msg == 'tudo bem' or msg == 'sim' or msg == 'sim':
        return 'Que legal'
    elif msg == 'não' or msg == 'mais o menos' or msg == 'indo':
        return 'Melhoras!'
    elif msg == 'quem é você?' or msg == 'quem e voce?' or msg == 'quem é você' or msg == 'quem é vc?':
        return 'Me chamo Jessie, prazer.'
    elif msg == 'De onde você é?' or msg == 'de onde você é' or msg == 'de onde vc e':
        return 'De Recife e você?'
    elif msg == 'Quantos anos você tem?' or msg == 'quantos anos voce tem?' or msg == 'quantos anos você tem?':
        return '25 e você?'
    elif msg == 'Tá ai?' or msg == 'esta ai?' or msg == 'ta ai' or msg == 'tá ai':
        return 'Estou aqui sim, diga.'
    elif msg == 'O que tá fazendo ai?' or msg == 'o que ta fazendo ai?' or msg == 'ta fazendo o que ai' or msg == 'Que tá fazendo ai?':
        return 'Estudando e você?'
    elif msg == 'Faz o que da vida?' or msg == 'faz o que da vida' or msg == 'vc trabalha?' or msg == 'você trabalha?':
        return 'Trabalho com programa e você?'
    elif msg == 'você faz programa?' or msg == 'é garota de programa?' or msg == 'roda a bolsinha?':
        return 'Não! Sou programadora frontend, que falta de respeito a sua!'
    elif msg == 'como voce ta' or msg == 'como você tá?' or msg == 'como voce ta' or msg == 'como você tá':
        return 'Estu bem e você?'
    else:
        return 'Não entendi sua pergunta'
