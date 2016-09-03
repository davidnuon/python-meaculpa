#!/usr/bin/python

import cgi

print "Content-Type: text/html\n\n"
print '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Mercury Layout</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>
	<div class="ContentBox">
   	  <div class="ContentBoxHead">
       	<div class="ContentBoxHeadDec">
			<img src="img/root.png" alt="root" style="margin-top:30px;margin-left:255px"/>
		</div>
            <div id="ContentBoxHeadNavi">
            	<ul>
					<li><a href="#" class="main_nav_home">Test</a></li>
                </ul>
			</div>
      </div>
        <div class="ContentBoxBody">
			<div class="ContentBoxBodyContents">
            	<h1>Test</h1>
            	Test
            </div>
        </div>
        <div class="ContentBoxFooter">
        </div>
    </div>
</body>
</html>

'''