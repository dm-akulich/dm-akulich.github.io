---
layout: post
title: Настройки терминала
comments: true
category: bash
tags: bash
---

*Источники*
- [How To Customize Your macOS Terminal](https://medium.com/@charlesdobson/how-to-customize-your-macos-terminal-7cce5823006e)
- [Tilde Remapping](https://www.grzegorowski.com/how-to-remap-single-mac-keyboard-key)

<img src="/assets/img/2020-10-26-terminal-config/7.png">

## 1. Установка темы

Перетащить Pro.terminal тему в список с темами. [Ссылка на тему](https://github.com/dm-akulich/mac_config_repo/blob/main/Pro.terminal). И нажать Default.

Ссылка на репо с темами (https://github.com/nathanbuchar/atom-one-dark-terminal)[https://github.com/nathanbuchar/atom-one-dark-terminal]

<img src="/assets/img/2020-10-26-terminal-config/1.png">

## 2. Setting Preferences

**Text Tab**
<img src="/assets/img/2020-10-26-terminal-config/8.png">

**Window Tab**
<img src="/assets/img/2020-10-26-terminal-config/2.png">

**Tab Tab**
<img src="/assets/img/2020-10-26-terminal-config/3.png">

**Shell Tab**
<img src="/assets/img/2020-10-26-terminal-config/4.png">

**Keyboard**
<img src="/assets/img/2020-10-26-terminal-config/6.png">

**Advanced**
<img src="/assets/img/2020-10-26-terminal-config/5.png">

## 3. Configuring .bash_profile

```bash
cd ~
touch .bash_profile
nano .bash_profile
```

В **.bash_profile** добавляем 

```
source ~/.bash_prompt
source ~/.aliases 
```

## 4. Configuring .bash_prompt

```bash
touch .bash_prompt
nano .bash_prompt
```

В **.bash_prompt** добавляем 

```bash
#!/usr/bin/env bash

# GIT FUNCTIONS
git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# TERMINAL PROMPT
PS1="\[\e[0;93m\]\u\[\e[m\]"    # username
PS1+=" "    # space
PS1+="\[\e[0;95m\]\W\[\e[m\]"    # current directory
PS1+="\[\e[0;92m\]\$(git_branch)\[\e[m\]"    # current branch
PS1+=" "    # space
PS1+="$ "    # end prompt
export PS1;

export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
```

## 5. Configuring .aliases

```bash
nano .aliases
```

В .aliases добавляем

```bash
#!/usr/bin/env bash

# NAVIGATION
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
# COMMON DIRECTORIES
alias dl="cd ~/Downloads"
alias dt="cd ~/Desktop"
alias dc="cd ~/Documents"
alias p="cd ~/Documents/projects"
alias home="cd ~"
# GIT
alias g="git"
alias gs="git status"
alias gd="git diff"
alias gb="git branch"
alias gm="git checkout master"
```

## 6. Cleaning Up

Чтобы не показывалась дата последнего входа, просто добавляем в корень файл **.hushlogin**

```bash
touch .hushlogin
```



## 7. AUTOCOMPLETE

Type in terminal ```nano ~/.inputrc```. Paste the following on separate lines

```bash
set completion-ignore-case on
set show-all-if-ambiguous on
TAB: menu-complete

## arrow up
"\e[A":history-search-backward
## arrow down
"\e[B":history-search-forward
```


Hit Control+O to save changes to .inputrc followed by control+X to quit. Open a new Terminal window or tab, or type “login” to open a new session with the rules in effect. Type and hit the tab key.

## 8. Ремаппинг тильды для usb ПК клавиатуры на маке

Create plist file e.g. **/Library/LaunchDaemons/org.custom.keyboard-remap.plist**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>org.custom.keyboard-remap</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/hidutil</string>
      <string>property</string>
      <string>--set</string>
      <string>{"UserKeyMapping": [{"HIDKeyboardModifierMappingSrc":0x700000064, "HIDKeyboardModifierMappingDst":0x700000035}] }</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
  </dict>
</plist>
```

Then load it with ```sudo launchctl load -w /Library/LaunchDaemons/org.custom.keyboard-remap.plist``` so it will be loaded on each system reboot.

If you want to check if your plist file was loaded successfully you can use ```sudo launchctl list | grep org.custom.keyboard-remap.plist```


## 9. Использовать nano вместо vim по умолчанию

If you use bash on macOS, this is easiest done by editing your ```~/.bash_profile``` file and adding the two lines

```bash
export EDITOR=nano
export VISUAL="$EDITOR"
```

## 10. Tree

Чтобы можно было вызывать дерево инсталлим tree через homebrew

```bash
brew install tree
```

```
tree --help
------- Listing options -------
  -a            All files are listed.
  -d            List directories only.
  -l            Follow symbolic links like directories.
  -f            Print the full path prefix for each file.
  -x            Stay on current filesystem only.
  -L level      Descend only level directories deep. САМАЯ ПОЛЕЗНАЯ
  -R            Rerun tree when max dir level reached.
  -P pattern    List only those files that match the pattern given.
  -I pattern    Do not list files that match the given pattern.
  --ignore-case Ignore case when pattern matching.
  --matchdirs   Include directory names in -P pattern matching.
  --noreport    Turn off file/directory count at end of tree listing.
  --charset X   Use charset X for terminal/HTML and indentation line output.
  --filelimit # Do not descend dirs with more than # files in them.
  --timefmt <f> Print and format time according to the format <f>.
  -o filename   Output to file instead of stdout.
```

Гайд [List A Directory With Tree Command On Mac OS X](https://rschu.me/list-a-directory-with-tree-command-on-mac-os-x-3b2d4c4a4827)


## 11. Алиас со шпаргалкой командой ```h```

```bash
alias h="
  printf '\033[1;96mПросмотр содержимого папки\033[0m
ls                      \033[90m# показать содержимое папки\033[0m
ls -a                   \033[90m# то же, но показывать и скрытые файлы и папки\033[0m
ls -a -1                \033[90m# то же, но в один столбец\033[0m
ls build/css            \033[90m# показать содержимое папки ТЕКУЩАЯ_ПАПКА/build/css\033[0m
ls /d/projects          \033[90m# показать содержимое папки D:/projects\033[0m

\033[1;96mПереход по папкам\033[0m
cd projects             \033[90m# переход в папку projects, которая есть в текущей папке\033[0m
cd /d/projects          \033[90m# windows: переход в папку projects, расположенную по адресу D:/projects\033[0m
cd ..                   \033[90m# переход к родительской папке\033[0m
cd -                    \033[90m# переход к последней рабочей папке\033[0m
cd !$                   \033[90m# переход в новосозданную папку (после mkdir)\033[0m

\033[1;96mСоздание папок и файлов\033[0m
mkdir project                        \033[90m# создать папку с именем «project»\033[0m
mkdir project project/css project/js \033[90m# создать несколько папок\033[0m
mkdir -p project/{css,js}            \033[90m# то же, что выше\033[0m
touch index.html                     \033[90m# создать файл\033[0m
touch index.html css/style.css js/script.js \033[90m# создать файлы (папки css/ и js/ должны уже существовать)\033[0m

\033[1;96mКопирование файлов\033[0m
cp index.html catalog.html \033[90m# копирование файла index.html в тот же каталог с переименованием в catalog.html\033[0m
cp index.html old/         \033[90m# копирование файла index.html в папку old/ (все произойдет в текущей папке)\033[0m
cp temp/ temp2/ -r         \033[90m# дублирование каталога\033[0m

\033[1;96mПереименование или перемещение файлов\033[0m
mv index.html old              \033[90m# перемещение файла в папку\033[0m
mv index.html old/new_name.txt \033[90m# перемещение файла в папку с переименованием файла\033[0m
mv order.txt orderNew.txt      \033[90m# переименовать файл\033[0m

\033[1;96mУдаление папок и файлов\033[0m
rm ghost.png             \033[90m# удалить файл\033[0m
rm -rf old               \033[90m# удалить папку и всё из нее\033[0m

\033[1;96mРазные мелочи\033[0m
rm -rf node_modules && npm i        \033[90m# выполнение первой части команды (до &&) и, при отсутствии ошибок, второй части (после &&)\033[0m
pwd                                 \033[90m# «где я?»\033[0m
cat ~/.bash_profile                 \033[90m# вывести в консоль содержимое файла\033[0m
ls -a >> file.txt                   \033[90m# записать в file.txt результат вывода команды ls -a\033[0m
echo '\''some text'\'' >> readme.md       \033[90m# дописать строку в конец файла\033[0m
df -h                               \033[90m# показать статистику использования пространства на дисках\033[0m
grep -i -n --color '\''carousel'\'' index.html css/style.css \033[90m# найти слово carousel\033[0m
                                    \033[90m# в двух указанных файлах (с игнором регистра),\033[0m
                                    \033[90m# вывести строки с этим словом и номера строк (искомое слово подсветить)\033[0m
grep word -r project                \033[90m# найти слово word во всех файлах в папке project\033[0m
find . -iname '\''*ind*'\''               \033[90m# найти в текущей папке (и подпапках) все файлы,\033[0m
                                    \033[90m# имена которых содержат ind и показать списком\033[0m
curl -O https://vlc.org/vlc.dmg     \033[90m# скачивание файлов без браузера\033[0m
top                                 \033[90m# просмотр всех активных процессов\033[0m
defaults write com.apple.dock autohide-time-modifier -float 0 && killall Dock   \033[90m# ускорение анимации дока (ВКЛ)\033[0m
defaults write com.apple.dock autohide-time-modifier -float 0.7 && killall Dock \033[90m# ускорение анимации дока (ВЫКЛ)\033[0m
uptime                              \033[90m# время работы Mac\033[0m
'
"
```

<img src="/assets/img/2020-10-26-terminal-config/9.png">