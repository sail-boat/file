# 特定フォルダ以下のファイルのファイル名 指定文字数分削除

require 'find'
require 'fileutils'

path = ARGV[0] ? ARGV[0] : '.' # 引数より対象フォルダパス取得
sliceIdx = ARGV[1].to_i
sliceLen = ARGV[2].to_i

Find.find(path) do |item|
	fileNm = File.basename(item)
	fileNmN = String.new(fileNm)
	if FileTest.file?(path + '/' + fileNm)	
		fileNmN.slice!(sliceIdx, sliceLen)
		FileUtils.mv(path + '/' + fileNm, path + '/' + fileNmN)
	end
end