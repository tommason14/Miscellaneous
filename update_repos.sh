#!/usr/bin/env sh

update_git() {
  git pull
  git add . 
  git commit
  git push
}

update_and_cd() {
  blue=$(tput setaf 4)
  normal=$(tput sgr0)
  printf "\n$blue>>> $(pwd) <<<$normal\n\n"
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
repos_in_documents_folder="$(find . -name ".git" | sort | xargs -I {} dirname {})"
additional="$HOME/.local/scripts $HOME/dotfiles"
repos="$repos_in_documents_folder $additional"
run_loop $repos
