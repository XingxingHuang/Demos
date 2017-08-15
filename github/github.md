可以参考的学习资料	

* [try git](https://try.github.io/levels/1/challenges/1)
* Git 参考手册 [网站](http://gitref.org/zh/index.html)
* github 用法 [网站](https://guides.github.com/activities/hello-world/)


```
git log	查看log文件
git push -u origin master 用u记住我们这次的参数，下一次不需要重新输入。
git diff HEAD 
git diff --staged
git reset octofamily/octodog.txt
git checkout -- octocat.txt
git branch clean_up
git checkout clean_up
git merge clean_up
git branch -d clean_up
```

commit

```
git commit -m ""
git commit -ammend "" #修改上一次的commit
git rebase -i HEAD~N  #look over and reword the last N commits
```

克隆一个项目到本地

```
$ git clone <版本库的网址> <本地目录名>
```

添加一个远程工程路径，保存到本地```upstream/master```分支，切换到本地分支， 然后合并到本地的分支

```
git remote add upstream  *.git
git fetch upstream
git checkout master
git merge upstream/master

```

部分查找，修改的命令。查看remote工程

```
git remote show [remote-name] 	
git remote -v	
git remote set-url origin *.git
git fetch [remote-name]
git pull upstream master
git pull --rebase upstream master
git push [remote-name] [branch-name]:[branch-name]
```
另外`git branch`命令的`-r`选项，可以用来查看远程分支，`-a`选项查看所有分支。
取回远程主机的更新以后，可以在它的基础上，使用`git checkout`命令创建一个新的分支。`git checkout -b newBrach origin/master`



