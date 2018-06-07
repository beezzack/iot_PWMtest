from chatterbot import ChatBot

bot = ChatBot(
    "Hey Robbt",
    storage_adapter='chatterbot.storge.SQLStorageAdapter'

    logic_adapter=[
        {
            'import_path':"chatterbot.logic.MathematicalEvaluation",
            'import_path':"chatterbot.logic.TimeLogicAdapter",
            'import_path':'chatterbot.logic.logic.BestMatch',
        }
        {
            'import_path':"chatterbot.logic.LowConfidenceAdapter",
            'threhold':0.65,
            'default_response':'I am sorry, but I do not understand'
        }
    ]

    input_adapter='chatterbot.input.logic.LowConfienceAdapter',
    output_adapter ='chatterbot.output.TerminalAdapter',
    database='db.splite3'
)

while True:
    try:
        response = bot.get_response(None)
    except(KeyboardInterrupt, EOFError, SysrwmExit):
        break
