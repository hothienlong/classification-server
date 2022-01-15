from underthesea.corpus.data import Sentence
from underthesea.models.text_classifier import TextClassifier
from flask import Flask, request, jsonify
from collections import Counter
from constants import *

app = Flask(__name__)

model_folder = "tmp/classification_svm_vntc"
print(f"Load model from {model_folder}")
classifer = TextClassifier.load(model_folder)
print(f"Model is loaded.")


def predict(text):
    print(f"\nText: {text}")

    # khởi tạo sentence có text, chưa có labels
    sentence = Sentence(text)
    # gọi predict để add_labels cho sentence
    classifer.predict(sentence)
    labels = sentence.labels
    print(f"Labels: {labels}")

    category = LIST_CATEGORIES[labels[0]]
    print(f"Category: {category}")
    return category


@app.route('/get_category', methods=['GET'])
def get_category():
    text = request.args.get('text')
    print(text)

    category = predict(text)
    print(category)
    return category


@app.route('/get_categories', methods=['POST'])
def get_categories():
    print("----------------get_categories-------------")
    texts = request.json['texts']
    print("----------------Texts-------------")
    print(texts)

    categories = map(predict, texts)

    # filter duplicate categories
    categories = list(dict.fromkeys(categories))

    # print(list(categories))

    return {"categories": list(categories)}


# đánh count cho mỗi category
@app.route('/get_categories_with_count', methods=['POST'])
def get_categories_with_count():
    print("----------------get_categories_with_count-------------")
    texts = request.json['texts']
    print("----------------Texts-------------")
    print(texts)

    categories = map(predict, texts)

    print(f"categories: {categories}")

    return {"categories": Counter(categories)}



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1000, debug=True)

# predict('Quay qua quay lại đến cuối tuần, thời gian trôi qua quá nhanh. Cuối tuần này các bạn làm gì? 😌Còn minh tranh thủ thời gian chơi cùng các con và đưa vợ đi làm, trên đường 2 vợ chồng nghe lại bài Nắm Lấy Tay Anh. Còn các bạn hôm nay có đang nghe bài nào của Hưng không? Chúc mọi người cuối tuần vui nhé! 😍')
# predict('Anh được công chúng biết đến qua vai trò là thành viên của nhóm nhạc Quả dưa hấu - nhóm nhạc nổi tiếng của Hà Nội vào những năm cuối thế kỉ 20 và qua vai trò')
# predict('Dưới sự cổ vũ của 12 nghìn khán giả trên sân Mỹ Đình, ĐT Việt Nam đã có màn trình diễn quả cảm trước ĐT Nhật Bản và chỉ chịu thua sát nút 0-1. Tiền vệ Junya Ito là tác giả bàn thắng duy nhất ở phút 17.')
# predict('Tiền vệ Nguyễn Quang Hải cho rằng, ĐT Việt Nam có quyền tự hào về những gì đã thể hiện trước đối thủ mạnh như ĐT Nhật Bản.')
# predict('“Họ vẫn nói ra nói vào, nhưng Binz không muốn nhắc đến “họ” trong nhạc của mình nữa.”')
# predict('Phỏng vấn độc quyền Rap Việt mùa 2.')
# predict('Theo chân MC Binz "hậu trường" nha các homie')
# predict('Đã gì đâu mâm bánh hỏi chả giò heo quay nguyên tảng giòn rộp gói rau,anh 3 Sa mê tít #1034')
# predict('Đại tiệc thú linh tai heo khìa nước dừa&bánh bía sầu riêng-chia buồn cùng cô chú mất đàn chó #1049')
# predict('jđjoou')
# predict('Bên cạnh đó, Mr.T và Hoà Minzy tiếp tục đưa đến khán giả nhiều món ăn mới, phong phú của ẩm thực ba miền Bắc - Trung - Nam với phần lời khá vui nhộn. Ca khúc đã đưa đến thông điệp khá giản dị, nhẹ nhàng, thể hiện tinh thần quảng bá những món ăn truyền thống nhưng vô cùng ý nghĩa: Văn hóa Ẩm thực Việt Nam đậm đà bản sắc dân tộc.')
