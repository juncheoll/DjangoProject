import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("order_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_add("order_group", self.channel_name)


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        order_info = text_data_json['order_info']

        # 주문 정보를 처리하는 코드 작성
        print('Received order:', order_info)
        
        # 연결된 모든 클라이언트에게 주문 정보 전송
        await self.send_order_to_group(order_info)
        
    async def send_order_to_group(self, order_info):
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            "order_group",
            {
                "type": "order.message",
                "message": order_info
            }
        )
    async def order_message(self, event):
        message = event['message']

        # 주문 정보 메시지를 클라이언트에게 전송
        await self.send(text_data=json.dumps({
            'message': message
        }))