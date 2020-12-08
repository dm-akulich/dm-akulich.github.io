---
layout: post
title: Приложение sudo purge
comments: true
category: bash mac
tags: bash mac
---

To create a service, open up Automator, then choose to start a "Service." Next, drag "Run AppleScript" over to the right pane, then use the code below in the box. Then just save it as "Sudo Purge" or "Purge" or whatever you want to name it. When you want to use it, just select the name of whatever app's currently selected in the menu bar, choose "Services," then whatever you named it.

```applescript
tell current application
	activate
	do shell script "sudo purge" with administrator privileges password "password"
end tell
```

To make an app that you can click on from your Dock, or wherever, open a new file in Automator, select "Application," and do the same exact thing as above. It will save as an Automator application that you can place wherever you want. You can <a href="https://mac-how-to.gadgethacks.com/how-to/change-your-mac-icons-0151545/" target="_blank">change the app icon</a> too if you want.