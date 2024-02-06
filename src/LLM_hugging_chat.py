"""Custom LLM: https://python.langchain.com/docs/modules/model_io/llms/custom_llm"""
from typing import Any, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from hugchat import hugchat
from hugchat.login import Login

class LlmHuggingChat(LLM):
    """
    This class represents a custom LLM based on the Hugging Chat API.
    Attributes:
        n (int): words to retrieve.
        sign (Login): An instance of the Login class for Hugging Face authentication.
        cookies (dict): The authentication cookies obtained from signing in.
        chatbot (ChatBot): An instance of the Hugging ChatBot class.
    """
    n: int
    hugging_face_account: str
    hugging_face_psw: str
    chatbot: Any = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the constructor of the parent class if needed
        sign = Login(self.hugging_face_account, self.hugging_face_psw)
        cookies = sign.login()
        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        chatbot=None
    ) -> str:
        """
        Make an API call to the Hugging ChatBot using the specified prompt and return the response.

        Parameters:
            prompt (str): The prompt or input text for the API call.
            stop (List[str], optional): List of stop words. Not used in this context.
            run_manager (CallbackManagerForLLMRun, optional): Callback manager for LLM run. 
                Not used in this context.

        Returns:
            str: The response from the Hugging ChatBot.
        """
        if chatbot is None:
            chatbot = self.chatbot

        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        # Return the response from the API
        result = chatbot.query(prompt)
        return str(result)

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}
    