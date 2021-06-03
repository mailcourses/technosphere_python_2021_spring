#! /usr/bin/env bash

function main()
{
  local message=$(/usr/games/fortune)
  if [ $# -ne 0 ]; then
    message="$@"
  fi
  echo "${message}" | /usr/games/cowsay -f tux
}

main $@
