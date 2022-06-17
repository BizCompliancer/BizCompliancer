from typing import List, Dict, TypeVar, Optional
import logging

# PythonCore Module
from PythonCore.ChatBot.Chatbot_vertices.chatbot_vertex import ChatBotVertex
from PythonCore.ChatBot.response_options import ResponseOptions

VertexType = TypeVar('VertexType', bound='Vertex')
ResponseOptionsType = TypeVar("ResponseOptionsType", bound=ResponseOptions)

class Adhaar(ChatBotVertex):
    def __init__(self, label: str, bot_message: str, response_options: List[ResponseOptionsType], orchestrator_obj):
        super().__init__(label, bot_message, response_options, orchestrator_obj)


    def action(self, next_vertex_label: Optional[str] = None, msg: Optional[str] = None, sender_name: Optional[str] = None, msg_id: Optional[int] = None) -> Optional[str]:
        split_msg_list: List[str] = msg.split(" ")
        adhaar: str = split_msg_list[1]

        return adhaar

    def send_bot_response(self, bot_response: str) -> None:
        # Getting instance of telegram_chat_bot_utils
        telegram_chat_bot_utils = self.orchestrator_object.telegram_chat_bot_utils
        msg_str: str = ""

        telegram_chat_bot_utils.send_message(self.orchestrator_object.group_chat_id, msg_str)


    def __call__(self) -> VertexType:
        logging.debug(f"vertex {self.get_label()} called")

        # Showing message first and asking for response
        self.send_bot_message()

        # Getting user response
        contained_strings_dict = {"Adhaar": "PAN-3"}
        next_vertex_label, msg, sender_name, msg_id = self.get_user_response(contained_strings_dict)

        # processing message and fetching useful data from it
        processed_msg = self.action(next_vertex_label, msg, sender_name, msg_id)

        # Responding response
        self.send_bot_response(processed_msg)

        # Saving data in cache and returning next_vertex
        next_vertex = self.transfer(next_vertex_label, msg_id, msg, processed_msg)
        return next_vertex



