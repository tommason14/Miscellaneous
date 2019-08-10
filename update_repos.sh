#!/usr/bin/env sh

update_git() {
  git pull
  git add .
  git commit
  git push
}

update_and_cd() {
  echo $(pwd)
  update_git
  cd $cwd
}

cwd=$(pwd) 
for f in $(find . -name ".git")
do 
  cd $(dirname $f)
  update_and_cd
done

cd ~/dotfiles
update_and_cd
cd ~/Documents/monash_automation
update_and_cd
