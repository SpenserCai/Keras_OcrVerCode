假设你已经安装好了
python 2.7.12/13（包括pip）
keras 1.2.2（配置好GPU环境）
pillow 4.0.0
numpy 1.12.0+mkl
theano 0.8.2
h5py 2.6.0
captcha 0.2.1
lxml 3.7.2
scipy 0.18.1
PyYAML 3.12
...此处欢迎补充...

那么你可以通过运行5000VerCodeGet.bat生成5000样本，虽然说一定不够，至少50000以上（Windows系统，如果你是linux我相信你能自己搞定。）
之后通过python trainvercode_cnn.py yanzheng_cnn_2d，开始训练。
训练完成打开cmd切换到本文件所在目录运行testocr.bat进行测试。

更多内容之后补充
