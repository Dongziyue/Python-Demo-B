#### ~~~变量作用域~~~

#### ~~~可更改 `mutable` 与不可更改 `immutable` 对象~~~

### 4. 高阶函数

> 函数可以接收另一个函数作为参数，这个函数就是高阶函数 `Higher-Order Functions`

```python
def fn_higher(f, *numbers):
    s = 0
    for number in numbers:
        s += f(number)
    return s


print(fn_higher(abs, 1, 2, -1, -2, 0))
```

#### map

> `map` 函数接收两个参数，一个是函数，一个是 Iterable
> `map` 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回

```python
def power(x, n=2):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p
    
    
numbers = [1, 2, 3, 4]

print(list(map(power, numbers)))

print(list(map(str, numbers)))
```

#### reduce

`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

> `reduce` 把一个函数作用在一个序列 `[x1, x2, x3, ...]` 上，这个函数必须接收两个参数，`reduce` 把结果继续和序列的下一个元素做累积计算

```python
from functools import reduce


def power(x, n=2):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p
    
    
numbers = [1, 2, 3, 4]

print(reduce(pow, numbers))
```


```python
from functools import reduce


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))
```

#### filter

#### sorted

### 5. 返回函数
#### 函数作为返回值

#### 闭包

### 5. 匿名参数

### 6. 装饰器

### 7. 偏函数