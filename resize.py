from PIL import Image
img_file = 'input.png'


# リサイズ前の画像を読み込み
img = Image.open(img_file)
magni = img.size[1]/ 512
print(magni)
# 読み込んだ画像の幅、高さを取得し半分に
(width, height) = (int(img.width // (5*magni)), int(img.height // (5*magni)))
# 画像をリサイズする
print(width,height)
img_resized = img.resize((width, height))
# ファイルを保存
img_resized.save('inputs/output.png', quality=90)
