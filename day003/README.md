# Day 3 - if文と日付計算

## 今日やったこと

* `if / elif / else` による条件分岐
* `try / except` によるエラー処理
* `input()` からの文字列入力
* `date.fromisoformat()` による日付変換
* `date.replace()` による日付の変更
* `date` 同士の引き算
* `timedelta.days` による日数の取得

## 作ったもの

年齢と誕生日を入力すると、20歳になるまでの日数を計算するプログラムを作成した。

```python
from datetime import date

age = int(input("Enter your age: "))
today = date.today()

print(f"Today's date is: {today}")

if age > 19:
    print("You can drink alcohol.")

elif age == 19:
    print("When is your birthday?")
    birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

    try:
        birthday = date.fromisoformat(birthday_input)

        twentieth_birthday = birthday.replace(year=birthday.year + 20)
        days = twentieth_birthday - today

        print(f"You can drink alcohol after {days.days} days")

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

else:
    print("You cannot drink alcohol.")
```

## 学んだこと

### 1. `if / elif / else`

条件によって処理を分けられる。

```python
if age > 19:
    ...
elif age == 19:
    ...
else:
    ...
```

### 2. `try / except`

エラーが発生する可能性がある処理を安全に実行できる。

```python
try:
    birthday = date.fromisoformat(birthday_input)
except ValueError:
    print("Invalid date format.")
```

### 3. `date` を使った日付計算

日付を手計算する必要はなく、`date` 同士を引き算できる。

```python
days = twentieth_birthday - today
```

結果は `timedelta` になる。

```python
days.days
```

で日数を取得できる。

### 4. `replace()`

```python
twentieth_birthday = birthday.replace(
    year=birthday.year + 20
)
```

誕生日の日付を基準に、20年後の日付を作ることができる。

## 今日のポイント

**日付の計算を自分で実装するのではなく、Pythonの `datetime` を使う。**

例えば、

```text
月の日数を自分で計算
        ↓
datetime.date に任せる
        ↓
date - date
        ↓
timedelta
```

という考え方を学んだ。

## Day 3 の感想

最初は月ごとの日数を自分で計算しようとしたが、`datetime` を使えば日付の差を直接計算できることが分かった。

Pythonの標準ライブラリを使うことで、複雑な処理をシンプルにできることを学んだ。
