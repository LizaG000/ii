import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization, Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.models import Sequential
from keras.utils import to_categorical
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def get_json() -> dict:
    with open("intents copy.json", "r", encoding="utf-8") as f:
        return json.load(f)

def train_model():
    x_texts = []  # тексты
    _y_labels = []  # индексы интентов
    intents_dict = get_json()
    intent_names = list(intents_dict.keys())

    # подготовка данных
    for key, data in intents_dict.items():
        for example in data["input_example"]:
            x_texts.append(example)
            _y_labels.append(key)
#     vectorizer = TfidfVectorizer()
#     X = vectorizer.fit_transform(x_texts)
    
#     model = LogisticRegression()
#     model.fit(X, y_labels)
#     for i in range(len(x_texts)):
#         X = vectorizer.transform([x_texts[i]])
#         intent = model.predict(X)[0]
#         print(x_texts[i])
#         print(y_labels[i])
#         print(intent)
#     X = vectorizer.transform(["пока"])
#     intent = model.predict(X)[0]
#     print(intent)
# train_model()
    print(_y_labels)
    x_texts = np.array(x_texts)
    y_labels = np.array(_y_labels)

    # векторизация текста
    vocab_size = 300
    embedding_dim = 10
    sequence_length = 6

    vectorizer = TextVectorization(
        max_tokens=vocab_size,
        output_mode='int',
        output_sequence_length=sequence_length
    )
    _vectorizer = TextVectorization(
        max_tokens=7,
        output_mode='one_hot'
    )
    vectorizer.adapt(x_texts)
    print(y_labels)
    _vectorizer.adapt(y_labels)
    print(y_labels)

    # преобразуем тексты в последовательности чисел
    x_vect = vectorizer(x_texts)
    # x_vect = x_vect.to_tensor()
    intent_names = list(intents_dict.keys())  # ['greeting', 'goodbye', 'catalog', ...]
    y_labels = [intent_names.index(label) for label in y_labels]
    print(y_labels)
    y_labels = to_categorical(y_labels, num_classes=8).astype(np.float32)
    print("Векторы x (числовое представление текста):")
    print(x_vect.numpy())
    print("y (метки интентов):")
    print(y_labels)

    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True),
        GlobalAveragePooling1D(),
        Dense(32, activation='relu'),
        Dense(len(intent_names), activation='softmax')
    ])

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    # Передаём строки напрямую
    model.fit(x_vect, y_labels, validation_split=0.2, epochs=30, batch_size=16)

    # # модель
    # model = Sequential([
    #     Embedding(input_dim=vocab_size, output_dim=embedding_dim, mask_zero=True),
    #     GlobalAveragePooling1D(),
    #     Dense(32, activation='relu'),
    #     Dense(len(intent_names), activation='softmax')
    # ])

    # model.compile(
    #     loss='sparse_categorical_crossentropy',
    #     optimizer='adam',
    #     metrics=['accuracy']
    # )

    # # обучение
    # model.fit(x_vect, y_labels, epochs=30, batch_size=16, verbose=0)

    # предсказания модели
    predictions = model.predict(x_vect)
    predicted_classes = np.argmax(predictions, axis=1)

    print("\nПредсказания модели для каждого текста:")
    i = 0
    for text, true_idx, pred_idx in zip(x_texts, y_labels, predicted_classes):
        print(f"Текст: {text}")
        print(f"Истинный интент: {true_idx}")
        print(f"Предсказанный интент: {pred_idx}")
        print("---")

train_model()