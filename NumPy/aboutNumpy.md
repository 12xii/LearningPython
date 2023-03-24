# NumPy

```
import numpy as np

# np라는 이름으로 numpy 모듈을 import 한다
```

---

## NumPy

+ 배열에서의 빠른 작업을 위한 라이브러리

+ 같은 타입의 배열만을 허용 => 기존 배열 대비 빠른 속도

+ 정적 배열 -> 크기 변경 시 원본 삭제, 새 배열 생성

    + 파이썬 내장 배열의 경우 동적 배열

+ 2차원 이상의 다차원 배열의 사용 가능

---

## NumPy 사용

### array Class : ndarray

NumPy의 배열 클래스는 ndarray라고 한다

ndarray : N demensional array

| 주요 객체 속성 | 기능 |
| ----------- | --- |
| .ndim       | 배열의 차원 수 |
| .shape      | 차원 ex) 2demension : (n, m) |
| .size       | 총 요소 수 |
| .dtype      | 요소 유형의 설명 |
| .itemsize   | 각 요소의 크기 |
| .data       | 실제 요소를 포함하는 버퍼 ( 보통 미사용 ) |


### 배열 생성

```
import numpy as np

a = np.array([2, 3, 4])
```

`a`는 `[2, 3, 4]`인 배열이다

| 함수 | 기능 |
| --- | --- |
| .array(\[elements\]) | `ndarray` 타입 생성 |
| .zeros((row, column)) | 0으로 가득 찬 `row * column` 크기의 ndarray 생성 |
| .ones((row, column)) | 1로 가득 찬 `row * column` 크기의 ndarray 생성 |
| .empty((row, column)) | 빈 `row * column` 크기의 ndarray 생성 |
| .arange(start, end, step) | `start`에서 `end`까지의 범위 중 `step`만큼 일정하게 나뉜 일련의 ndarray 생성 |

### 배열의 출력
```
# 1d
[1 2 3 4 5]

# 2d
[[0  1  2]
 [3  4  5]
 [6  7  8]
 [9 10 11]]

# 3d
[[[  0  1  2  3]
  [  4  5  6  7]
  [  8  9 10 11]]
  
 [[ 12 13 14 15]
  [ 16 17 18 19]
  [ 20 21 22 23]]]
```

+ 배열의 사이즈가 너무 큰 경우 배열의 중앙은 건너뛴다

    + 비활성화 옵션
        ```
        np.set_printoptions(threshold = sys.maxsize)
        ```
---

## Operator

+ 각 연산자는 행렬 연산처럼 요소별로 작동한다

+ 새 배열을 만들거나 얕은 복사를 하지 않고 기존 배열의 수정

### indexing, slicing and Iterating

리스트 등과 같은 원리로 인덱싱 / 슬라이싱 / 반복 가능

### 모양 조작

`a.reshape(INTEGER)` : 수정된 모양으로 인수 반환

`ndarray.resize((INTEGER))` : 배열 자체 수정

### 배열 쌓기

```
a = [[1, 2],
     [3, 4]]

b = [[5, 6],
     [7, 8]]

np.vstack((a, b)) # == row_stack()

# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
```
```
np.hstack((a, b))

# array ([[1, 2, 5, 6]
#         [3, 4, 7, 8]])
```