users = ['Natsume', 'Kirito', 'Naruto', 'Eren']
html_str = '<ul>'
del_id = input('请输入 ID 来删除: ')
del users[int(del_id)]
query = input('Please input user info: ')
for name in users:
    if name.find(query) > -1:
        html_str += '<li>' + name + '</li>'
html_str += '</ul>'
print(html_str)
