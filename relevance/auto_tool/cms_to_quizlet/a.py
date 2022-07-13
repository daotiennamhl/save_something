import re

res = ''

with open('cms.txt', encoding= 'utf-8') as f:
   cms = f.read()
   items = re.split(r'Question \d+', cms)
   for i in range(1, len(items)):
      item = items[i].split("Question text")[1].strip()
      question, answer = map(str.strip, item.split("Select one:"))
      option_answers, correct_answer = map(str.strip, answer.split("Feedback\nThe correct answer is:"))
      option_answers = list(map(str.strip, option_answers.split('\n')))
      for j in range(len(option_answers)):
         option_answers[j] = re.sub(r'([a-z]\.\s)', '', option_answers[j])
      correct_answer = chr(65 + option_answers.index(correct_answer))
      for j in range(len(option_answers)):
         option_answers[j] = chr(65 + j) + ". " + option_answers[j]
      # print(question, option_answers, correct_answer)
      res += str(i) + ". " + question + '\n' + '\n'.join(option_answers) + 'ANSS' + correct_answer + "ENDD"

with open('quizlet.txt', mode='w', encoding='utf-8') as f:
   f.write(res)

# Between term and definition: 'ANSS'
# Between cards: 'ENDD'

# dhs câu 70 không tạo được quizlet