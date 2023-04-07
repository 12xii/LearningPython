# Matplotlib

---

데이터 시각화 처리

---

## 라이브러리 추가

`from matplotlib import pyplot as plt`

`import matplotlib.pyplot as plt`

(둘은 같은 구문)

---

## 사용

```
x = np.arange(0, 5, 0.5)
y = x**2

plt.plot(x, y)
```

x, y 값은 `numpy`를 이용해 만든다

---

## 꾸미기

![img](https://scontent.xx.fbcdn.net/v/t1.15752-9/337772488_1653889028379063_7696933224650799247_n.png?_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=lyghIKIP81AAX_Cru-0&_nc_oc=AQliC-52oYxYqnIJ3QDPHt5JmH2M0OWi0HWbGkdcBvPEJQxomrJsATy6u_o2uU6GyJI3X2uTtpQzuJSK1slbZQMY&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQKxg1fBZGvtfUDcgreoXAb-lZUMhPQOxg1Heh3ZsQbDg&oe=6456E410)

선 스타일 / 마커 바꾸기 : 
 [공식문서 - line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle) /
 [공식문서 - marker](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers)

제목 / 축 제목 : 
 `plt.title('')` /
 `plt.xlabel('', labelpad = , fontdict='')` /
 `plt.ylabel('', labelpad = , fontdict='')`

축 간격
 `plt.xticks(x)` /
 `plt.yticks(x)`

배경 그리드
 `plt.grid(boolean, axis = '', color = '', alpha = '')`

범례
 `plt.legend(loc_num = '')`

---

