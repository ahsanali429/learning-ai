import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the importance of LLM",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)


# chat_completion = client.chat.completions.create(
#     #
#     # Required parameters
#     #
#     messages=[
#         # Set an optional system message. This sets the behavior of the
#         # assistant and can be used to provide specific instructions for
#         # how it should behave throughout the conversation.
#         {
#             "role": "system",
#             "content": "you are a helpful assistant."
#         },
#         # Set a user message for the assistant to respond to.
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],

#     # The language model which will generate the completion.
#     model="llama3-8b-8192",

#     #
#     # Optional parameters
#     #

#     # Controls randomness: lowering results in less random completions.
#     # As the temperature approaches zero, the model will become deterministic
#     # and repetitive.
#     temperature=0.5,

#     # The maximum number of tokens to generate. Requests can use up to
#     # 32,768 tokens shared between prompt and completion.
#     max_tokens=1024,

#     # Controls diversity via nucleus sampling: 0.5 means half of all
#     # likelihood-weighted options are considered.
#     top_p=1,

#     # A stop sequence is a predefined or user-specified text string that
#     # signals an AI to stop generating content, ensuring its responses
#     # remain focused and concise. Examples include punctuation marks and
#     # markers like "[end]".
#     stop=None,

#     # If set, partial message deltas will be sent.
#     stream=False,
# )

# # Print the completion returned by the LLM.
# print(chat_completion.choices[0].message.content)