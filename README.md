# Training a Vietnamese Text Classifier

In this play, we build a `Vietnamese Text Classifier` using `VNTC` dataset

## Results

[*Corpus Description*](vntc_description.md)

Experiment results with SVM model and Tfidf, BoW features

| Models                                          | F1 (%)   |
|-------------------------------------------------|----------|
| TfidfVectorizer(ngram_range=(1, 2), max_df=0.5) | **92.8** |
| CountVectorizer(ngram_range=(1, 3), max_df=0.7) | 89.3     |
| TfidfVectorizer(max_df=0.8)                     | 89.0     |
| CountVectorizer(ngram_range=(1, 3)              | 88.9     |
| TfidfVectorizer(ngram_range=(1, 3))             | 86.8     |
| CountVectorizer(max_df=0.7)                     | 85.5     |

## Reproduce

Create Development Environment 

# mỗi dự án lớn đều thường hard code một phiên bản cố định, để tránh sự bất đồng bộ => tải đúng phiên bản yêu cầu
# cài môi trường conda để quản lý package của 1 dự án, các package sẽ đc cài đúng vào môi trường đó (ko tốn thêm bộ nhớ nhờ cơ chế ánh xạ, chỉ cài thêm nếu chưa có package đó, cùng env thì package mới khác phiên bản sẽ ghi đè phiên bản cũ)

# conda quản lý mọi thứ python, có sẵn tất cả phiên bản, ko cần cài thêm

# conda env list: xem các môi trường đã tạo

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

Text: Huawei có thể không cần Google, nhưng sẽ ra sao nếu thiếu ARM ?
Labels: ['vi_tinh']

Text: Trưởng phòng GD&ĐT xin lỗi vụ học sinh nhận khen thưởng là tờ giấy A4
Labels: ['chinh_tri_xa_hoi'] 
```

Optimize hyper-parameters

```
$ python optimize_hyperparameters.py 
```
