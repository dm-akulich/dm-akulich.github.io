#!/usr/bin/env python3
import os
import re
import os.path


def add_post(path_to_blog, categories):
    # Ввод названия поста
    while True:
        post_name = input('What is the title of your new post? <yyyy-mm-dd-my-new-post>\n')
        post_name_pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-zA-Z-0-9+]*$")
        if post_name_pattern.match(post_name):
            break
        else:
            print("Wrong name!")

    # Создание файла с постом
    while True:
        if os.path.exists(path_to_blog+'/_posts/'+post_name+'.md'):
            print("File is already exists!")
            break
        else:
            with open(path_to_blog+'/_posts/'+post_name+'.md', "w") as f:
                categories_dict = categories
                print('Available categories')
                for e, key in categories_dict.items():
                    print('[' + str(e) + ']', key)
                chosen_category = int(input("What is category?"))
                sample_content = '---\nlayout: post\ntitle: Заголовок Поста \ncomments: False\ncategory: {1}\ntags:\n---\n\n<img src="/assets/img/{0}/1.png">'.format(post_name, \
                                                                                                                                                                  categories_dict[chosen_category])
                f.write(sample_content)
            print("File has been created.")
            break

    # Создание директории с картинками
    while True:
        create_folder = input('Do you want to create directory for images? (Y|N)\n')
        if create_folder == 'y' or create_folder == 'Y':
            if not os.path.exists(path_to_blog+'/assets/img/'+post_name):
                os.makedirs(path_to_blog+'/assets/img/'+post_name)
            print("Post file and directory for images have been created successfully.")
            break
        elif create_folder == 'n' or create_folder == 'N':
            print("Only post file has been created.")
            break
        else:
            continue

    return input('Press any key to exit.\n')


if __name__ == '__main__':
    post_categories = {
        1: 'python',
        2: 'sql',
        3: 'bash',
        4: 'other'
    }
    add_post('/Users/dima/dev_my/dm-akulich.github.io', post_categories)
