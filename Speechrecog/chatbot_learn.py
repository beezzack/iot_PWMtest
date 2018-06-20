from chatterbot import ChatBot
from chatterbot.utils import input_function

bot = ChatBot(
	'Feedback Learning Bot',
	storage_adapter = 'chatterbot.storage.SQLStorageAdapter',

	logic_adapters=[
		{
			'import_path': "chatterbot.logic.MathematicalEvaluation",
			'import_path': "chatterbot.logic.TimeLogicAdapter",
			'import_path': "chatterbot.logic.BestMatch",
		},
		{
			'import_path': "chatterbot.logic.LowConfidenceAdapter",
			'threshold': 0.65,
			'default_response': "I am sorry, but I do not understand,"
		}
	],

	input_adapter = 'chatterbot.input.TerminalAdapter',
	output_adapter = 'chatterbot.output.TerminalAdapter',
	batabase = 'db.adlite3'
)

CONVERSATION_ID = bot.storage.create_conversation()

def get_feedback():
	text = input_function()

	if 'yes' in text.lower():
		return False
	elif 'no' in text.lower():
		return True
	else:
		print('Please type either "Yes" or "No"')
		return get_feedback

print('Type something to begin..')

while True:
	try:
		input_statement = bot.input.process_input_statement()

		if not bot.storage.find(input_statement.text):
			statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
			print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))

			if get_feedback():
				print('Please input the correct one')
				response = bot.input.process_input_statement()
				bot.lear_response(response1, input_statement)
				bot.storage.add_to_conversation(CONVERSATION_ID, statement, response1)
				print('Reaponses added to bot!')
		else:
			print('The statement is already in database.')
	except(KeyboardInterrupt ,EOFError, SystemExit):
		break



