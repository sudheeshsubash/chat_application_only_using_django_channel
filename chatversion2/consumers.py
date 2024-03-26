 # chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from chat.models import ChatMessages


class ChatConsumer(WebsocketConsumer):
    
    def one_query_object_to_json(self, queryobject):
        return {
            'message': queryobject.content,
            'user': queryobject.author.username,
            'time':str(queryobject.timestamp),
        }
    
    
    def multiple_query_object_to_json(self, queryobjects):
        content = []
        for queryobject in queryobjects:
            content.append(self.one_query_object_to_json(queryobject))
        return content
    
    
    def fetch_history_messages(self):
        history_messages = ChatMessages.last_10_messages()
        history_messages_jsonformat = self.multiple_query_object_to_json(history_messages)
        self.send_history_fetched_messages(history_messages_jsonformat)
    
    
    def user_table_object_get(self, username):
        return User.objects.filter(username=username).first()


    def save_message_to_chatmessages_database(self, message, user):
        chatmessages_object = ChatMessages.objects.create(
            author = self.user_table_object_get(user),
            content = message
        )
        content = self.one_query_object_to_json(chatmessages_object)
        self.send_message(content)

    
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        self.fetch_history_messages()
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        self.save_message_to_chatmessages_database(message, user)
        
        
    def send_message(self,content):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message", 
                "method":'chat_message',
                "message": content.get('message'),
                'user': content.get('user'),
                "time": content.get('timestamp'),
            }
        )
        
    
    def send_history_fetched_messages(self, history_messages):
        '''
        hisoty chat message fetch and send in order
        '''
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message", 
                "method": "fetch_history_messages",
                "messages": history_messages
            }
        )
        
        

    # Receive message from room group
    def chat_message(self, event):
        
        if event["method"] == 'chat_message':
            self.send(text_data=json.dumps({
                "message": event["message"],
                'user': event["user"],
                "time":event["time"],
                "method":'chat_message',
            }))
        elif event["method"] == 'fetch_history_messages':
            self.send(text_data=json.dumps({
                "method":'fetch_history_messages',
                "messages": event["messages"],
            }))
        