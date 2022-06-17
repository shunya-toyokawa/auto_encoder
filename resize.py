from PIL import Image
img_file = 'input.png'

# リサイズ前の画像を読み込み
img = Image.open(img_file)
# 読み込んだ画像の幅、高さを取得し半分に
(width, height) = (img.width // 4, img.height // 4)
# 画像をリサイズする
img_resized = img.resize((width, height))
# ファイルを保存
img_resized.save('inputs/output.png', quality=90)
