import urllib.parse

test_str = ' 这是一句话'
test_str_2 = "这又是一句话 "
test_str_3 = 'This is still the same sentence...'
test_str_3_upper = 'THIS IS STILL THE SAME SENTENCE...'

print('1. ' + test_str.lstrip())
print('2. ' + (test_str + test_str_2).strip())
print('3. ' + test_str_2.rstrip('话 ') + ' sentence'.title())

print('4. ' + test_str_3.title())
print('5. ' + test_str_3.upper())
print('6. ' + test_str_3.lower())
print('7. ' + str(test_str_3.upper() == test_str_3_upper.upper()))

print('8. ' + test_str_2[1])  # 0 是第一个字
print('9. ' + test_str_2[1:3])  # 开始(截取):结束(不截取)
print('10. ' + test_str_3[-1])  # -1 是倒数第一个字
print('11. ' + test_str_3[:4])  # 截取前 4 个 字符串
print('12. ' + test_str_3[4:])  # 删去前 4 个 字符串
print('13. ' + test_str_3[-4:])  # 截取最后 4 个 字符串
print('14. ' + test_str_3[:-5:-3])  # 逆序截取

print('15. ' + str("..." in test_str_3))
print('16. ' + str(test_str.find('这是')))
print('17. ' + str((test_str + test_str_2).count(' ')))
print('18. ' + test_str.replace('这是', 'This is '))

print('19. ' + ('{}/?{}'.format('admin', urllib.parse.urlencode({
    'access_token': '3143820-313847',
    'fields': 'id, url'
}))))
print('20. ' + '/examples/hello-world.html'.strip('/'))
print('21. ' + str(urllib.parse.urlsplit('https://www.xxx.com/%E5%93%88%E5%93%88%E5%93%88')))
