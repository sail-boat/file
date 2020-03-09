# -*- coding: utf-8 -*-
"""
階層の深いディレクトリを1階層にする

以下のようなディレクトリを
dir
 - subdir
     - subdir
         - file

以下のように直す
dir
 - file     
    
以下のようにファイルが存在する階層が複数あれば処理対象外とする
dir
 - subdir
     - file
 - file
"""

import os
import shutil
import mimetypes

def get_proc_path(path):
    """
    ディレクトリが処理対象なら、処理対象のパスを返す
    """
    
    exe_path = ""  # 処理対象ディレクトリのパス
    i = 0

    for tpl in os.walk(path):
        i+=1
        if len(tpl[2]) > 0:  # ファイルが存在する場合
            # 全てリンクファイルならスルー
            # todo
            
            if len(exe_path) > 0:  # 既にファイルが存在するディレクトリが有った場合
                return ""  # 処理対象外
            exe_path = tpl[0]
    
    if len(exe_path) > 0:
        return exe_path
    
    return ""
    
def del_sub_dir(path):
    """
    サブディレクトリを削除
    """

    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            shutil.rmtree(os.path.join(path, f))

        
"""
メイン処理
"""
base_path = '.'
proc_list = []  # 処理対象ディレクトリ

# ディレクトリを取得
for f in os.listdir(base_path):
    
    # ディレクトリのpath
    dir_path = os.path.join(base_path, f)
    
    if os.path.isdir(dir_path):
        proc_list.append(f)

for f in proc_list:
    # ディレクトリを1件ずつ処理

    # ディレクトリのpath
    dir_path = os.path.join(base_path, f)
    
    exe_path = get_proc_path(dir_path)
    if len(exe_path) == 0:
        # ログ書き込み
        # todo
        continue
        
    # 最下層ファイルを最上層へ移動
    for sf in os.listdir(exe_path):
        # 同名ファイルは上書きされる
        shutil.move(os.path.join(exe_path,sf), os.path.join(dir_path,sf))
            
    # サブディレクトリを削除
    del_sub_dir(dir_path)
    
    # エラーが発生したらログを書き込み次のディレクトリへ
    # todo


