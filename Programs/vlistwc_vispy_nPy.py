import numpy as np
import vispy.scene
from vispy.scene import visuals

# ファイルからデータを読み込む
coords = np.load('{"your path"}/colornum_{X}/iteration_{Y}/vlistwc/coords_{N}.npy', allow_pickle=True)
colors = np.load('{"your path"}/colornum_{X}/iteration_{Y}/vlistwc/colors_{N}.npy', allow_pickle=True)
elength = 5  # 辺の長さを設定

# 座標と色情報の処理
positions = np.array(coords)
colorset_w_alpha = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'gray', 'black']
color_indices= np.array(colors)

# Vispyキャンバスの設定
canvas = vispy.scene.SceneCanvas(keys='interactive', show=True, bgcolor='white')
view = canvas.central_widget.add_view()

# ポイントの追加
positions = np.array(positions)
scatter_colors = [colorset_w_alpha[index - 1] for index in color_indices]
scatter = visuals.Markers()  # 大文字に変更
scatter.set_data(positions, edge_color=None, face_color=scatter_colors, size=50*elength/2)
view.add(scatter)

print(positions)
# ビューの設定
view.camera = 'turntable'

# アプリケーションの実行
if __name__ == '__main__':
    vispy.app.run()
