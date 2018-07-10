---
title: Pomise
date: 2018-06-29 11:29:36
tags:
    - promise
---

### Promise 是什么
按照用途来解释：
+ 主要用于异步计算
+ 可以将异步操作队列化，按照期望的顺序执行，返回符合预期的结果
+ 可以在对象之间传递和操作 Promise ，帮助我们处理队列

<!-- more -->

```
new Promise(
    /* 执行器 executor */
    function (resolve, reject) {
        // 一段耗时很长的异步操作

        resolve(); // 数据处理完成

        reject(); // 数据处理出错
    }
)
    .then(function A() {
        // 成功，下一步
    }, function B() {
        // 失败，做相应处理
    });
```

+ Promise 是一个代理对象，它和原先要进行的操作并无关系
+ 它通过引入一个回调，避免更多的回调

### Promise 有3个状态：
+ **pending** [待定] 初始状态
+ **fulfilled** [实现] 操作成功
+ **rejected** [被否决] 操作失败

+ Promise 状态发生改变，就会触发 .then() 里面的响应函数处理后续步骤
+ Promise 状态一经改变，不会再变

### 举例：
```
console.log('here we go');
new Promise( resolve => {
    setTimeout( () => {
        resolve('hello');
    }, 2000);
})
    .then( value => {
        console.log( value + ' world');
    });
```

### 分两次，顺序依次执行，举例：
```
console.log('here we go');
new Promise( resolve => {
    setTimeout( () => {
        resolve('hello');
    }, 2000);
})
    .then( value => {
        console.log(value);
        return new Promise( resolve => {
            setTimeout( () => {
                resolve('world')
            });
        });
    })
    .then( value => {
        console.log( value + 'world');
    });
```

### 假如一个 Promise 已经完成了，再 .then() 会怎样？举例：
```
console.log('start');

let promise = new Promise(resolve => {
    setTimeout( () => {
        console.log('the promise fulfilled');
        resolve('hello, world);
    }, 1000);
});

setTimeout(() => {
    promise.then( value => {
        console.log(value);
    });
}, 3000);
```

### 假如在 .then() 的函数里面不返回新的 Promise，会怎样？举例：
```
console.log('here we go');
new Promise( resolve => {
    setTimeout( () => {
        resolve('hello');
    }, 2000);
})
    .then( value => {
        console.log(value);
        console.log('everyone');
        (function() {
            return new Promise( resolve => {
                        setTimeout( () => {
                            console.log('Mr.Laurence');
                            resolve('Merry Xmas');
                        }, 2000);
                    });
        }());
        return false;
    })
    .then( value => {
        console.log( value + 'world');
    });
```