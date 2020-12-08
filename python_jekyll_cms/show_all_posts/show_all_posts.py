#!/usr/bin/env python3
import os
from os import listdir
from os.path import isfile, join
from simple_term_menu import TerminalMenu
import time
from .edit_post import edit_post


def show_all_posts(blog_path):
    only_files = ((sorted([f for f in listdir(blog_path+'/_posts')
                           if isfile(join(blog_path+'/_posts', f))]))[1:])[-10:]
    only_files_with_index = []
    for i in enumerate(only_files):
        only_files_with_index.append('['+str(i[0])+'] '+i[1])

    # All Posts
    all_post_menu_title = "  Last 10 Posts\n"
    all_post_menu_items = only_files_with_index
    all_post_menu_items = all_post_menu_items+["Back to Main Menu"]
    all_post_menu_back = False
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    all_post_menu = TerminalMenu(all_post_menu_items,
                                 all_post_menu_title,
                                 main_menu_cursor,
                                 main_menu_cursor_style,
                                 main_menu_style,
                                 cycle_cursor=True,
                                 clear_screen=True)

    while not all_post_menu_back:
        edit_sel = all_post_menu.show()
        for i in enumerate(all_post_menu_items):
            if i[0] == 0:
                if edit_sel == 0:
                    print("First Post")
                    time.sleep(1)
            elif i[0] != 0 and i[0] != 10:
                if edit_sel == i[0]:
                    print("Post is", i[1])
                    edit_post(blog_path=blog_path, post_name=i[1])

                    time.sleep(2)
            elif i[0] == 10:
                if edit_sel == 10:
                    all_post_menu_back = True
                    print("Back Selected")
    # all_post_menu_back = False
