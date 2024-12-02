fruit_prices = {
    "사과": 1000,
    "바나나": 700,
    "오렌지": 1500,
    "포도": 2000,
    "복숭아": 1300
}

print("과일 가격표:")
for fruit, price in fruit_prices.items():
    print(f"{fruit}: {price}원")

print("\n특정 과일 가격 조회:")

apple_price = fruit_prices["사과"]
print(f"사과의 가격: {apple_price}원")

banana_price = fruit_prices["바나나"]
print(f"바나나의 가격: {banana_price}원")

fruit_prices["키위"] = 1800
print("\n키위를 추가한 후 과일 가격표:")
for fruit, price in fruit_prices.items():
    print(f"{fruit}: {price}원")

fruit_prices["사과"] = 1200
print("\n사과 가격을 수정한 후 과일 가격표:")
for fruit, price in fruit_prices.items():
    print(f"{fruit}: {price}원")

total_fruits = len(fruit_prices)
print(f"\n총 과일 종류 수: {total_fruits}")