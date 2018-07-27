# 重複画像削除

require 'fileutils'

# ディレクトリ一覧取得
dirs = Dir.glob('*/')

dirs.each{|dr|
	if File.exist?(dr + '001.jpg') then
		if FileUtils.cmp('001.jpg', dr + '001.jpg') then
			for num in 1..58 do
				nums = format("%03d", num)
				File.delete dr + nums + '.jpg'
			end
		end
	end
}
