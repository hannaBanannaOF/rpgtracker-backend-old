import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class SessionsConsumer(WebsocketConsumer):
    def connect(self):
        self.userPK = self.scope['url_route']['kwargs']['userPK']
        self.room_group_name = 'sessions_%s' % self.userPK

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['ation']
        session_id = text_data_json['session_id']
        session_name = text_data_json['session_name']
        header = text_data_json['header']
        link = text_data_json['link']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'open_close_session',
                'action': action,
                'session_id' : session_id,
                'session_name' : session_name,
                'header' : header,
                'link' : link
            }
        )

    # Receive message from room group
    def open_close_session(self, event):
        action = event['action']
        session_id = event['session_id']
        session_name = event['session_name']
        header = event['header']
        link = event['link']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'action': action,
            'session_id' : session_id,
            'session_name' : session_name,
            'header' : header,
            'link' : link
        }))