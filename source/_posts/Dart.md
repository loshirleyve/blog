---
title: Dart学习
date: 2019-09-19 15:55:22
urlname: dart
tags: Dart
categories:
    - Dart
---

### 准备工作

### List 列表
常用属性：
* length    长度
* reversed  翻转
* isEmpty   是否为空
* isNotEmpty 是否为不空

常用方法
* add   增加
* addAll    拼接数组
* indexOf   查找  传入具体值
* remove    删除  传入具体值
* removeAt  删除  传入索引值
* fillRange 修改
* insert(index, value)  指定位置插入
* insertAll(index, list)    指定位置插入 List
* toList()  其他类型转换成 List
* join()    List 转换成字符串
* split()   字符串转化成 List
* forEach
* map
* where
* any


    List myList = ['a'];
    print(myList); // [a]
    
    myList.add('b'); // [a, b]
    
    myList.addAll(['c', 'd']); // [a, b, c, d]
    
    print(myList.indexOf('c')); // 2
    
    print(myList.indexOf('e')); // -1
    
    myList.remove('a'); // [b, c, d]
    
    myList.removeAt(1); // [b, d]
    
    myList.fillRange(0, 1, 'x'); // [x, d]
    
    myList.insert(1, 'y'); // [x, y, d]
    
    myList.insertAll(2, ['m', 'n']); // [x, y, m, n, d]
    
    print(myList.reversed); // (d, n, m, y, x), myList不变
    
    print(myList.reversed.toList()); // [d, n, m, y, x]
    
    print(myList.join('_')); // x_y_m_n_d
    
    print(myList.join('_').split('_')); // [x, y, m, n, d]
    
### Set 与 List 区别：Set 不能添加重复数据，List可以

    var s = new Set();
    s.add('a');
    s.add('b');
    s.add('a');
    print(s); // {a, b}
    
可利用 set 特性给数组去重

    List a = ['a', 'b', 'c', 'a', 'x', 'a'];
    var s = new Set();
    s.addAll(a);
    print(s.toList()); // [a, b, c, x]
    
### Map
常用属性：
* keys  获取所有的 key 值
* values    获取所有的 value 值
* isEmpty   是否为空
* isNotEmpty    是否为不空

常用方法：
* remove(key)   删除指定的 key 的数据
* addAll({...}) 合并 Map，给 Map 增加属性
* containsValue 查看 Map 内的值 返回 true/false
* forEach
* map
* where 
* any
* every


    Map person = {
      'name': 'shirley',
      'age': 18,
      'sex': 'female'
    };
    print(person); // {name: shirley, age: 18, sex: female}
    
    person.keys.toList() // [name, age, sex]
    
    person.values.toList() // [shirley, 18, female]
    
    person.addAll({
      "height": 168
    });  // {name: shirley, age: 18, sex: female, height: 168}
    
    person.containsValue('shirley'); // true
    
    
### 函数

    // 入口函数
    void main() {
    
    }
    
    void a() {
      print('无返回值函数');
    }
    
    int b() {
      print('返回值为 int 类型');
      return 1;
    }
    
    String c() {
      print('返回值为 String 类型');
      return 'c';
    }
    
    d() {
      print('不指定返回类型函数');
    }
    
    String printUserInfo(String name, [String sex='女', int age], {String work}) {
      print('默认参数，可选参数函数');
      if(age != null) {
        return "姓名：$name---性别：$sex---年龄：$age";
      }
      return "姓名：$name---性别：$sex---年龄保密";
    }
    print (printUserInfo('shirley', 20)); // 姓名：shirley---性别：女---年龄：20
    print (printUserInfo('shirley')); // 姓名：shirley---性别：女---年龄保密
    
    String printUser(String name, {int age, String sex='女'}) {
      print('命名函数');
      if(age != null) {
        return "姓名：$name---性别：$sex---年龄：$age";
      }
      return "姓名：$name---性别：$sex---年龄保密";
    }
    print (printUser('shirley', age:20)); // 姓名：shirley---性别：女---年龄：20
    print (printUser('shirley')); // 姓名：shirley---性别：女---年龄保密
    