import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class LoginConsumer(WebsocketConsumer):

    _SIGN_IN = 'sign_in'
    _PING = 'ping'
    _GROUP_NAME = 'active_users'
    user_active = []

                            # **** Methods parents ****

    def connect(self):
        print('** Somebody connect **')
        scope = self.scope['client']
        print('scope', scope)

        # exist = self.validate_User(email)

        self.accept()

        # print('self.room_name', self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self._GROUP_NAME,
            self.channel_name
        )


    def receive(self, text_data):
        print('sent messagge', text_data)
        dic_text_data = json.loads(text_data)
        print('sent messagge', dic_text_data)
        method = dic_text_data['method']
        email = dic_text_data['email']
        # exist_user = self.validate_User(email)
        exist = self.validate_User(email)

        if method == self._SIGN_IN:
            if exist: self.clearUser(email)
            self.push_user(email)

        mensaje = {
            'type': 'validate_user',
            'data': self.user_active
        }

        self.chat_message(self.user_active)

        # Send message to room group BUT no is necessary for evit a lot request at server api full rest
        async_to_sync(self.channel_layer.group_send)(
            self._GROUP_NAME,
            {
                'type': 'chat_message', # type key correspondin to the name of method that be invoked
                'message': self.user_active
            }
        )

    def ws_disconnect(self, message):
        print('********Ciao*******')

                            # ****** Methods second *******

    def chat_message(self, event):
        json_string = json.dumps(event)
        self.send(text_data= json_string)

    def validate_User(self, email):
        exist = filter(self.def_exist, email)
        return exist

    def def_exist(self, email):
        for user in self.user_active:
            return True if email == user else False

    def clearUser(self, email):
        self.user_active.remove(email)

    def push_user(self, email):
        self.user_active.append(email)