# FPT config
### Config git trên trường: 
    $ git config --global http.proxy http://proxy:8080
### ve nha: 
    $ git config --global --unset http.proxy
# command
## delete git tag
    Delete a remote Git tag
        git push --delete origin <tagname>
    Delete a local Git tag
        git tag -d <tag_name>
## unstage
    git ls-files
    git rm --cached
# task
## delete all local branch 
git branch | grep -v "development" | xargs git branch -D
## remove all history
git checkout --orphan latest_branch
git add -A
git commit -am "init commit"
git branch -D master
git branch -m master
git push -f origin master