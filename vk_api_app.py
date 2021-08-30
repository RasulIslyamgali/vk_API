import vk_api
# import your token and user_id
from config import token, user_id
# for happy print
from colorama import init, Fore
# for choose random id(not user_id) during send message
from random import randint


def get_user_status(session, user_id):
    """func for get vk user status with id"""
    status = session.method('status.get', {'user_id': user_id})
    print('Ваш статус успешно поменялся на:', status['text'])


def set_user_status(vk, text):
    """set new user status"""
    vk.status.set(text=text)


def get_friends_status(session, user_id, *args, **kwargs):
    """func for get status all user friends"""
    fields = ['nickname']
    friends = session.method('friends.get', {"user_id": user_id, 'fields': fields})
    friends_list = friends['items']

    for friend in friends_list:
        status = session.method('status.get', {'user_id': int(friend['id'])})
        my_friend = friend
        # print(my_friend['first_name'], my_friend['last_name'], 'Статус:', status['text'])
        if status['text']:
            print(Fore.GREEN + my_friend['first_name'], my_friend['last_name'])
            print(Fore.GREEN + 'Статус вк:', Fore.BLUE + status['text'])
            print()
        else:
            print(Fore.GREEN + my_friend['first_name'], my_friend['last_name'])
            print(Fore.RED + 'Скрытный человек(нет статуса)')
            print()


def get_message_history_with_user(session, user_id, *args, **kwargs):
    """func for get message history with some user
    ideas for modernization:
    -- set specific color for users
    -- get time from unix time
    """

    messages = session.method('messages.getHistory', {'user_id': user_id,
                                                      'start_message_id': 1,
                                                      'offset': -100,
                                                      'count': 100
                                                      })['items']
    print(messages)
    for message in messages:
        print(message['text'])


def send_message(session, *args, **kwargs):
    """func for send message with chat_id"""
    random_id = randint(1, 1000000)
    message = input('Введите текст сообщения:\n')
    message = session.method('messages.send', {'peer_ids': kwargs['user_id'],
                                               'message': message,
                                               'random_id': random_id})
    print(message)


if __name__ == '__main__':
    # init colorama
    init()
    # you can use class VkApi
    session = vk_api.VkApi(token=token)
    # or you can use method get_api()
    vk = session.get_api()
    # text = input('Введите новый статус:\n')
    # set_user_status(vk, text)
    # get_user_status(session, user_id)
    # get_friends_status(session, user_id)
    # get_message_history_with_user(session, some_user_id)
    send_message(session, user_id=some_user_id)
