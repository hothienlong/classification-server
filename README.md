Create Development Environment 
<!-- 
# mỗi dự án lớn đều thường hard code một phiên bản cố định, để tránh sự bất đồng bộ => tải đúng phiên bản yêu cầu
# cài môi trường conda để quản lý package của 1 dự án, các package sẽ đc cài đúng vào môi trường đó (ko tốn thêm bộ nhớ nhờ cơ chế ánh xạ, chỉ cài thêm nếu chưa có package đó, cùng env thì package mới khác phiên bản sẽ ghi đè phiên bản cũ)

# conda quản lý mọi thứ python, có sẵn tất cả phiên bản, ko cần cài thêm

# conda env list: xem các môi trường đã tạo -->

``` 
conda create -n classification python=3.6 (tạo môi trường python)
conda activate classification (active môi trường đã tạo)
pip install underthesea
```
# pip install -r requirements.txt

# pip install torch===1.5.1 torchvision===0.6.1 -f https://download.pytorch.org/whl/torch_stable.html


Download VNTC dataset

```
underthesea download-data VNTC
```

Train a text classifier model

```
python vntc_train.py 
>>> Start training
Dev score: 0.933037037037037
Test score: 0.9267266194191333
>>> Finish training in 116.78 seconds
Your model is saved in tmp/classification_svm_vntc
```

Predict using trained model

```
python vntc_predict.py

Text: Một Mình Cân Hết Mâm Tôm Nữ Hoàng Rang Muối Ớt Siêu Cay ngon nhức nách 😆
Labels: ['thucpham_douong']

Text: Quang Hải đang đá bóng
Labels: ['thethao'] 
```

Optimize hyper-parameters

```
$ python optimize_hyperparameters.py 
```
