import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer

class LoginConsumer(WebsocketConsumer):

    _SIGN_IN = 'sign_in'
    _PING = 'ping'
    _GROUP_NAME = 'active_users'
    user_active = []

                            # **** Methods parents ****

    def connect(self):
        print('** Somebody connect **')
        scope = self.scope['client']
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self._GROUP_NAME,
            self.channel_name
        )

    def receive(self, text_data):
        print('sent messagge', text_data)
        dic_text_data = json.loads(text_data)
        method = dic_text_data['method']
        email = dic_text_data['email']

        exist_user = self.validate_User(email)        
        if exist_user:
            print('exist', exist_user['channel_name'])

        if method == self._SIGN_IN:
            self.clearUser(email, exist_user['channel_name']) if exist_user else self.push_user(email, self.channel_name)
    
        print('********', self.user_active)
        self.send_message_group('message group')
        

    def ws_disconnect(self, channel_name):
        print('********Ciao*******', channel_name)
        self.senf_message_channel('ciao', channel_name)
        async_to_sync(self.channel_layer.group_discard)( self._GROUP_NAME, channel_name)

                            # ****** Methods seconds *******

    def senf_message_channel(self, message, channel_name):
        print('enviar', channel_name)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(
            channel_name,{
            'type': 'send_message', # type key correspondin to the name of method that be invoked
            'text': message
        })

    def send_message_group(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self._GROUP_NAME,
            {
                'type': 'send_message', # type key correspondin to the name of method that be invoked
                'message': message
            }
        )
    
    def send_message(self, message):
        message_send = self.chat_message(message)
        print('pepepe', message_send)
        self.send(text_data=message_send)

    def chat_message(self, event):
        json_string = json.dumps(event)
        return json_string

    def validate_User(self, email):
        # exist = filter(self.def_exist, self.user_active)
        # return list(exist)
        for user in self.user_active:
            if email == user['email']: 
                print('USER: ',user)
                return user 
        return []

    def clearUser(self, email, channel_name):
        print('*_*', channel_name)
        self.ws_disconnect(channel_name)
        try:
            self.user_active.remove(email)
        except ValueError:
            pass

    def push_user(self, email, channel_name):
        print('Add client', email)
        user = {
            'email': email,
            'channel_name': channel_name
        }
        self.user_active.append(user)