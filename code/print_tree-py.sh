#!/bin/bash

tree -L 3
echo ""

##————————————————————————————————————————————————————————————————————————————##

file_list=(
    "website_app.py" "flask_routes/docs_app.py"
    "templates/docs_page.html"
    )

for file in "${file_list[@]}"; do
    echo "[START] $file "
    cat  "$file"
    echo "[ END ] $file "
    echo ""
done
