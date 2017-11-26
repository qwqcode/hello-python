import requests

src_url = 'https://i.pinimg.com/originals/92/ee/5b/92ee5ba6b5f101495249317b25908cff.gif'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '62.0.3202.94 Safari/537.36',
    'Referer': 'https://za.pinterest.com/',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
}
proxies = {'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}  # Shadowsocks
response = requests.get(src_url, headers=headers, stream=True, proxies=proxies)
content_size = int(response.headers['content-length'])  # 内容体总大小
chunk_size = 1024  # 单次请求最大值
now_size = 0
with open('download_img_example.gif', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=chunk_size):
        fd.write(chunk)
        now_size += len(chunk)
        if (content_size > 0) and (now_size == content_size):
            print('下载完毕 总大小：%.2f KB' % (int(content_size) / 1024))
