import os
from meta import include 
faile =["html1.html","html2.html","html3.html"]#作りたい分のファイルの数だけ名前用意
n = len(faile)#要素数を取得
H_text = [None] * n  # 生成したファイルを格納するn個のNone要素を持つリストを作成
Mark_up = include.meta()


class Hyper_Text:
        def write(self,HTML, string):
           self.HTML = HTML
           self.string = string 
           with open(self.HTML, 'w', encoding='utf-8') as  html: 
                self.HTML.write(self.string) 
                
                return 0
            

print(Mark_up) 
# デスクトップ上の新しいディレクトリ内にHTMLファイルを作成します


path1 = os.path.expanduser("~/OneDrive/Desktop/new_dir")
if Hyper_Text == True:
    for i in range(n):
        H_text[i] = os.path.join(path1, faile[i])
        Hyper_Text.write(H_text[i], Mark_up)
            
        

'''
if __name__ == '__main__':
    print('Sccessfully New-Files ⇩') #これ表示されればエラーなし
'''