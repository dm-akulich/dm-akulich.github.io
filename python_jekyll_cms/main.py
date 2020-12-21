#!/usr/bin/env python3
# Запускать и дебаггать через терминал
# This code only works in python3. Install per
# sudo pip3 install simple-term-menu

import os
from simple_term_menu import TerminalMenu
from image_compressor.image_compressor import crawler
from config import blog_path, post_categories
from create_backup.create_backup import make_tarfile, current_dt
from datetime import datetime as dt
import time
from add_new_post.add_new_post import add_post
from show_all_posts.show_all_posts import *


def main():
    main_menu_title = "  Jekyll CMS Menu\n"
    main_menu_items = ["Add new post",  # 0
                       "Optimize Images",  # 1
                       "Open Blog In VSC",
                       "Open Blog In Finder",
                       "Git commit && push",
                       "Show Last 10 Posts",
                       "Create Backup",
                       "Example Submenu",
                       "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    edit_menu_title = "  Example Submenu\n"
    edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:  # "Add new post"
            print("Add New Post Selected")
            add_post(blog_path, post_categories)
            time.sleep(1)

        elif main_sel == 1:  # Image Compressor
            crawler(input('Input full path to directory with images\n'))
            time.sleep(5)

        elif main_sel == 2:  # "Open Blog In VSC"
            os.system('code {}'.format(blog_path))
            time.sleep(5)

        elif main_sel == 3:  # "Open Blog In Finder"
            os.system('open {}'.format(blog_path))
            time.sleep(5)

        elif main_sel == 4:  # Git Update
            os.system('cd {} \
                    && git add . && git commit -m "post" && git push origin main && echo Updated Successfully'.format(
                blog_path))
            input('press enter to get back')
            time.sleep(5)

        elif main_sel == 5:  # All Posts
            show_all_posts(blog_path)
            time.sleep(2)

        elif main_sel == 6:  # Make backup
            print(
                make_tarfile(blog_path + '/backups/' + blog_path.split('/')[-1] + '-' + current_dt + '.tgz', blog_path))
            time.sleep(2)

        elif main_sel == 7:  # Example submenu
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Edit Config Selected")
                    time.sleep(5)
                elif edit_sel == 1:
                    print("Save Selected")
                    time.sleep(5)
                elif edit_sel == 2:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False

        elif main_sel == 8:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()
