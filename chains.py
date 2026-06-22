import datetime

from dotenv import load_dotenv

from schemass import AnswerQuestion, ReviseAnswer


load_dotenv()

from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,
    PydanticToolsParser
)
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model= "gpt-4-turbo")
parser = JsonOutputToolsParser(return_id=True)
parser_pydantic = PydanticToolsParser(tools=[AnswerQuestion])


actor_prompt_tempalte = ChatPromptTemplate.from_messages(
    [
        { "role": "system", "content": """
            You are expert researcher.
            Current time: {time}

            1. {first_instruction}
            2. Refelct and critique your answer. Be severe to maximize improvement.
            3.Recommend search qeuries to research information and improve the answer.
        """
         },
         MessagesPlaceholder(variable_name="messages"),
        
        
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

first_responder_prompt_template = actor_prompt_tempalte.partial(
    first_instruction = "Provide a detailed ~250 word answer"
)

first_responder = first_responder_prompt_template | llm.bind_tools(
    tools=[AnswerQuestion], tool_choice="AnswerQuestion"
)

revise_instructions = """
    Revise your previous answer using new information.
    - You should use the previous critique to add importnant information to your answer.
        -You MUST include numerical citation in your revised answer to ensure it can be verified.
        -Add a "references" section to the bottom of your answer (which does not count towards the word limit) in the form of:
            -[1] https://example.com
            -[2] https://example.com
        -You should use the previous critique to remove superfulous information from your answer and make SURE it is not more than ~250 words.
"""
revisor = actor_prompt_tempalte.partial(
    first_instruction= revise_instructions
    ) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")




if __name__ == '__main__':
    human_message = HumanMessage(
        content="Write about AI-Powered SOC / autonomous soc problem domain,"
        "list startups that do that and raised capital."
    )

    chain = (
        first_responder_prompt_template
        | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
        | parser_pydantic
    )

    res = chain.invoke(input= {"messages": [human_message]})
    print(res)
