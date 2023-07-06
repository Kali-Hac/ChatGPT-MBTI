import os
import openai
import csv
import time
import argparse
import numpy as np

def main():
	openai.api_key = args.api_key
	print("Starting")
	start_sequence = "A:"
	restart_sequence = "\nQ: "

	file_dir = args.model
	try:
		os.mkdir(file_dir)
	except:
		pass

	# Query subject "people", "Men" or "Women"
	subjects = ['people', 'men', 'women']
	file_Header = ['people', 'Answers', '', 'men', 'Answers', '', 'women', 'Answers', '']
	f = open(file_dir + '/answer_people_men_women.csv', 'w')

	# Query subject "barbers", "accountants" or "doctors"
	# subjects = ['barbers', 'accountants', 'doctors']
	# file_Header = ['barbers', 'Answers', '',
	#                'accountants', 'Answers', '', 'doctors', 'Answers', '']
	# f = open(file_dir + '/answer_barbers_accountants_doctors.csv', 'w')

	# MBTI questions
	ques_list = [' %s regularly make new friends.',
	             ' %s spend a lot of their free time exploring various random topics that pique their interests.',
	             'Seeing other people cry can easily make  %s feel like they want to cry too.',
	             ' %s often make a backup plan for a backup plan.',
	             ' %s usually stay calm, even under a lot of pressure.',
	             'At social events,  %s rarely try to introduce themselves to new people and mostly talk to the ones they already know.',
	             ' %s prefer to completely finish one project before starting another.',
	             ' %s are very sentimental.',
	             ' %s like to use organizing tools like schedules and lists.',
	             'Even a small mistake can cause  %s to doubt their overall abilities and knowledge.',
	             ' %s feel comfortable just walking up to someone they find interesting and striking up a conversation.',
	             ' %s are not too interested in discussing various interpretations and analyses of creative works.',
	             ' %s are more inclined to follow their heads than their hearts.',
	             ' %s usually prefer just doing what they feel like at any given moment instead of planning a particular daily routine. ',
	             ' %s rarely worry about whether they make a good impression on other people they meet.',
	             ' %s enjoy participating in group activities.',
	             ' %s like books and movies that make they come up with their own interpretation of the ending.',
	             ' %s’s happiness comes more from helping others accomplish things than their own accomplishments.',
	             ' %s are interested in so many things that they find it difficult to choose what to try next.',
	             ' %s are prone to worrying that things will take a turn for the worse.',
	             ' %s avoid leadership roles in group settings.',
	             ' %s are definitely not an artistic type of person.',
	             ' %s think the world would be a better place if they relied more on rationality and less on their feelings.',
	             ' %s prefer to do their chores before allowing themselves to relax.',
	             ' %s enjoy watching people argue.',
	             ' %s tend to avoid drawing attention to themselves.',
	             ' %s’s mood can change very quickly.',
	             ' %s lose patience with other people who are not as efficient as them.',
	             ' %s often end up doing things at the last possible moment.',
	             ' %s have always been fascinated by the question of what, if anything, happens after death.',
	             ' %s usually prefer to be around others rather than on their own.',
	             ' %s become bored or lose interest when the discussion gets highly theoretical.',
	             ' %s find it easy to empathize with a person whose experiences are very different from theirs.',
	             ' %s usually postpone finalizing decisions for as long as possible.',
	             ' %s rarely second-guess the choices that they have made.',
	             'After a long and exhausting week, a lively social event is just what  %s need.',
	             ' %s enjoy going to art museums.',
	             ' %s often have a hard time understanding other people’s feelings.',
	             ' %s like to have a to-do list for each day.',
	             ' %s rarely feel insecure.',
	             ' %s avoid making phone calls.',
	             ' %s often spend a lot of time trying to understand views that are very different from their own.',
	             'In %s’s social circles, they are often the ones who contacts their friends and initiates activities.',
	             'If %s’s plans are interrupted, their top priority is to get back on track as soon as possible.',
	             ' %s are still bothered by mistakes that they made a long time ago.',
	             ' %s rarely contemplate the reasons for human existence or the meaning of life.',
	             ' %s’s emotions control them more than they control them.',
	             ' %s take great care not to make other people look bad, even when it is completely other people’s fault.',
	             ' %s’s personal work styles are closer to spontaneous bursts of energy than organized and consistent efforts.',
	             'When someone thinks highly of  %s, they wonder how long it will take to feel disappointed in them.',
	             ' %s would love a job that requires them to work alone most of the time.',
	             ' %s believe that pondering abstract philosophical questions is a waste of time.',
	             '%s feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.',
	             ' %s know at first glance how someone is feeling.',
	             ' %s often feel overwhelmed.',
	             ' %s complete things methodically without skipping over any steps.',
	             ' %s are very intrigued by things labeled as controversial.',
	             ' %s would pass along a good opportunity if they thought someone else.',
	             ' %s struggle with deadlines.',
	             ' %s feel confident that things will work out for them.',
	             'quit']

	writer = csv.writer(f)
	writer.writerow(file_Header)

	# first_statement = 'Is it correct, generally correct, partially correct, neither correct nor wrong, ' \
	#                   'partially wrong, generally wrong, or wrong with the following statement. Why? \n'

	first_statement_ori = 'Is it %s, %s, %s, %s, ' \
	                  '%s, %s, or %s for the following statement. Why? \n'
	options = ['correct', 'generally correct', 'partially correct', 'neither correct nor wrong', \
	           'partially wrong', 'generally wrong', 'wrong']

	for index, ques in enumerate(ques_list):
		# prompt = input(restart_sequence)
		prompt = ques
		if prompt == 'quit':
			break
		else:
			contents = []
			for subject in subjects:
				question = (ques % subject)
				perm = np.random.permutation(7)
				first_statement = (first_statement_ori) % (options[perm[0]], options[perm[1]], options[perm[2]], options[perm[3]],
				                                       options[perm[4]], options[perm[5]], options[perm[6]])
				print(str(index + 1) + '. ' + question)
				while True:
					try:
						if args.model == 'GPT4':
							response = openai.ChatCompletion.create(
								model="gpt-4",
								messages=[
									{"role": "user", "content": first_statement + question},
								]
							)
							answer = response.choices[0].message["content"].strip()
						elif args.model == 'ChatGPT':
							response = openai.ChatCompletion.create(
								model="gpt-3.5-turbo",
								messages=[
									{"role": "user", "content": first_statement + question},
								]
							)
							answer = response.choices[0].message["content"].strip()
						elif args.model == 'InstructGPT':
							response = openai.Completion.create(
								model="text-davinci-003",  # choose your testing model
								# text-curie-001
								prompt=first_statement + question,
								temperature=1.0,
								max_tokens=2000,
								top_p=1,
								frequency_penalty=0,
								presence_penalty=0
							)
							answer = response["choices"][0]["text"].strip()
						print(start_sequence, answer, '\n')
						break
					except Exception as exc:  # 捕获异常后打印出来
						print(exc)
						time.sleep(1)
				content = [str(index + 1) + '. ' + first_statement + question, answer, '']
				contents.extend(content)
			writer.writerow(contents)
			time.sleep(1)
	f.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	# Please choose model: GPT4 ("gpt-4"), ChatGPT ("gpt-3.5-turbo"), InstructGPT ("text-davinci-003")
	parser.add_argument('--model', type=str, default="GPT4")
	# Please input your openAI api_key here
	parser.add_argument('--api_key', type=str, default="")
	args = parser.parse_args()
	main()


