#! /usr/bin/bash
message=$1
main(){
    if [ -z $message ]
    then
        message="fast_push"
    fi
    echo $message
    git add .
    git commit -m "$message"
    git push origin master
}
main $1