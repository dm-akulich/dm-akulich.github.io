import os
import re


def edit_post(blog_path, post_name):
    print('blog_path is = ', blog_path)
    print('post_name is = ', post_name)
    post_name = (re.sub(r'^[\[\d\]]+', '', post_name)).lstrip(' ')
    print('post_name is = ', post_name)
    input('hello\n')


if __name__ == '__main__':
    path = '/Users/dima/dev_my/dm-akulich.github.io'
    name = '[2] 2020-11-16-ms-sql-server.md'  # приходит такое
    edit_post(path, name)
