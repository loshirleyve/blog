---
title: Dart学习
date: 2019-09-19 15:55:22
urlname: dart
tags: Dart
categories:
    - Dart
---
### Dart 文档
http://www.dartdoc.cn
 <!-- more -->
### DartPad 线上工具
https://dartpad.cn
https://gist.github.com/

### 准备工作

### List 列表
#### 常用属性：
* length    长度
* reversed  翻转
* isEmpty   是否为空
* isNotEmpty 是否为不空
#### 常用方法
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
```$xslt
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
```
### Set 与 List 区别
#### Set 不能添加重复数据，List可以
```$xslt
var s = new Set();
    s.add('a');
    s.add('b');
    s.add('a');
    print(s); // {a, b}
``` 
#### 可利用 set 特性给数组去重
```$xslt
List a = ['a', 'b', 'c', 'a', 'x', 'a'];
    var s = new Set();
    s.addAll(a);
    print(s.toList()); // [a, b, c, x]
```
### Map
#### Map 常用属性：
* keys  获取所有的 key 值
* values    获取所有的 value 值
* isEmpty   是否为空
* isNotEmpty    是否为不空
#### Map 常用方法：
* remove(key)   删除指定的 key 的数据
* addAll({...}) 合并 Map，给 Map 增加属性
* containsValue 查看 Map 内的值 返回 true/false
* forEach
* map
* where 
* any
* every
#### Map 使用示例
```$xslt
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
```
### 函数
```$xslt
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
    
// Dart 支持箭头函数，闭包
```
    
### 类    
#### Dart 是一门使用类和单继承的面向对象语言，所有的对象都是类的实例，并且所有的类都是 Object 的子类
```$xslt
class Person {
    String name;
    int age;

    // 默认构造函数
    // Person(String name, int age) {
    //   this.name = name;
    //   this.age = age;
    //   print("这是构造函数 这个方法在类实例化的时候触发");
    // }

    // 默认构造函数简写
    Person(this.name, this.age);

    /* dart 里面的构造函数可以写多个 */
    Person.now() {
      print("我是命名构造函数");
    }

    Person.setInfo(String name, int age) {
      this.name = name;
      this.age = age;
      print("我是命名构造函数setInfo");
    }

    void getInfo() {
        // print("$name---$age");
        print("${this.name}---${this.age}");
    }     
}

void main() {
  Person p = new Person("shirley", 18);
  print(p.name);
  p.getInfo();

  Person p1 = new Person('kyle', 20);
  print(p1.name);
  p1.getInfo();

  Person p2 = new Person.now();

  Person p3 = new Person.setInfo('mary', 16);
  p3.getInfo();
}

// 可以使用 _ 把一个属性或者方法定义成私有，注意必须把类抽离成单独的文件，通过 import 引入，才能让私有属性或文件真正私有
```
### Dart 中的抽象类 多态 和接口

#### Dart中抽象类: Dart抽象类主要用于定义标准，子类可以继承抽象类，也可以实现抽象类接口。

```$xslt
/*
  1、抽象类通过abstract 关键字来定义

  2、Dart中的抽象方法不能用abstract声明，Dart中没有方法体的方法我们称为抽象方法。

  3、如果子类继承抽象类必须得实现里面的抽象方法

  4、如果把抽象类当做接口实现的话必须得实现抽象类里面定义的所有属性和方法。

  5、抽象类不能被实例化，只有继承它的子类可以

extends抽象类 和 implements的区别：

  1、如果要复用抽象类里面的方法，并且要用抽象方法约束自类的话我们就用extends继承抽象类

  2、如果只是把抽象类当做标准的话我们就用implements实现抽象类

案例：定义一个Animal 类要求它的子类必须包含eat方法

*/

abstract class Animal{
  eat();   //抽象方法
  run();  //抽象方法  
  printInfo(){
    print('我是一个抽象类里面的普通方法');
  }
}

class Dog extends Animal{
  @override
  eat() {
     print('小狗在吃骨头');
  }

  @override
  run() {
    // TODO: implement run
    print('小狗在跑');
  }  
}
class Cat extends Animal{
  @override
  eat() {
    // TODO: implement eat
    print('小猫在吃老鼠');
  }

  @override
  run() {
    // TODO: implement run
    print('小猫在跑');
  }

}

main(){

  Dog d=new Dog();
  d.eat();
  d.printInfo();

  Cat c=new Cat();
  c.eat();

  c.printInfo();

  // Animal a=new Animal();   //抽象类没法直接被实例化

}
```

#### Dart中的多态：
```
/*
    允许将子类类型的指针赋值给父类类型的指针, 同一个函数调用会有不同的执行效果 。

    子类的实例赋值给父类的引用。
    
    多态就是父类定义一个方法不去实现，让继承他的子类去实现，每个子类有不同的表现。
*/

abstract class Animal{
  eat();   //抽象方法 
}

class Dog extends Animal{
  @override
  eat() {
     print('小狗在吃骨头');
  }
  run(){
    print('run');
  }
}
class Cat extends Animal{
  @override
  eat() {   
    print('小猫在吃老鼠');
  }
  run(){
    print('run');
  }
}

main(){

  // Dog d=new Dog();
  // d.eat();
  // d.run();


  // Cat c=new Cat();
  // c.eat();

  Animal d=new Dog();

  d.eat();


  Animal c=new Cat();

  c.eat();
}
```
    
#### 和Java一样，dart也有接口，但是和Java还是有区别的。
```$xslt
/*
  首先，dart的接口没有interface关键字定义接口，而是普通类或抽象类都可以作为接口被实现。

  同样使用implements关键字进行实现。

  但是dart的接口有点奇怪，如果实现的类是普通类，会将普通类和抽象中的属性的方法全部需要覆写一遍。
  
  而因为抽象类可以定义抽象方法，普通类不可以，所以一般如果要实现像Java接口那样的方式，一般会使用抽象类。

  建议使用抽象类定义接口。
*/

/*
定义一个DB库 支持 mysql  mssql  mongodb

mysql  mssql  mongodb三个类里面都有同样的方法
*/

abstract class Db{   //当做接口   接口：就是约定 、规范
    String uri;      //数据库的链接地址
    add(String data);
    save();
    delete();
}

class Mysql implements Db{
  
  @override
  String uri;

  Mysql(this.uri);

  @override
  add(data) {
    // TODO: implement add
    print('这是mysql的add方法'+data);
  }

  @override
  delete() {
    // TODO: implement delete
    return null;
  }

  @override
  save() {
    // TODO: implement save
    return null;
  }

  remove(){
      
  }
}

class MsSql implements Db{
  @override
  String uri;
  @override
  add(String data) {
    print('这是mssql的add方法'+data);
  }

  @override
  delete() {
    // TODO: implement delete
    return null;
  }

  @override
  save() {
    // TODO: implement save
    return null;
  }
}

main() {
  Mysql mysql=new Mysql('xxxxxx');

  mysql.add('1243214');
}
```    
### Dart 中一个类实现多个接口 以及 Dart 中的 Mixins   
#### Dart中一个类实现多个接口：
```$xslt
abstract class A{
  String name;
  printA();
}

abstract class B{
  printB();
}

class C implements A,B{  
  @override
  String name;  
  @override
  printA() {
    print('printA');
  }
  @override
  printB() {
    // TODO: implement printB
    return null;
  }
}

void main(){
  C c=new C();
  c.printA();
}
```
#### Dart 中的 mixins
```$xslt
/*
mixins的中文意思是混入，就是在类中混入其他功能。

在Dart中可以使用mixins实现类似多继承的功能

因为mixins使用的条件，随着Dart版本一直在变，这里讲的是Dart2.x中使用mixins的条件：

  1、作为mixins的类只能继承自Object，不能继承其他类
  2、作为mixins的类不能有构造函数
  3、一个类可以mixins多个mixins类
  4、mixins绝不是继承，也不是接口，而是一种全新的特性
*/

class A {
  String info="this is A";
  void printA(){
    print("A");
  }
}

class B {
  void printB(){
    print("B");
  }
}

class C with A,B{
  
}

void main(){
  var c=new C();  
  c.printA();
  c.printB();
  print(c.info);
}
```    
#### mixins的实例类型是什么？
```$xslt
/*
很简单，mixins的类型就是其超类的子类型。
*/

class A {
  String info="this is A";
  void printA(){
    print("A");
  }
}

class B {
  void printB(){
    print("B");
  }
}

class C with A,B{
  
}

void main(){  
  var c=new C();  
   
  print(c is C);    //true
  print(c is A);    //true
  print(c is B);   //true

  // var a=new A();
  // print(a is Object);
}
```    
### 泛型 泛型方法 泛型类 泛型接口
* 通俗理解：泛型就是解决 类 接口 方法的复用性、以及对不特定数据类型的支持(类型校验)
```$xslt
  //只能返回string类型的数据

  // String getData(String value){
  //     return value;
  // }
  

  //同时支持返回 string类型 和int类型  （代码冗余）

  // String getData1(String value){
  //     return value;
  // }

  // int getData2(int value){
  //     return value;
  // }



//同时返回 string类型 和number类型       不指定类型可以解决这个问题

  // getData(value){
  //     return value;
  // }

//不指定类型放弃了类型检查。我们现在想实现的是传入什么 返回什么。比如:传入number 类型必须返回number类型  传入 string类型必须返回string类型
 
  // T getData<T>(T value){
  //     return value;
  // }

  getData<T>(T value){
      return value;
  }

void main(){
    // print(getData(21));

    // print(getData('xxx'));

    // getData<String>('你好');

    print(getData<int>(12));
}

```    

#### 集合List 泛型类的用法
```$xslt
//案例：把下面类转换成泛型类，要求List里面可以增加int类型的数据，也可以增加String类型的数据。但是每次调用增加的类型要统一

//  class PrintClass{
//       List list=new List<int>();
//       void add(int value){
//           this.list.add(value);
//       }
//       void printInfo(){          
//           for(var i=0;i<this.list.length;i++){
//             print(this.list[i]);
//           }
//       }
//  }

//  PrintClass p=new PrintClass();
//     p.add(1);
//     p.add(12);
//     p.add(5);
//     p.printInfo();

 class PrintClass<T>{
      List list=new List<T>();
      void add(T value){
          this.list.add(value);
      }
      void printInfo(){          
          for(var i=0;i<this.list.length;i++){
            print(this.list[i]);
          }
      }
 }

main() {  
    // PrintClass p=new PrintClass();
    // p.add(11);
    // p.add('xxx');
    // p.add(5);
    // p.printInfo();

  // PrintClass p=new PrintClass<String>();
  // p.add('你好');
  //  p.add('哈哈');
  // p.printInfo();

  PrintClass p=new PrintClass<int>();

  p.add(12);
  p.add(23);
  p.printInfo();
 
  // List list=new List();
  // list.add(12);
  // list.add("你好");
  // print(list);

  // List list=new List<String>();

  // // list.add(12);  //错误的写法

  // list.add('你好');
  // list.add('你好1');

  // print(list);

  // List list=new List<int>();

  // // list.add("你好");  //错误写法
  // list.add(12); 

  // print(list);
}
```   
#### Dart中的泛型接口    
```$xslt
/*
    实现数据缓存的功能：有文件缓存、和内存缓存。内存缓存和文件缓存按照接口约束实现。
    1、定义一个泛型接口 约束实现它的子类必须有getByKey(key) 和 setByKey(key,value)
    2、要求setByKey的时候的value的类型和实例化子类的时候指定的类型一致
*/
  // abstract class ObjectCache {
  //   getByKey(String key);
  //   void setByKey(String key, Object value);
  // }

  // abstract class StringCache {
  //   getByKey(String key);
  //   void setByKey(String key, String value);
  // }

  // abstract class Cache<T> {
  //   getByKey(String key);
  //   void setByKey(String key, T value);
  // }

abstract class Cache<T>{
  getByKey(String key);
  void setByKey(String key, T value);
}

class FileCache<T> implements Cache<T>{
  @override
  getByKey(String key) {    
    return null;
  }

  @override
  void setByKey(String key, T value) {
   print("我是文件缓存 把key=${key}  value=${value}的数据写入到了文件中");
  }
}

class MemoryCache<T> implements Cache<T>{ 
  @override
  getByKey(String key) {   
    return null;
  }

  @override
  void setByKey(String key, T value) {
       print("我是内存缓存 把key=${key}  value=${value} -写入到了内存中");
  }
}
void main(){
    // MemoryCache m=new MemoryCache<String>();
    //  m.setByKey('index', '首页数据');

     MemoryCache m=new MemoryCache<Map>();
     m.setByKey('index', {"name":"张三","age":20});
}
```    
### Dart 中的库 自定义库 系统库 第三方库    
#### Dart 中的库
```$xslt
/*
前面介绍Dart基础知识的时候基本上都是在一个文件里面编写Dart代码的，但实际开发中不可能这么写，模块化很重要，所以这就需要使用到库的概念。
在Dart中，库的使用时通过import关键字引入的。
library指令可以创建一个库，每个Dart文件都是一个库，即使没有使用library指令来指定。

Dart中的库主要有三种：

    1、我们自定义的库     
          import 'lib/xxx.dart';
    2、系统内置库       
          import 'dart:math';    
          import 'dart:io'; 
          import 'dart:convert';
    3、Pub包管理系统中的库  
        https://pub.dev/packages
        https://pub.flutter-io.cn/packages
        https://pub.dartlang.org/flutter/

        1、需要在自己想项目根目录新建一个pubspec.yaml
        2、在pubspec.yaml文件 然后配置名称 、描述、依赖等信息
        3、然后运行 pub get 获取包下载到本地  
        4、项目中引入库 import 'package:http/http.dart' as http; 看文档使用
*/
```    
#### Dart 中导入自己本地库
```$xslt
import 'lib/Animal.dart';
main(){
  var a=new Animal('小黑狗', 20);
  print(a.getName());
}
```    
#### 导入系统内置库 math 库
```$xslt
// import 'dart:io';
import "dart:math";
main(){
    print(min(12,23));
    print(max(12,25));
}
```
#### 导入系统内置库实现请求数据 httpClient
```$xslt
import 'dart:io';
import 'dart:convert';


void main() async{
  var result = await getDataFromZhihuAPI();
  print(result);
}


//api接口： http://news-at.zhihu.com/api/3/stories/latest
getDataFromZhihuAPI() async{
  //1、创建HttpClient对象
  var httpClient = new HttpClient();  
  //2、创建Uri对象
  var uri = new Uri.http('news-at.zhihu.com','/api/3/stories/latest');
  //3、发起请求，等待请求
  var request = await httpClient.getUrl(uri);
  //4、关闭请求，等待响应
  var response = await request.close();
  //5、解码响应的内容
  return await response.transform(utf8.decoder).join();
}
```    
#### 关于 async await
```$xslt
/*
async和await
  这两个关键字的使用只需要记住两点：
    只有async方法才能使用await关键字调用方法
    如果调用别的async方法必须使用await关键字

async是让方法变成异步。
await是等待异步方法执行完成。
*/

void main() async{
  var result = await testAsync();
  print(result);
}

//异步方法
testAsync() async{
  return 'Hello async';
}
```
#### Dart 导入 pub 包管理系统中的库
```$xslt
/*
pub包管理系统:

1、从下面网址找到要用的库
        https://pub.dev/packages
        https://pub.flutter-io.cn/packages
        https://pub.dartlang.org/flutter/

2、创建一个pubspec.yaml文件，内容如下
    name: xxx
    description: A new flutter module project.
    dependencies:  
        http: ^0.12.0+2
        date_format: ^1.0.6

3、配置dependencies

4、运行pub get 获取远程库

5、看文档引入库使用
*/
import 'dart:convert' as convert;
import 'package:http/http.dart' as http;
import 'package:date_format/date_format.dart';

main() async {
  // var url = "http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=1";

  //   // Await the http get response, then decode the json-formatted responce.
  //   var response = await http.get(url);
  //   if (response.statusCode == 200) {
  //     var jsonResponse = convert.jsonDecode(response.body);
     
  //     print(jsonResponse);
  //   } else {
  //     print("Request failed with status: ${response.statusCode}.");
  //   }
  
  print(formatDate(DateTime(1989, 2, 21), [yyyy, '*', mm, '*', dd]));
```   
#### Dart 库的重命名 Dart 冲突解决
```$xslt
/*
1、冲突解决
当引入两个库中有相同名称标识符的时候，如果是java通常我们通过写上完整的包名路径来指定使用的具体标识符，甚至不用import都可以，但是Dart里面是必须import的。当冲突的时候，可以使用as关键字来指定库的前缀。如下例子所示：
    import 'package:lib1/lib1.dart';
    import 'package:lib2/lib2.dart' as lib2;

    Element element1 = new Element();           // Uses Element from lib1.
    lib2.Element element2 = new lib2.Element(); // Uses Element from lib2.
*/

import 'lib/Person1.dart';
import 'lib/Person2.dart' as lib;

main(List<String> args) {
  Person p1=new Person('张三', 20);
  p1.printInfo();

  lib.Person p2=new lib.Person('李四', 20);
  p2.printInfo();
}
```    
#### 部分导入
```$xslt
/*
部分导入
  如果只需要导入库的一部分，有两种模式：

     模式一：只导入需要的部分，使用show关键字，如下例子所示：

      import 'package:lib1/lib1.dart' show foo;

     模式二：隐藏不需要的部分，使用hide关键字，如下例子所示：

      import 'package:lib2/lib2.dart' hide foo;      
*/

// import 'lib/myMath.dart' show getAge;

 import 'lib/myMath.dart' hide getName;

void main(){
//  getName();
  getAge();
}
```    
#### 延迟加载
```$xslt
/*
延迟加载
    也称为懒加载，可以在需要的时候再进行加载。
    懒加载的最大好处是可以减少APP的启动时间。

    懒加载使用deferred as关键字来指定，如下例子所示：

    import 'package:deferred/hello.dart' deferred as hello;

    当需要使用的时候，需要使用loadLibrary()方法来加载：

    greet() async {
      await hello.loadLibrary();
      hello.printGreeting();
    }
*/
```   
    
    
    
    
    
    
    
    
    
    