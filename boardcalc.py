from pprint import pprint
table=[]
row=8
col=8
html=""
url="board.html"
board=open(url,"w")
top='''
<html>
<link rel="stylesheet" href="board.css">
<body>
<div id="border">
<table id="board">

'''
bottom='''
</table>
</div>
</body>
'''
for i in range(row):
    tmp_row=[]
    for j in range(col):
        if i%2==0:
            if j%2==0:
                tmp_row.append(1)
            else:
                tmp_row.append(0)
        else:
            if j%2==0:
                tmp_row.append(0)
            else:
                tmp_row.append(1)
    table.append(tmp_row)

i,j=[0,0]
board.write(top)
for row in table:
    board.write("<tr>\n")
    j=0
    for cell in row:
        if cell==0:
            board.write('<td class="white-bg" id="%s">  </td>\n' % (str(i)+','+str(j)))
        else:
            if i in [0,1,2]:
                board.write('<td class="black-bg" id="%s"> <div class ="piece normal black-p">  </div> </td>\n' % (str(i)+','+str(j)))
            elif i in [5,6,7]:
                board.write('<td class="black-bg" id="%s"> <div class ="piece normal white-p">  </div> </td>\n' % (str(i)+','+str(j)))
            else:
                board.write('<td class="black-bg" id="%s"> </td>\n' % (str(i)+','+str(j)))
        j+=1
    board.write("</tr>\n")
    i+=1
board.write(bottom)
board.close()
