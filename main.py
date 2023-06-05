import requests
import _sqlite3
import time


def req(comment_id, max_id, max_id_type):
    if max_id == '':
        url = f'https://m.weibo.cn/comments/hotflow?id={comment_id}&mid={comment_id}&max_id_type={max_id_type}'
    else:
        url = f'https://m.weibo.cn/comments/hotflow?id={comment_id}&mid={comment_id}&max_id={max_id}&max_id_type={max_id_type}'
    #     add your cookie here
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        # 'cookie': ''
    }

    content = requests.get(url, headers=headers)
    return content


# replace the weibo id you want to get comment of
weibo_id = 1111222233334444

db_name = str(weibo_id) + '_comments.db'
conn = _sqlite3.connect(db_name)
c = conn.cursor()
c.execute('''
        CREATE TABLE IF NOT EXISTS comments(z 
            id TEXT PRIMARY KEY,
            created_time TEXT,
            screen_name TEXT,
            user_id TEXT,
            content TEXT
        )
    ''')

max_id_type = 0
data = req(weibo_id, max_id='', max_id_type=0).json()

comments = data['data']['data']
max_id = data['data']['max_id']

max_page = data['data']['max']
total_num = data['data']['total_number']
count = 1
print(f'total {max_page} pages，{total_num} comments')
print(f'the first page has {len(comments)} comments')
time.sleep(5)
while True:
    content = req(weibo_id, max_id, max_id_type).json()
    if content['ok'] == 0:
        break
    max_id = content['data']['max_id']
    max_id_type = content['data']['max_id_type']
    content = content['data']['data']
    count += 1
    print(f'page {count} has {len(content)} comments')

    for comment in content:
        c.execute('''
            INSERT OR REPLACE INTO comments VALUES (?,?,?,?,?)
        ''', (
            comment['id'],
            comment['created_at'],
            comment['user']['screen_name'],
            comment['user']['id'],
            comment['text']
        ))
    conn.commit()
    if max_id == 0:
        break
    time.sleep(5)
conn.close()
