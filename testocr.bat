cd ./sample_test
python ../tools/GetVerCode.py 1500
python ../tools/resize.py
python ../ocrvercode.py ../yanzheng_cnn_2d_model.json ../yanzheng_cnn_2d_weights.model