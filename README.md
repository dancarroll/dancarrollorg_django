**ARCHIVED**: This was the old version of my website, written using Python and the Django web framework. It has not been modified
since 2011, and is only kept around for reference purposes.

----------


Generate code sample HTML with:
pygmentize -O style=native -f html -l <LANGUAGE, i.e. python, or blank> -o <OUTPUT.html> <INPUT, i.e.:models.py>


Website color scheme:
---------------------
http://kuler.adobe.com/#themeID/748381
scheme name: shy

dark blue: 121C26
grey: 30403B
light grey: 8B9976
beige: BFBF8A
orange: 8C4119


Special thanks to:
------------------
Social network icons courtesy of Komodo Media
http://www.komodomedia.com/download/
Social Network Icon Pack by Rogie King is licensed under a Creative Commons Attribution-Share Alike 3.0 Unported License (http://creativecommons.org/licenses/by-nc-sa/3.0/)

django-paging for the InfinitePaginator code

Graham Binns for a starting point for using django-xmlrpc to implement the MetaWeblog API

Components used:
----------------
All required components are listed in the requirements file.  To install these dependencies, use the following command (ideally run inside of a virtualenv):
pip install -r requirements.txt

