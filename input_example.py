prompt = "If you tell us who you are, we can personalize the message you see."
prompt += '\nWhat is your first name?'

name = input(prompt + ' ')
print('\nHello, ' + name + '!')  # 这和 php 不同，单引号使用 \n 都可以换行

age = input('How old are you? ')
print('\n' + age + ' 是一个' + (
    '偶数' if int(age) % 2 == 0 else '奇数'
))
age_look_like = int(age) - 5
print("其实看上去你像是 " + str(age_look_like) + " 岁")

prompt = '\nTell me somethings, and I will repeat it bake to you:'
prompt += '\nEnter \'quit\' to end the program. '
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print('你刚刚说了：' + message)
