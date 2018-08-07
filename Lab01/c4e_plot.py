import matplotlib

from matplotlib import pyplot
matplotlib.use('tkAgg')
# 1. Prepare data
labels = ["Web","Android","iOS","React Native"]
values = [40,25,20,15]
colors = ["green","green","green","gold"]
explode = [0,0,0,0.1] 
# explode: Tách 1 phần của biểu đổ ra ngoài
# 2.Plot
# pyplot.<tên của chart>
pyplot.pie(values,labels=labels,colors=colors,explode=explode)
# Tỉ lệ 2 cột bằng nhau
pyplot.axis('equal')

# 3.Show
pyplot.show()

