#!/bin/bash

target="${1:-}"
if [ -z "$target" ]; then
    echo "Usage: latex-build <target.pdf|target.tex|target>"
    exit 2
fi

base=$(basename "$target")
base="${base%.pdf}"
base="${base%.tex}"
texfile="${base}.tex"
mpfile="${base}.mp"
logfile="${base}.log"
extensions="mp log aux mpx nav toc snm out vrb [1-9] [1-9][0-9]"
compile="pdflatex -shell-escape -halt-on-error"
tempfile=$(mktemp)
keep_log=0

function remove_droppings() {
    for ext in $extensions; do
        if [ "$ext" == "log" -a "$keep_log" -ne 0 ]; then
            continue
        fi
        rm -f -- "${base}".${ext}
    done
}

function cleanup() {
    remove_droppings
    rm -f -- "${tempfile}"
}
trap cleanup EXIT

function compile_once() {
    $compile "$texfile" > "$tempfile"
    if [ $? -ne 0 ]; then
        keep_log=1
        cat "$tempfile"
        echo
        echo
        echo ERROR
        exit 1
    fi
}

function need_to_rerun() {
    if [ ! -e "$logfile" ]; then
        return 0
    fi
    if [ $(grep -E "Rerun" "$logfile" | grep -Ev "^Package" | wc -l) -gt 0 ]; then
        return 0
    else
        return 1
    fi
}


echo "Building first time."
compile_once

if [ -e "$mpfile" ]; then
    echo "Building meta post."
    compile_once
fi

count=0
while need_to_rerun; do
    echo "Rerunning by direction from logfile."
    compile_once
    ((count+=1))
    if [ $count -ge 5 ]; then
        echo "Too many reruns ($count)."
        echo "Stopping"
        exit 1
    fi
done

echo "Done"
exit 0
