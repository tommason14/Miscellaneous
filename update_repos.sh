#!/usr/bin/env sh

update_git() {
  git pull
  git add .
  git commit
  git push
}

update_and_cd() {
  echo ">>> $(pwd) <<<"
  update_git
  cd $cwd
}

run_loop() {
  for f in $@
  do
    cd $f
    update_and_cd
  done
}

cwd=$(pwd) 
repos_in_documents_folder="$(find . -name ".git" | xargs -I {} dirname {})"
additional="$HOME/dotfiles $HOME/Documents/monash_automation"
repos="$repos_in_documents_folder $additional"
run_loop $repos
