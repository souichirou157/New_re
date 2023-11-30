import os
from con_str import module #フォルダ->ファイル名
file =["html1.html","html2.html","html3.html"]
n = len(file)
H_text = [None] * n  # n個のNone要素を持つリストを作成
Mark_up =  module.mark()


path = os.path.expanduser("~/Desktop/new_dir")
class Write_text:
    def write(HTML, string):
        if path[0] == 'C' and path[7] == 's': 
            with open(HTML, 'w', encoding='utf-8') as html: 
                html.write(string) 
            return  0 


print(Mark_up) #htmlファイルソース表示 





for i in range(n):
        H_text[i] = os.path.join(path, file[i])
        Write_text.write(H_text[i], Mark_up)
    
    
    


