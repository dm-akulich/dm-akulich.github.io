---
layout: post
title: 'Как архивировать и разархивировать через Bash'
category: bash
tags: bash
---

## Create a compressed tar archive
In the Terminal app  on your Mac, enter the tar command, then press Return.

For a basic compression of a folder named, for example, LotsOfFiles, you could enter:

```% tar -czf LotsOfFiles.tgz LotsOfFiles```

The ```z``` flag indicates that the archive is being compressed, as well as being combined into one file. You’ll usually use this option, but you aren’t required to.

If it’s a large folder, you may want to monitor the process by adding the ```v``` flag:

```% tar -czvf LotsOfFiles.tgz LotsOfFiles```

## Uncompress a tar archive
To uncompress a tar archive on your Mac, do one of the following:

In the Terminal app  on your Mac, enter the tar command with the x flag, then press Return. To see progress messages, also use the v flag. For example:

```% tar -xvf LotsOfFiles.tgz```
