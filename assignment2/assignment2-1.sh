# Renat Norderhaug, CS 447, assignment 2

#!/bin/bash
# problem 
# 1. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat'
find /usr/share/man -name stat*
echo "1."

# problem 
# 2. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat', sort(1) them, and produce a uniq(1)
 # count
find /usr/share/man -name stat* | sort | uniq -c
echo "2."

#problem 3

 # 3. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat', cut(1) the path and retrieve the
 # file's parent directory (IE: man1). sort(1) and perform a 
 # a uniq(1) count of those directories.
 # Your output should look like the following
 # 1 man1
 # 6 man2
find /usr/share/man -name stat* | sort | cut -d / -f 5-5 | uniq -c
echo "3."

#problem 4
# 4. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat' then pipe the results to xargs 
 # and get the file type, use the file command with the -b
 # argument
find /usr/share/man -name stat* | xargs file -b
echo "4."

#problem 5
 # 5. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat' then pipe the results to xargs 
 # and compile the files to html
find /usr/share/man -name stat* | xargs zcat | groff -T html
echo "5."

#problem 6
# 6. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat' then pipe the results to xargs 
 # and compile the files to html with two processes.
find /usr/share/man -name stat* | xargs zcat | parallel -j 2 --pipe groff -T html
echo "6."

#problem 7
# 7. Use find(1) to find all the files in /usr/share/man
 # that start with 'stat' then pipe the results to parallel(1) 
 # and compile the files to html and
 # save the results is /srv/www/man with a .html extension
 # Hint: use parallel {}, zcat(1), groff(1) and stdout to an 
 # expression that uses basename(1)
find /usr/share/man -name stat* | xargs zcat | parallel -j 1 --pipe groff -T html
mkdir -p /srv/www/man
echo "7."