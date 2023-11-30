import os



#  ~ is C:/Users/kpg13/Desktop
path_recursive = os.path.expanduser("~/Desktop/new_dir")


class Mkdir:
    def mkdir(path): #フォルダを生成
        
        if path[0] == 'C' and path[7] == 's': 
            os.makedirs(path)
    mkdir(path_recursive)




##正常なパスを認識する為にパス先頭のCドライブのＣとUsersの末尾sを認識したら生成処理をする
#それ以降はユーザー名によって隔たりがあるので参照しない

'''
if __name__ == '__main__':
    input('--created  a new  folder on your  Desktop') 
'''