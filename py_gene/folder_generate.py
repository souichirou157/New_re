import os

# デスクトップ上に新しいディレクトリを作成します
new_dir_path_recursive = os.path.expanduser("~/OneDrive/Desktop/new_dir")

class Mkdir:
    def mkdir(path):
            if not os.path.isdir(path):
                os.makedirs(path)
                Mkdir.mkdir(path)
              
                
                return   path
print(Mkdir.mkdir(new_dir_path_recursive))


'''
if __name__ == '__main__': #インポートして別ファイルでしか上の処理はできなくなる
        print('Sccessfully New-Folder')  #これ表示されればエラーはない
'''        
        